# Evaluation Scope

This document defines an evidence-reporting structure. It is not a record of tests completed or passed.

## Implementation behavior

An implementation report should identify the exact version and distinguish between source inspection, reference-model tests, and native-platform results. It should document when displayed state and labels become observable, how incomplete history is handled, and what may change before a bar closes.

## Historical replay

A replay report should identify the data source, instruments, timeframes, observation dates, missing-data policy, and treatment of the final bar. Any comparison should use aligned inputs and distinguish state agreement from label agreement.

Agreement with a reference implementation does not establish that either implementation predicts future prices.

## Statistical interpretation

Swing statistics summarize a specified historical sample. Their interpretation depends on how swings are defined, when they become confirmed, and which completed observations enter the sample. A rank within that sample is not, by itself, a future-reversal probability.

## Predictive evaluation

A separate predictive study would need an explicit target, baseline, event timing, sample and event counts, time-ordered evaluation boundaries, and uncertainty analysis. Previously inspected or repeatedly used data should not be presented as a fresh sealed holdout.

Trading-performance claims would additionally require explicit execution and cost assumptions. No such performance claim is made in this repository.
