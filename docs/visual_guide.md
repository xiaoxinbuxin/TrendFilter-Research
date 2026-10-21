# Visual Guide

This guide describes the visible roles and timing found in the author-provided Trend R3 source. It does not publish the indicator's formulas, thresholds, or calibrated settings. Source inspection is not a substitute for native-platform compilation, replay, or predictive evaluation.

## Trend-state bands

The main chart uses bullish support, bearish pressure, and range-state shading to represent the indicator's current context. These states describe the model's classification rather than an objectively known future market direction.

The trend-state calculation is not wholly restricted to confirmed bars. Its appearance on an open bar can change as prices update. Close-confirmed labels must therefore not be used to describe the entire overlay as fixed throughout the bar.

## Contextual labels

The indicator classifies local price events using the trend context. The displayed vocabulary includes pullbacks, bounces, trend and range labels, and potential top or bottom labels. Label generation is evaluated at bar close.

A potential top or bottom is an interpretation of current conditions, not a guaranteed reversal. Historical object retention is bounded; visible labels should not be treated as a complete event archive.

## Swing percentile

The optional percentage describes normalized swing magnitude relative to stored same-direction historical swings. The source uses a sample-availability gate before displaying the percentile. This is a statistical description of observed amplitude: it does not estimate the distance to a future peak or trough.

The percentage is not the probability that the next move reverses, not a trade win rate, and not the percentage of comparable swings exceeded in elapsed time. When no percentage is displayed, the absence is not evidence of a low reversal probability.

## Swing skeleton and confirmation time

Confirmed segments connect historical extrema. Their objects are created when the segment is confirmed, while their coordinates refer to the earlier extreme bars. A historical chart can therefore display a turning-point location that was not yet confirmed at that location's timestamp.

Any evaluation must use the actual confirmation time as the time at which that information became available. The developing segment can update, and earlier objects can be removed under the retention policy. The selected line style is a display setting; a dashed appearance alone is not a reliable test of confirmation status.

## Moving-average references and alerts

Moving-average lines provide recent price context. They can respond while the bar is open. Alert conditions cover label events and state changes; this repository does not claim that native alert delivery has been verified.

## Relationship to other indicators

Trend R3 displays context directly on the price chart; WaveFilter provides a sub-chart representation. A screenshot containing both projects must identify which chart region belongs to each. Neither a visual match nor simultaneous signals establish independent statistical evidence.
