# Limitations

## Public evidence and private implementation

The repository describes the author-provided R3 source at a high level. Production code, exact formulas, calibrated settings, private data, and private research infrastructure remain excluded. The private indicator cannot be reconstructed or independently validated from these documents.

## Source inspection is a limited check

The documentation review identified visible components and their timing conventions. It was not a complete code audit, native TradingView compilation, live alert-delivery test, or bar-by-bar replay. Earlier-version testing is not automatically transferable to R3.

## Chart timing can be misleading

A confirmed line may connect earlier extrema, while an open-bar state or developing segment can change. Historical drawing coordinates must not be used as if they were real-time detection timestamps. Object retention can also remove older objects from the display.

## Percentiles are descriptive

A swing-magnitude rank depends on the available historical sample and the segment definition. It is not a reversal probability, prediction confidence, win rate, or elapsed-time percentile. A minimum sample gate does not by itself establish statistical reliability.

## Synthetic demonstration

The public example contains hand-authored prices and event timestamps. It audits timestamp availability and target-window eligibility without generating R3 signals. The small counts and deliberately constructed boundary cases are teaching devices, not empirical estimates or evidence of model quality.

## Generalization and execution

No R3 cross-market predictive study or cost-adjusted trading evaluation is provided here. A plausible visual display cannot establish either. Shared development history with WaveFilter also does not transfer that project's evidence to Trend Filter.
