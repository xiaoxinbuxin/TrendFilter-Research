# Development Story

## Research question and design rationale

How can a price chart communicate both trend context and the relative magnitude of a move? Trend Filter addresses this question through trend-state bands, contextual labels, a swing skeleton, swing percentiles, and recent moving-average references.

Momentum and price displacement describe different aspects of a move. The magnitude component measures observed swings and compares their normalized sizes with a historical sample of same-direction swings. It supplies statistical context for reading the chart, rather than a direct estimate of remaining upside or downside.

## Distinct roles within the display

A state band describes context, a label identifies a condition at a particular time, and a swing skeleton describes geometry that may only become confirmed later. A percentile summarizes the relative magnitude of the observed swing. These roles should not be treated as interchangeable predictions.

## The current R3 milestone

The author selected Trend R3 as the final version for this portfolio and supplied its source for documentation review. The [visual guide](visual_guide.md) records the roles and timing visible in that source without disclosing formulas or calibrated settings.

The public account does not infer a release chronology from filenames or import test claims from earlier versions. It records the research scope, the selected milestone, and the currently inspectable documentation.

## A central evaluation question

A historical turning-point marker has two relevant times: the bar where it is drawn and the later bar where the information became available. Conflating them can make a retrospective chart look more timely than the event stream actually was.

The [public timing example](../results/public_timing_results.md) isolates that distinction using constructed prices and event timestamps. It is educational code for evaluating a supplied event log, not a reproduction of Trend R3.

## What remains to be established

A fuller R3 study would need version-specific native-platform observations, an event log with confirmation times, a documented data universe, and explicit evaluation targets. The repository does not treat those requirements as completed simply because the design can be described clearly.
