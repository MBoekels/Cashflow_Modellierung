# Cashflow Modellierung

A modular cash flow modeling application built with Python and Streamlit.

## Project Structure

- `models/` - data models for cash flows and products
- `services/` - business logic, schedule generation, aggregation, and utilities
- `ui/` - Streamlit application components
- `data/` - sample data and configuration files
- `utils/` - date math, currency helpers, and utilities

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run ui/app.py
```
