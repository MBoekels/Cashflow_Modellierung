# Implementation Plan

This plan focuses on building the base application for cash flow modeling with a Streamlit UI and a minimal, extensible architecture.

## 1. Initialize Project Structure

1. Create the top-level directories: `models/`, `services/`, `ui/`, `data/`, and `utils/`.
   - Test: Verify the directories exist and are empty placeholders.
2. Add a root `README.md` with a short description of the application and execution instructions.
   - Test: Open `README.md` and confirm it documents how to run the app with `streamlit run`.
3. Create a dependency manifest file such as `requirements.txt` or `pyproject.toml`.
   - Test: Confirm the file lists `streamlit`, `pandas`, and `numpy`.

## 2. Define the Cash Flow Data Model

1. Create a `models/cash_flow.py` file defining a cash flow data class or typed model.
   - Include fields: `product_name`, `type`, `date`, `amount`, `currency`, `description`.
   - Test: Import the model and instantiate one example cash flow record.
2. Create a `models/product_template.py` file for generic product parameters and template metadata only.
   - Product templates should be data models; schedule generation logic will live in `services/`.
   - Test: Instantiate the template object and verify default field values.

## 3. Implement Core Date and Convention Utilities

1. Create `services/date_utils.py` with helpers for day-count and business-day rules.
   - Include default 30/360 and Modified Following behavior.
   - Ensure the product model can expose per-product day-count and business-day convention overrides.
   - Test: Validate that a sample date adjustment returns the expected business day.
2. Add a helper to normalize payment frequencies and generate date sequences.
   - Test: Confirm a quarterly sequence from a start date produces correct dates.

## 4. Build Cash Flow Schedule Generation Logic

1. Create `services/schedule_generator.py` that converts product parameters into cash flow lists.
   - Accept inputs such as notional, rate, term, frequency, start date, currency, day-count, and business-day rules.
   - Use a generic schedule generator for now, with product templates providing only metadata.
   - Test: Generate a simple schedule and verify output is a sorted list of cash flow objects.
2. Implement validation for required product fields and date ordering.
   - Test: Pass invalid input and confirm the function raises a meaningful validation error.

## 5. Implement Portfolio Aggregation Services

1. Create `services/portfolio.py` for combining multiple product schedules.
   - Provide a function to merge schedules and aggregate totals by date and currency.
   - Use `EUR` as the base currency for the model, while allowing each cash flow object to retain its own currency attribute.
   - For the first version, support per-currency aggregations only and keep future FX conversion extension in mind.
   - Test: Combine two sample schedules and confirm the output includes both product cash flows.
2. Add a summary helper that calculates total inflows and outflows.
   - Test: Verify the summary numbers match the combined schedule totals.

## 6. Build Basic Streamlit UI

1. Create `ui/app.py` for the Streamlit application entry point.
   - Add sections for product input, cash flow table, and chart display.
   - Test: Run the app locally and confirm the Streamlit page loads.
2. Add a table view that displays the combined cash flow schedule using `pandas.DataFrame`.
   - Test: Confirm the table renders without error when given sample data.
3. Add a bar chart view for cash flow amounts by date.
   - Test: Confirm the chart renders successfully using Streamlit chart APIs.

## 7. Wire Components Together

1. Connect the UI input form to the schedule generator and portfolio service.
   - Test: Enter sample parameters and confirm the UI updates with a table and chart.
2. Ensure the UI can accept at least one sample product and display the resulting cash flow schedule.
   - Test: Verify that the displayed cash flow list contains the expected number of rows.

## 8. Add Basic Validation and Error Handling

1. Implement input validation in the UI and services to catch missing or invalid fields.
   - Test: Submit invalid input and verify the UI shows a clear error message.
2. Add defensive checks for empty schedules or unsupported currencies.
   - Test: Pass an unsupported currency or zero term and confirm the app handles it gracefully.

## 9. Create Basic Tests

1. Add a `tests/` directory with unit tests for model creation, date utilities, schedule generation, and aggregation.
   - Test: Run `pytest` and confirm all base tests pass.
2. Add a smoke test for the Streamlit app entry point that imports `app.py` without failure.
   - Test: Run the import test and confirm there are no import errors.

## 10. Document the Base Application

1. Update `README.md` with project goals, structure, setup instructions, and how to run the Streamlit app.
   - Test: Read the `README.md` and confirm it includes a runnable command and expected behavior.
2. Add a short note in `memory-bank/implementation-plan.md` describing what is complete versus future enhancements.
   - Test: Confirm the implementation plan reflects the current project state.
