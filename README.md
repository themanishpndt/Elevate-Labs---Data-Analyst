
# 📊 Task 1 - Data Cleaning & Preprocessing (Elevate Labs Internship)

## 🎯 Objective
The goal of this task is to **clean and preprocess a raw dataset** containing common real-world issues such as:
- Missing values
- Duplicate records
- Inconsistent formatting (text, dates, numeric values)
- Outliers and extreme values
- Invalid data entries (e.g., malformed emails, unrealistic ages)

This ensures the dataset is **accurate, consistent, and ready for analysis or modeling**.

---

## 📂 Repository Structure
```
DataAnalyst_Task1_ElevateLabs/
│── raw_dataset.csv              # Original noisy dataset with issues
│── cleaned_dataset.csv           # Final cleaned dataset ready for analysis
│── task1_cleaning.py            # Python script to reproduce the cleaning process
│── task1_cleaning.ipynb         # Jupyter Notebook (step-by-step explanation)
│── report.md                    # Deep dive report (before vs after cleaning)
│── data_dictionary.md           # Explanation of each field/column
│── requirements.txt             # Python dependencies
│── images/                      # Charts & visualizations of data before/after cleaning
│   ├── age_hist_raw.png
│   ├── age_hist_cleaned.png
│   ├── income_boxplot_raw.png
│   ├── income_boxplot_cleaned.png
│   ├── gender_counts_raw.png
│   └── gender_counts_cleaned.png
│── README.md                    # Project documentation (this file)
│── LICENSE                      # Open-source license (MIT)
│── .gitignore                   # Git ignore file
```

---

## 🛠 Tools & Libraries Used
- **Python** – Data cleaning and preprocessing  
- **Pandas** – Data handling and transformations  
- **NumPy** – Numerical computations  
- **Matplotlib** – Data visualization (before/after comparisons)  
- **Jupyter Notebook** – Documentation and step-by-step cleaning process  

---

## 🧹 Data Cleaning Steps Performed

### 1. Handling Missing Values
- Identified using `.isnull().sum()`
- Filled `Age` with **median**, `Annual Income` with **mean**, `Spending Score` with **median**
- Missing `JoinDate` and `LastPurchaseDate` were filled with the **mode or logical replacements**

### 2. Removing Duplicates
- Removed using `.drop_duplicates()`
- Ensured unique records per `CustomerID`

### 3. Standardizing Text Data
- **Gender** standardized → `Male`, `Female`, `Unknown`
- **Country** standardized → e.g., `"usa"`, `"U.S.A"`, `"us"` → `United States`
- **Email** validated for proper format (`@` and domain)

### 4. Fixing Data Types
- Converted `Age` to **integer**
- Converted `JoinDate` and `LastPurchaseDate` to **datetime**
- Converted categorical fields (`Gender`, `Churn`) to consistent formats

### 5. Outlier Treatment
- Identified outliers using **IQR method** on `Annual Income`
- Applied **capping** to reduce the influence of extreme values

### 6. Column Name Standardization
- Converted to **lowercase**
- Replaced spaces & special characters with underscores (`annual_income_k`)

---

## 📊 Visual Insights (Before vs After Cleaning)

- **Age Distribution**: Unrealistic values (e.g., 5, 150) replaced with valid ages
- **Annual Income**: Outliers capped, missing values filled
- **Gender Counts**: Standardized across multiple inconsistent labels
- **Country Field**: Normalized to consistent country names

*All visuals are available under the `/images` folder*

---

## 📜 Deliverables
- ✅ `raw_dataset.csv` → original messy dataset
- ✅ `cleaned_dataset.csv` → final processed dataset
- ✅ `task1_cleaning.py` → reproducible cleaning pipeline
- ✅ `task1_cleaning.ipynb` → notebook with explanation + profiling
- ✅ `report.md` → summary of issues and fixes
- ✅ `data_dictionary.md` → detailed field descriptions

---

## 📘 Interview Prep Questions (with Answers)

### 1. What are missing values and how do you handle them?
**Answer**: Missing values are blanks or nulls in a dataset. They can be handled by:
- Removing rows/columns with `dropna()`
- Filling with statistical measures using `fillna()` (mean/median/mode)
- Predictive imputation for advanced cases

### 2. How do you treat duplicate records?
**Answer**: Use `.drop_duplicates()` in Pandas or "Remove Duplicates" in Excel. Keep the first occurrence unless business logic requires specific handling.

### 3. Difference between `dropna()` and `fillna()`?
**Answer**: 
- `dropna()` removes rows/columns with missing values
- `fillna()` replaces missing values with specified values (mean, median, mode, or custom)

### 4. What is outlier treatment and why is it important?
**Answer**: Outliers are extreme values that don't follow the data pattern. Treatment is important because outliers can skew statistical analyses and machine learning models. Common methods include capping, transformation, or removal.

### 5. Explain the process of standardizing data
**Answer**: Standardization involves making data consistent across the dataset:
- Text normalization (lowercase/uppercase)
- Category standardization (Male/M → Male)
- Date format consistency
- Unit standardization

### 6. How do you handle inconsistent data formats (e.g., dates)?
**Answer**: Use `pd.to_datetime()` in Python with appropriate format specifications, or use Excel's "Format Cells" feature to standardize date formats.

### 7. What are common data cleaning challenges?
**Answer**: 
- Missing data handling decisions
- Duplicate identification and removal
- Inconsistent category labels
- Outlier detection and treatment
- Data type conversions
- Text cleaning and standardization

### 8. How do you check data quality?
**Answer**: 
- Summary statistics (`.describe()`)
- Missing value analysis (`.isnull().sum()`)
- Unique value counts (`.nunique()`)
- Data type validation (`.dtypes`)
- Data profiling and validation rules

---

## 🚀 How to Run This Project

### Prerequisites
- Python 3.7+
- pip package manager

### Installation & Execution

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/DataAnalyst_Task1_ElevateLabs.git
cd DataAnalyst_Task1_ElevateLabs
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the cleaning script**:
```bash
python task1_cleaning.py
```
*This will generate `cleaned_dataset.csv`*

4. **Explore the notebook**:
```bash
jupyter notebook task1_cleaning.ipynb
```

---

## 📌 Key Learnings
- Hands-on practice in data cleaning and preprocessing
- Improved skills in Pandas & data manipulation
- Deeper understanding of real-world data issues
- Experience with complete data cleaning pipeline
- Produced a dataset ready for analysis, visualization, or modeling

---

## 🔄 Next Steps
- Perform exploratory data analysis (EDA) on the cleaned dataset
- Create data visualizations and dashboards
- Build predictive models using the cleaned data
- Implement data validation checks for future data ingestion

---

## 📄 License
This project is licensed under the MIT License - feel free to use, modify, and share.

---

## 👥 Contributing
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📞 Contact
manishsharma93155@gmail.com
---
