# Architecture

The diagram maps public responsibilities rather than private calculations. Its arrows indicate conceptual relationships, not the complete execution order or a reconstruction of Trend R3.

![Trend Filter public component map](../figures/architecture.svg)

## Trend context and event interpretation

Trend-state bands provide bullish, bearish, or range context. Contextual labels describe local price conditions using that context. State visualization and label availability have different timing: labels are evaluated at bar close, while the trend-state calculation is not wholly restricted to confirmed bars.

## Swing description

The swing subsystem supplies historical geometry and descriptive percentile context. A confirmed segment is drawn between historical extreme coordinates, but becomes available only at its confirmation time. A developing segment can change.

The percentile ranks normalized swing magnitude against stored same-direction observations. It does not independently estimate future direction or a reversal probability.

## Moving averages and output objects

Recent moving-average references provide additional price context. Lines, labels, shading, and alert conditions are output interfaces. Object retention limits mean that a rendered chart is not a complete research database.

## Research interfaces

A reproducible study needs a separate event record containing version, data source, historical anchor, actual confirmation time, and evaluation eligibility. A static screenshot cannot supply all of those fields.

See [Methodology](methodology.md) for an evaluation plan and [Visual guide](visual_guide.md) for display interpretation. No production formulas or parameter values are included here.
