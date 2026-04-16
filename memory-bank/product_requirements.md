# Product Requirements

## 1. Project Overview

This application models cash flows from financial products in a flexible framework. The main goal is to create reusable methods that generate structured cash flow schedules, then combine multiple products and visualize the resulting cash flows in a clear and responsive Streamlit web UI.

## 2. Goals

- Model cash flows for different financial products using Python.
- Provide methods that take product parameters and return lists of cash flow objects.
- Support cash flow objects with at least: type, date, amount.
- Aggregate cash flows from multiple products.
- Display cash flows in both a table and a bar chart.
- Keep the visualization easy to use and responsive in a Streamlit web UI.
- Support multiple currencies from the start.
- Make the framework extensible for future discounting and valuation calculations.

## 3. Core Concepts

### Cash Flow Object

A cash flow should be represented as a structured object or data record with fields such as:

- `product_id` or `product_name` (optional): identifies the product
- `type`: e.g. "payment", "principal", "interest", "fee", "income"
- `date`: date of the cash flow event
- `amount`: numeric value, positive or negative depending on direction
- `currency` (optional): currency code
- `description` (optional): short label or note

### Product Model

Each financial product should have a generator method or class that can produce a schedule of cash flows. Example features:

- Accept parameters such as notional, rate, term, frequency, start date
- Return a list of cash flow objects
- Support different product types such as loans, bonds, deposits, or custom cash flow schedules
- Possibly allow irregular or user-defined cash flow patterns
- Support multiple currencies from the start
- Work with generic cash flow schedules while allowing generator-based product templates
- Support adjustable day-count conventions and business-day adjustments per product

## 4. Functional Requirements

### 4.1 Cash Flow Generation

- Provide methods for creating cash flow schedules from input parameters
- Ensure cash flows are validated and sorted by date
- Support common cash flow types: principal repayment, interest payment, fees, and payouts
- Allow flexible output so cash flows can be combined across products

### 4.2 Aggregation and Portfolio Handling

- Enable adding multiple products to a portfolio
- Aggregate cash flows by date, type, or product
- Support portfolio-level views of total cash inflows and outflows
- Optionally support grouping by product, currency, or category

### 4.3 Visualization

- Provide a tabular view of cash flows showing key fields
- Provide a bar chart of cash flows by date or period
- Ensure the user interface is easy to read and responsive in Streamlit
- Allow filtering or selecting time ranges if useful

## 5. User Interaction and Workflow

- User defines one or more financial products via code or configuration
- Application generates cash flow schedules for each product
- User can view the combined cash flows in a table
- User can view the aggregated cash flows visually as a bar chart

## 6. Nonfunctional Requirements

- Implementation in Python
- Clean and extensible code structure
- Easy to extend with new product types and visualization options
- Prefer built-in or standard libraries for data handling, and common plotting libraries for charts
- Simple web UI built with Streamlit
- Support multiple currencies from the start

## 7. Future Enhancements

- Add support for real-time interactive filtering of cash flow visualization
- Support additional visualization types such as stacked bars or line charts
- Add import / export options for tables and charts (CSV, Excel, image)
- Add more detailed product metadata and scenario comparisons
- Add discounting of future cash flows using a zero coupon rate curve
- Add valuation support for PV under IRR scenarios

## 8. Clarifications and Design Decisions

- The system should work with generic cash flow schedules, while supporting pre-defined product templates through generator classes or helper functions.
- Multiple currencies should be supported from the start.
- Day-count conventions and business-day adjustments should be defined per product by default.

## 9. Open Questions

- What level of granularity should the product framework support next? (e.g. more advanced templates, custom schedule builders, or direct data imports)
- Do you want to support currency conversion and FX scenarios in the initial release or phase it in later?
