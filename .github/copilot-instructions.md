# Project Instructions: Financial Cashflow Modeler

# CRITICAL RULES (Read First)
1. **Memory Bank Access:** Always read `memory-bank/@architecture.md` and `memory-bank/@product-requirements.md` before generating code.
2. **Anti-Monolith Policy:** NEVER suggest adding more than 100 lines of code to a single file. If a feature is complex, split it into `models/`, `services/`, or `utils/`.
3. **File Creation:** When providing code, ALWAYS specify the target file path at the top of the snippet (e.g., `# File: services/aggregators.py`).
4. **Consistency:** After any major architectural change, explicitly remind the user to update `memory-bank/@architecture.md`.

## Tech Stack & Financial Logic
- **Environment:** Python 3.12+, Streamlit (UI), Pandas/Numpy (Data).
- **Core Logic:** - Default Day-Count: 30/360.
    - Business-Day Adjustment: Following Business Day.
    - Support per-product overrides for these conventions.
- **Data Structure:** Multi-currency support is mandatory from day one.

## Project Architecture (Strict Enforcement)
Follow this modular layout. Do not create files in the root unless they are config files:
- `models/`: Data classes and TypedDicts for CashFlows and Products.
- `services/`: The "Engine Room." Schedule generators, Day-count math, and IRR/Discounting.
- `ui/`: Streamlit components and page layouts.
- `utils/`: Date math, currency conversion helpers, and holiday calendars.

## When Responding to Code Requests
- **Think in Steps:** First, describe which file needs to be created or modified. 
- **Modular Scaffolding:** If asked to "build the app," provide a directory structure first, then individual file contents.
- **Don't Over-Comment:** Write self-documenting code with clear variable names (e.g., `calculate_discounted_present_value` instead of `calc_pv`).
- **Imports:** Use absolute imports (e.g., `from models.cash_flow import CashFlow`).

## Maintenance
- Ensure every CashFlow object includes: `product_name`, `type`, `date`, `amount`, `currency`, and `description`.
- Keep the `Streamlit` UI decoupled from the `services` logic. The UI should only call service functions and display results.