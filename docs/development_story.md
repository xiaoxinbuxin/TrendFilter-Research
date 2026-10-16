# Development Story

## Why a separate main-chart project

Trend Filter originated within the author's 波段过滤器 (WaveFilter) development. The author separated the main-chart work when adding more functionality, so the sub-chart wave representation would not have to carry every price-chart feature.

This origin matters when presenting the projects together: they are related parts of one development history, with different chart roles. Creating two repositories does not create two independent bodies of validation evidence.

## What the separation makes easier to describe

The sub-chart project represents normalized wave and market-state information. The main-chart project places context alongside price: trend-state bands, contextual labels, a swing skeleton, swing percentiles, and recent moving-average references.

Separating their documentation makes it possible to ask different questions of each display. A state band describes context, a label identifies a condition at a particular time, and a swing skeleton describes geometry that may only become confirmed later. Those roles should not be treated as interchangeable predictions.

## The current R3 milestone

The author selected 趋势 R3 as the final version for this portfolio and supplied its source for documentation review. The [visual guide](visual_guide.md) records the roles and timing visible in that source without disclosing formulas or calibrated settings.

The public account does not infer a release chronology from filenames or import test claims from earlier versions. It records the confirmed origin, the selected milestone, and the currently inspectable documentation.

## A central evaluation question

A historical turning-point marker has two relevant times: the bar where it is drawn and the later bar where the information became available. Conflating them can make a retrospective chart look more timely than the event stream actually was.

The [public timing example](../results/public_timing_results.md) isolates that distinction using constructed prices and event timestamps. It is educational code for evaluating a supplied event log, not a reproduction of Trend R3.

## What remains to be established

A fuller R3 study would need version-specific native-platform observations, an event log with confirmation times, a documented data universe, and explicit evaluation targets. The repository does not treat those requirements as completed simply because the design can be described clearly.
