"""Standalone synthetic event-log example; does not implement Trend R3."""

import csv
from pathlib import Path


def synthetic_example():
    """Hand-authored illustration, with no signal-detection rule or fitted settings."""
    knots = [(0, 100), (8, 106), (24, 98), (40, 109), (53, 101), (72, 111), (79, 107)]
    prices = []
    for bar in range(80):
        for (left, a), (right, b) in zip(knots, knots[1:]):
            if left <= bar <= right:
                prices.append(a + (b - a) * (bar - left) / (right - left))
                break
    events = [
        {"event_id": name, "anchor_bar": anchor, "confirmed_bar": confirmed}
        for name, anchor, confirmed in [
            ("A", 8, 12), ("B", 24, 28), ("C", 40, 51),
            ("D", 53, 59), ("E", 72, 76),
        ]
    ]
    return prices, events


def event_ledger(events, *, n_bars, split_bar, horizon):
    """Audit supplied events; horizon starts after the confirmation bar."""
    if n_bars < 2 or not 0 < split_bar < n_bars or horizon < 1:
        raise ValueError("Invalid timeline or horizon")
    rows = []
    ids = set()
    for event in events:
        name = event["event_id"]
        anchor, confirmed = event["anchor_bar"], event["confirmed_bar"]
        if name in ids or not 0 <= anchor <= confirmed < n_bars:
            raise ValueError("Event IDs must be unique and timestamps ordered")
        ids.add(name)
        target_end = confirmed + horizon
        if target_end >= n_bars:
            status = "excluded_incomplete_future"
        elif confirmed < split_bar <= target_end:
            status = "purged_at_split"
        elif confirmed < split_bar:
            status = "development"
        else:
            status = "holdout"
        rows.append({
            **event,
            "confirmation_delay_bars": confirmed - anchor,
            "target_start_bar": confirmed + 1,
            "target_end_bar": target_end,
            "status": status,
        })
    return rows


def available_events(events, through_bar):
    """Only confirmed records are available, irrespective of their plotted anchor."""
    return [dict(event) for event in events if event["confirmed_bar"] <= through_bar]


def write_snapshot(root):
    import matplotlib.pyplot as plt

    root = Path(root)
    (root / "results").mkdir(exist_ok=True)
    (root / "figures").mkdir(exist_ok=True)
    prices, events = synthetic_example()
    # Public illustration settings only; not Trend R3 settings.
    split_bar, horizon = 56, 8
    rows = event_ledger(events, n_bars=len(prices), split_bar=split_bar, horizon=horizon)
    with (root / "results/synthetic_event_ledger.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    with plt.rc_context({"font.size": 10, "svg.fonttype": "none", "svg.hashsalt": "trend-timing-demo"}):
        fig, axes = plt.subplots(2, 1, figsize=(11, 6.4), sharex=True, gridspec_kw={"height_ratios": [1.35, 1]})
        fig.suptitle("Synthetic illustration: plotted position and information availability", fontsize=14, fontweight="bold")
        axes[0].plot(range(len(prices)), prices, color="#243b53", linewidth=1.8)
        for event in events:
            a, c = event["anchor_bar"], event["confirmed_bar"]
            axes[0].scatter(a, prices[a], marker="x", color="#c05621", s=55)
            axes[0].scatter(c, prices[c], marker="o", color="#147d92", s=35)
            axes[0].annotate(event["event_id"], (a, prices[a]), xytext=(0, 8), textcoords="offset points", ha="center")
        axes[0].plot([], [], marker="x", linestyle="none", color="#c05621", label="Historical anchor")
        axes[0].plot([], [], marker="o", linestyle="none", color="#147d92", label="Confirmation time")
        axes[0].legend(loc="upper left", frameon=False, ncol=2)
        axes[0].set_ylabel("Illustrative price")
        colors = {"development": "#147d92", "holdout": "#4d7c0f", "purged_at_split": "#b7791f", "excluded_incomplete_future": "#9b2c2c"}
        for i, row in enumerate(rows):
            a, c = row["anchor_bar"], row["confirmed_bar"]
            axes[1].plot([a, c], [i, i], color="#a0aec0", linewidth=2)
            axes[1].scatter(a, i, marker="x", color="#c05621", s=45)
            axes[1].scatter(c, i, color=colors[row["status"]], s=40)
            axes[1].plot([c + 1, row["target_end_bar"]], [i, i], linewidth=4, color=colors[row["status"]], alpha=.65)
        axes[1].set_yticks(range(len(rows)), [f"{r['event_id']}: {r['status'].replace('_', ' ')}" for r in rows])
        axes[1].invert_yaxis()
        axes[1].set_xlabel("Synthetic bar index (0–79 observed; later positions have no data)")
        axes[1].set_ylim(len(rows) - .5, -.7)
        for ax in axes:
            ax.axvline(split_bar, color="#5f6c7b", linestyle="--", linewidth=1)
            ax.axvspan(79.5, 85, color="#edf2f7")
            ax.spines[["top", "right"]].set_visible(False)
            ax.grid(axis="x", alpha=.15)
            ax.set_xlim(-1, 85)
        axes[0].text(split_bar + .8, 110.5, "Split", color="#5f6c7b")
        fig.tight_layout(rect=(0, .02, 1, .95))
        fig.savefig(root / "figures/synthetic_timing.svg", metadata={"Date": None}, bbox_inches="tight")
        svg = root / "figures/synthetic_timing.svg"
        svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines()) + "\n")

    counts = {status: sum(row["status"] == status for row in rows) for status in colors}
    table = "\n".join(f"| {r['event_id']} | {r['anchor_bar']} | {r['confirmed_bar']} | {r['confirmation_delay_bars']} | {r['target_start_bar']}–{r['target_end_bar']} | {r['status']} |" for r in rows)
    report = f"""# Executed Synthetic Timing Example

Generated from [the public demo](../notebooks/public_timing_demo.ipynb). **All prices and event timestamps are hand-authored illustrations. No Trend R3 signal logic, private data, or fitted settings are used.**

## What this demonstrates

An annotation may be drawn at an earlier price extreme after confirmation. The plotted coordinate cannot be used as the time at which the event became available. This example audits a supplied event log; it does not discover or predict turning points.

There are {len(prices)} synthetic bars and {len(rows)} illustrative events. The demonstration split begins at bar {split_bar}; an evaluation window spans the next {horizon} bars after confirmation. These are teaching settings, not production settings or a sealed study.

| Event | Historical anchor | Confirmation | Delay (bars) | Future window | Eligibility |
|---|---:|---:|---:|---|---|
{table}

Eligible development events: **{counts['development']}**. Eligible holdout events: **{counts['holdout']}**. Purged at the split: **{counts['purged_at_split']}**. Excluded for an incomplete future window: **{counts['excluded_incomplete_future']}**.

Event C cannot stay in development because its future window reaches the holdout. Event E cannot be evaluated because part of its future window is outside the observed timeline. No return or hit-rate statistic is calculated from this deliberately small example.

![Synthetic event timing and evaluation windows](../figures/synthetic_timing.svg)

## What this does not establish

The checks cover this public event-log example only. They do not verify Trend R3's event generation, prove absence of repainting, establish TradingView/Python parity, or show trading performance. Actual chart replay must record when an object appeared, not merely its final historical coordinates.

[Event ledger](synthetic_event_ledger.csv) · [Run instructions](../notebooks/README.md) · [R3 evidence status](evidence_status.md)
"""
    (root / "results/public_timing_results.md").write_text(report)
    return rows, fig


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    rows, fig = write_snapshot(Path(__file__).resolve().parents[1])
    print(f"Generated a synthetic ledger for {len(rows)} illustrative events.")
    plt.close(fig)
