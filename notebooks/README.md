# Public Timing Notebook

[public_timing_demo.ipynb](public_timing_demo.ipynb) contains a fully executed illustration of historical anchor time versus event confirmation time. Read the [result page](../results/public_timing_results.md) without running code, or inspect the notebook's saved table and chart.

The event timestamps and price path are deliberately constructed. The demo does not detect turning points, implement Trend R3, or use private data or settings.

## Run from the repository root

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
jupyter nbconvert --to notebook --execute --inplace notebooks/public_timing_demo.ipynb --ExecutePreprocessor.timeout=120
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.

The notebook imports [demo/timing_demo.py](../demo/timing_demo.py), regenerates the public CSV, result page, and SVG chart, and saves its own output. To regenerate only those artifacts, run `python demo/timing_demo.py`.

Requirements use supported ranges. The saved notebook prints the exact Python and plotting-library versions used for its execution. CI reruns the checks and notebook and compares the generated ledger and result text with the committed files.

The test suite checks event availability, the effect of future event records, split-boundary inclusion, incomplete future windows, and invalid event logs. These are tests of this public example, not tests of the private R3 implementation.
