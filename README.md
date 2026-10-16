# 趋势过滤器 · Trend Filter Research

**A main-chart indicator research project developed from 波段过滤器 (WaveFilter).**

Trend Filter became a separate project when additional price-chart functionality was split out of the WaveFilter development process. Keeping the two projects separate allows the main-chart tools and the sub-chart wave representation to develop around their respective roles.

The selected project milestone is **趋势 R3 (Trend R3)**.

## Research focus

The project concerns how to organize and communicate market context directly on a price chart. Its documentation separates three questions: what the indicator displays, whether its implementation behaves consistently, and whether any proposed use has supporting empirical evidence.

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

## Start here

- [Project background](docs/project_background.md) explains the separation and the selected R3 milestone.
- [Evaluation scope](docs/evaluation_scope.md) distinguishes implementation checks, replay, statistical interpretation, and predictive evaluation.
- [Disclosure boundary](NOTICE.md) identifies material excluded from this public portfolio.

## Evidence status

The component descriptions have been checked against the author-provided Trend R3 source. This is a source-level documentation check, not a completed implementation audit. The public repository does not include a reproducible R3 evaluation, native TradingView compilation or replay evidence, or performance statistics. No passing-test count, prediction-accuracy claim, or trading return is asserted here.

Screenshots or numerical results from other versions, and the synthetic demonstration in WaveFilter-Research, do not establish the behavior or effectiveness of Trend R3. Any future evidence should identify its version, data, evaluation procedure, and limitations.

## Scope

The production Pine Script, exact formulas, calibrated settings, private test infrastructure, raw private data, and execution-specific rules remain private. The R3 version label identifies the selected milestone; it is not a certification of correctness or predictive performance.

This repository is intended for research discussion and portfolio review. Chart appearance alone cannot establish predictive accuracy, profitability, or validity across markets.
