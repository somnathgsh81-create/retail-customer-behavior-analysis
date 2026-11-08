# Retail Customer Behavior & Data Analytics Pipeline

An end-to-end data analytics pipeline designed to process, model, and analyse retail transactional data. This workflow handles initial raw data ingestion and structural cleaning in Python, deep analytical business querying in Microsoft SQL Server (MS SQL), and senior-level executive dashboard delivery via Power BI.

---

## Business Problem Statement

A leading retail company requires a data-driven understanding of its customer shopping behaviour to improve overall sales, elevate customer satisfaction, and drive long-term retention. 

Recent internal tracking indicated shifting purchasing patterns across customer demographics, product categories, and sales channels. Management requires a comprehensive diagnostic analysis to determine exactly how foundational factors—such as promotional discounts, review ratings, seasonal changes, and payment method preferences—influence customer decisions and repeat purchase frequencies. 

### Core Objective
Analyse the organization's transactional data to identify high-value consumer trends, optimise targeted marketing strategies, evaluate subscription plan structures, and provide executive stakeholders with clear product management recommendations.

---

## Project Structure & Deliverables

* **Data Engineering & Preparation (Python):** Handled missing data anomalies via targeted category-median imputation to eliminate metric bias, standardised headers into consistent snake case, and engineered numeric purchase frequency transformations.
* **Advanced Analytics Engine (MS SQL):** Configured a Microsoft SQL Server database instance to execute complex subqueries, common table expressions (CTEs), and specialised window functions (such as `ROW_NUMBER` partitioning) to segment loyalty cohorts and rank product groups.
* **Executive Visualisation Tool (Power BI):** Designed an interactive business reporting dashboard tracking core performance KPIs, demographic splits, and purchase conversion variables under dynamic metric filters.

---

## Technical Stack & Utilities
* **Languages:** Python (Pandas, NumPy, SQLAlchemy, pyodbc), SQL (T-SQL / MS SQL Server dialect)
* **Visualization Tools:** Power BI Desktop
* **Database Management:** Microsoft SQL Server / SQL Server Management Studio (SSMS)
