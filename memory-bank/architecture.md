# Architecture Overview

This project is designed as a modular Python application with a clean separation of responsibilities. The files are:

- `models/__init__.py`: defines the `models` package and exports the core data classes.
- `models/cash_flow.py`: defines the `CashFlow` dataclass with required fields `product_name`, `type`, `date`, `amount`, `currency`, and `description`.
- `models/product_template.py`: defines the `ProductTemplate` dataclass with product metadata and default conventions.
- `services/__init__.py`: defines the `services` package and contains schedule generation, aggregation, business logic, and convention helpers.
- `services/date_utils.py`: contains day-count conventions, business-day adjustment, frequency normalization, and schedule date generation.
- `services/schedule_generator.py`: converts product parameters into validated cash flow schedules and returns ordered `CashFlow` objects.
- `ui/__init__.py`: defines the `ui` package and will contain Streamlit app entry points and UI components.
- `data/__init__.py`: defines the `data` package for sample inputs or future configuration files.
- `utils/__init__.py`: defines the `utils` package for reusable helpers such as currency utilities and common helpers.
- `README.md`: documents installation, project structure, and how to run the app.
- `requirements.txt`: declares the initial dependencies needed for the application.
- `pyproject.toml`: configures the project metadata and `pytest` settings for future test execution.
