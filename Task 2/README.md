# Superstore Data Analysis & Visualization

A comprehensive data visualization project built around a sample Superstore dataset. This project demonstrates end-to-end data analysis, from data cleaning to interactive dashboard creation.

## 📊 Project Overview

This project analyzes Superstore sales data to uncover business insights, trends, and performance metrics. The analysis includes data preprocessing, exploratory data analysis, visualization, and provides foundations for building interactive dashboards in Power BI or Tableau.

## 🎯 Objectives

- Perform comprehensive data cleaning and preprocessing
- Generate insightful visualizations and charts
- Identify key sales trends and performance metrics
- Create foundation for interactive business intelligence dashboards
- Provide actionable insights for business decision-making

## 📁 Project Structure

```
Task 2/
│
├── data/
│   ├── Superstore_sample.csv          # Original sample dataset
│   └── Superstore_cleaned.csv         # Processed and cleaned data
│
├── notebooks/
│   └── analysis_notebook.ipynb        # Jupyter notebook with exploratory analysis
│
├── outputs/
│   ├── charts/
│   │   ├── sales_profit_over_time.png      # Time series analysis
│   │   ├── sales_by_region.png             # Regional performance
│   │   ├── profit_margin_by_category.png   # Category profitability
│   │   ├── discount_vs_profit.png          # Discount impact analysis
│   │   └── top10_products_profit.png       # Top performing products
│   │
│   └── storyboard.pdf                 # Dashboard design and storyboard
│
├── src/
│   └── analysis.py                    # Main Python analysis script
│
├── README.md                          # Project documentation
├── analysis_notes.md                  # Technical notes and methodology
├── interview_questions_answers.md     # Q&A about the analysis
└── LICENSE                           # Project license
```

## 🛠️ Technologies Used

- **Python 3.8+**
- **Libraries:** Pandas, Matplotlib, Pillow (PIL)
- **BI Tools:** Power BI / Tableau (for dashboard creation)
- **Data Format:** CSV

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/themanishpndt/Elevate-Labs---Data-Analyst.git
cd "Elevate-Labs---Data-Analyst/Task 2"
```

2. **Install dependencies**
```bash
pip install pandas matplotlib pillow
```

3. **Run the analysis**
```bash
python src/analysis.py
```

## 📈 Outputs Generated

After running the analysis script, the following outputs will be created:

### Data Outputs
- `data/Superstore_cleaned.csv` - Processed and cleaned dataset ready for analysis

### Visualization Outputs
- `outputs/charts/` - Folder containing various charts including:
  - Sales trends over time
  - Regional performance comparisons
  - Product category analysis
  - Customer segment insights
  - Profitability analysis

## 📊 Dashboard Creation

### Power BI Instructions
1. Open Power BI Desktop
2. Import `data/Superstore_cleaned.csv` as your data source
3. Use the generated charts as reference for your dashboard design
4. Create interactive filters for date range, region, category, etc.
5. Publish to Power BI Service for sharing

### Tableau Instructions
1. Open Tableau Desktop
2. Connect to `data/Superstore_cleaned.csv`
3. Build worksheets based on the Python-generated charts
4. Combine worksheets into an interactive dashboard
5. Add filters and actions for enhanced interactivity

## 🔧 Customization

### Using Full Dataset
Replace `data/Superstore_sample.csv` with the complete `Superstore.csv` file and re-run the analysis script:

```bash
python src/analysis.py
```

### Modifying Analysis
Edit `src/analysis.py` to:
- Add new visualizations
- Change chart styles and colors
- Include additional metrics
- Modify data preprocessing steps

## 📋 Key Analysis Areas

The project analyzes:
- **Sales Performance**: Monthly/quarterly sales trends
- **Regional Analysis**: Geographic performance comparisons
- **Product Insights**: Category and sub-category performance
- **Customer Segmentation**: B2B vs B2C analysis
- **Profitability**: Profit margins and cost analysis
- **Shipping Analysis**: Mode efficiency and costs

## 🎨 Sample Visualizations

The analysis generates several key visualizations:

- **Sales Trend Analysis**: Line charts showing sales performance over time
- **Regional Performance**: Bar charts comparing sales across regions
- **Category Breakdown**: Pie charts showing product category distribution
- **Profitability Heatmaps**: Correlation analysis between different metrics

## 🤝 Contributing

This project was created as part of the Elevate Labs Data Analyst assessment. For suggestions or improvements, please feel free to open an issue or submit a pull request.

## 📧 Contact

- **Manish Sharma** 
- **GitHub:** [@themanishpndt](https://github.com/themanishpndt)
- **Project Link:** [https://github.com/themanishpndt/Elevate-Labs---Data-Analyst/Task%202](https://github.com/themanishpndt/Elevate-Labs---Data-Analyst/tree/main/Task%202)

## 📄 License

This project is created for educational and assessment purposes as part of the Elevate Labs Data Analyst application process.

---
