# Progress

## Step 1 Completed

- Created project package directories: `models/`, `services/`, `ui/`, `data/`, and `utils/`.
- Added root `README.md` containing setup and `streamlit run` instructions.
- Added `requirements.txt` with `streamlit`, `pandas`, `numpy`, and `python-dateutil`.
- Confirmed Step 1 artifacts are present and ready for Step 2.

## Step 2 Completed

- Added `models/cash_flow.py` defining `CashFlow` with required fields.
- Added `models/product_template.py` defining `ProductTemplate` and product convention defaults.
- Exported model classes from `models/__init__.py` for easy imports.

## Step 3 Completed

- Created `services/date_utils.py` with default `30/360` day count logic.
- Added business-day adjustment helpers including `modified_following`.
- Added frequency normalization and quarterly schedule date generation.
- Added `tests/test_date_utils.py` to validate business day behavior and schedule generation.

## Step 4 Completed

- Added `services/schedule_generator.py` to generate validated cash flow schedules from product parameters.
- Implemented validation for required product fields, frequency rules, and date ordering.
- Added `tests/test_schedule_generator.py` to verify schedule output, maturity handling, and invalid input errors.

## Step 5 Completed

- Added `services/portfolio.py` for merging product schedules and aggregating cash flows by date and currency.
- Added `tests/test_portfolio.py` to verify schedule merging, aggregation, and currency-aware summaries.
- Confirmed Step 5 via `venv\Scripts\python.exe -m pytest tests/test_portfolio.py`.
