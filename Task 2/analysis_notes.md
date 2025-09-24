
# Analysis Notes

This document explains the steps taken in `src/analysis.py` and guidance for expanding the analysis.

## 1. Data cleaning
- Standardized column names.
- Parsed date columns (`Order_Date`, `Ship_Date`).
- Converted numeric columns: Sales, Profit, Discount, Quantity.
- Calculated Shipping_Days and Profit_Margin.

## 2. Feature engineering
- Profit_Margin = Profit / Sales
- Order_Year, Order_Month, Order_Quarter derived from Order_Date.

## 3. Charts produced
- Sales and Profit over time (monthly)
- Sales by Region
- Profit Margin by Category
- Top 10 Products by Profit
- Discount vs Profit scatter

## 4. Next steps
- Create RFM features for customer segmentation.
- Build cohort analysis for retention.
- Create interactive dashboard in Power BI/Tableau.
