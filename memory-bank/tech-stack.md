# Tech Stack

## Overview
This project should use a simple, robust stack focused on Python for cash flow modeling and Streamlit for a lightweight web UI.

## Language
- Python 3.12+
  - Widely supported and stable for numerical and data workflows
  - Good ecosystem for plotting, date handling, and finance logic

## Core Libraries
- `pandas`
  - For structured cash flow data handling and table display
- `numpy`
  - For numeric operations, array math, and discount/PV calculations
- `datetime` / `dateutil`
  - For date arithmetic, frequency handling, and schedule generation

## UI and Visualization
- `streamlit`
  - Simple web UI framework with low overhead
  - Supports tables and charts out of the box
- `plotly` or `altair` (optional)
  - For interactive bar charts and richer visualizations if needed

## Financial / Date Conventions
- `business-duration` or custom date utilities
  - For business-day adjustments and calendars
- Custom day-count convention helpers
  - Support 30/360 and Modified Following conventions per product

## Project Structure
- `models/`
  - Cash flow object definitions and product schedule generators
- `services/`
  - Aggregation, discounting, PV, and IRR valuation functions
- `ui/`
  - Streamlit app and visualization components
- `data/`
  - Example product definitions, sample cash flow inputs, and curves

## Testing
- `pytest`
  - Lightweight and robust Python testing framework
- `pydantic` or dataclasses
  - For validating cash flow object structure and input parameters

## Dependency Management
- `venv`
  - Keep dependencies isolated and reproducible
- `requirements.txt`
  - Simple dependency listing for installation

## Deployment / Running
- Local development via `streamlit run app.py`
- Future deployment on Streamlit Cloud or a simple container if needed

## Goals for the Stack
- Keep the implementation simple and maintainable
- Use standard Python tools and libraries
- Make it easy to extend with multi-product aggregation, currency support, and valuation logic
- Keep the UI lightweight and responsive with Streamlit