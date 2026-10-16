# 趋势过滤器 · Trend Filter Research

[![Public timing demo](https://github.com/xiaoxinbuxin/TrendFilter-Research/actions/workflows/public-demo.yml/badge.svg)](https://github.com/xiaoxinbuxin/TrendFilter-Research/actions/workflows/public-demo.yml)

**Research on price-chart context, swing interpretation, and confirmation-aware evaluation.**

Trend Filter became a separate project when additional price-chart functionality was split out of the WaveFilter development process. Keeping the two projects separate allows the main-chart tools and the sub-chart wave representation to develop around their respective roles.

The selected project milestone is **趋势 R3 (Trend R3)**.

## Research focus

The project concerns how to organize and communicate market context directly on a price chart. Its documentation separates three questions: what the indicator displays, whether its implementation behaves consistently, and whether any proposed use has supporting empirical evidence.

## Start here

| Material | What you can inspect | Evidence boundary |
|---|---|---|
| [Executed timing demo](results/public_timing_results.md) | Event availability, complete future windows, boundary exclusions, and a chart | Hand-authored synthetic example; no R3 signal generation |
| [Architecture](docs/architecture.md) and [visual guide](docs/visual_guide.md) | Public component roles and how to read their timing | Source-level documentation, not a full implementation audit |
| [Development story](docs/development_story.md) | Why the main-chart work was separated and what R3 represents | Confirmed project background, not an invented release history |
| [Evidence status](results/evidence_status.md) | Which materials are public and which validations remain unavailable | Public-demo checks are separate from R3 validation |

## Public timing demonstration

A turning-point marker can be drawn at a historical extreme after the event is confirmed. Evaluating it as if it had been known at that earlier extreme would give the analysis information it did not yet have.

The [executed notebook](notebooks/public_timing_demo.ipynb) demonstrates that distinction with constructed prices and an explicit event log. It also excludes incomplete future windows and purges development events whose targets reach the holdout. The saved [result page](results/public_timing_results.md) includes the complete ledger and interpretation.

![Synthetic anchor and confirmation-time example](figures/synthetic_timing.svg)

This example audits supplied timestamps rather than detecting turning points. Its five events are teaching cases, not R3 performance observations. [Run instructions](notebooks/README.md) explain how to reproduce it; automated checks execute the notebook and compare the generated event ledger and result text.

## Development path

The project began within 波段过滤器 (WaveFilter). Additional price-chart functionality motivated a separate main-chart project, and the author selected **趋势 R3** as the milestone documented here.

The split gives the main-chart work its own questions: how to present trend context, how to distinguish developing structure from confirmed history, and how to interpret swing statistics without turning descriptive ranks into forecasts. The [development story](docs/development_story.md) explains this scope; the [project background](docs/project_background.md) records its relationship to WaveFilter.

## Project relationship

| Project | Chart role | Public record |
|---|---|---|
| **趋势过滤器 / Trend Filter** | Main-chart indicator | This repository: project background, research scope, and evidence boundaries |
| **波段过滤器 / WaveFilter** | Sub-chart wave and market-state representation | [WaveFilter-Research](https://github.com/xiaoxinbuxin/WaveFilter-Research): development history, selected screenshots, and a separate synthetic evaluation demo |

Trend Filter originated within the author's WaveFilter development work and was separated to accommodate additional functionality. The two repositories document related parts of that development history; they should not be counted as independent validation of the same claims.

## Visible components

| Component | What it displays | How to read it |
|---|---|---|
| Trend-state bands | Bullish support, bearish pressure, and a range state | Model-defined context; the open bar can still change |
| Contextual labels | Local price events classified by the current trend state | Evaluated at bar close; not instructions to enter a trade |
| Swing percentile | The current normalized swing magnitude relative to stored same-direction swings | A descriptive rank, not a reversal probability or elapsed-time percentile |
| Swing skeleton | Lines joining historical swing extremes once a segment is confirmed, plus a developing segment | Historical placement is different from the later confirmation time; the current segment can change |
| Moving-average references | A compact recent-price reference | Context for interpretation, not independent validation |

See [Visual guide](docs/visual_guide.md) for timing and interpretation details.

## System overview

![Trend Filter public component map](figures/architecture.svg)

The architecture separates trend context, swing description, and price references. Its arrows show conceptual responsibilities, not production calculations. Read [Architecture](docs/architecture.md) for the component relationships.

## How the project should be evaluated

The [methodology](docs/methodology.md) begins with version and feed identification, distinguishes historical anchors from actual confirmation times, and separates implementation consistency from predictive utility. Any predictive study needs a defined target, baseline, chronological evaluation boundaries, and uncertainty analysis. Trading claims would require additional execution assumptions.

The [evaluation scope](docs/evaluation_scope.md) describes those requirements; it is not a list of completed R3 tests.

## Evidence status

The component descriptions have been checked against the author-provided Trend R3 source. This is a source-level documentation check, not a completed implementation audit. The public repository includes an executed synthetic event-log example and checks for that example. It does not include a reproducible R3 evaluation, native TradingView compilation or replay evidence, or R3 performance statistics. No R3 passing-test count, prediction-accuracy claim, or trading return is asserted here.

Screenshots or numerical results from other versions, and the synthetic demonstration in WaveFilter-Research, do not establish the behavior or effectiveness of Trend R3. Any future evidence should identify its version, data, evaluation procedure, and limitations.

## Repository guide

| Directory | Contents |
|---|---|
| [docs/](docs/README.md) | Development story, architecture, interpretation, methodology, and limitations |
| [notebooks/](notebooks/README.md) | Executed public notebook and reproduction instructions |
| [demo/](demo/timing_demo.py) | Standalone synthetic event-log example |
| [results/](results/README.md) | Generated synthetic results and R3 evidence status |
| [figures/](figures/README.md) | Conceptual architecture and synthetic timing chart |
| [tests/](tests/test_timing_demo.py) | Regression checks for the public example |

## Scope

The production Pine Script, exact formulas, calibrated settings, private test infrastructure, raw private data, and execution-specific rules remain private. The R3 version label identifies the selected milestone; it is not a certification of correctness or predictive performance.

This repository is intended for research discussion and portfolio review. Chart appearance alone cannot establish predictive accuracy, profitability, or validity across markets.

See [Limitations](docs/limitations.md) and the [disclosure boundary](NOTICE.md) for the scope of the public material.
