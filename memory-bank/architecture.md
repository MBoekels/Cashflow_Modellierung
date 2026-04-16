# Architecture Overview

This project is designed as a modular Python application with a clean separation of responsibilities. The initial files created in Step 1 are:

- `models/__init__.py`: defines the `models` package and exports the core data classes.
- `models/cash_flow.py`: defines the `CashFlow` dataclass with required fields `product_name`, `type`, `date`, `amount`, `currency`, and `description`.
- `models/product_template.py`: defines the `ProductTemplate` dataclass with product metadata and default conventions.
- `services/__init__.py`: defines the `services` package and will contain schedule generation, aggregation, and business logic.
- `ui/__init__.py`: defines the `ui` package and will contain Streamlit app entry points and UI components.
- `data/__init__.py`: defines the `data` package for sample inputs or future configuration files.
- `utils/__init__.py`: defines the `utils` package for reusable helpers such as date math and currency utilities.
- `README.md`: documents installation, project structure, and how to run the app.
- `requirements.txt`: declares the initial dependencies needed for the application.
