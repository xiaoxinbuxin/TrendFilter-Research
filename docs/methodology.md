# Research Methodology

This is a proposed evaluation protocol for the documented R3 roles. It is not a claim that the full protocol has already been completed.

## 1. Identify the version and observation conditions

Record the exact implementation revision, chart feed, symbol, timeframe, loaded history, and whether observations concern historical bars, closed real-time bars, or an open bar. Keep screenshots separate from event-level evidence.

## 2. Audit information availability

For every plotted historical object, record both its anchor time and the time it was created or confirmed. Preserve events that later appear unfavorable. Record removals caused by display retention separately from changes to the underlying event log.

Open-bar state changes, close-confirmed labels, developing swing segments, and confirmed historical geometry should be inspected separately. A claim about one does not automatically apply to the entire indicator.

## 3. Check implementation before predictive utility

Use native-platform compilation and replay to observe the intended version. If a separate implementation is used for analysis, compare aligned event timestamps and relevant states. A matching screenshot is insufficient to establish parity.

The public Python example checks a supplied synthetic event log only. Its tests do not test R3's event detector or certify that R3 cannot repaint.

## 4. Define a question and a baseline

Decide whether a study concerns descriptive consistency, event frequency, confirmation delay, subsequent price behavior, or an executable strategy. Define the target and baseline before evaluation. Swing percentiles should not be relabeled as probability estimates without a separate calibration study.

## 5. Respect time boundaries

Start future targets after the actual confirmation time. Exclude incomplete future windows and purge development events whose target windows reach a later evaluation segment. Report sample and event counts alongside exclusions.

Previously examined data is development evidence. It should not be described as a fresh sealed holdout merely because a chronological split was applied again.

## 6. Report uncertainty and failure cases

A statistical study should address event overlap, time dependence, different market regimes, and selection across candidate rules. Trading claims additionally require executable entry timing, costs, slippage, and risk assumptions. Report null or unfavorable outcomes along with positive ones.

[Evaluation scope](evaluation_scope.md) describes the evidence categories. [Evidence status](../results/evidence_status.md) states which of them are currently public.
