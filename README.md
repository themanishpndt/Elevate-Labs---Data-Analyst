# 📊 Data Analyst Internship - Task 1: Data Cleaning & Preprocessing

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
├── raw_dataset.csv              # Original noisy dataset with issues (300 records)
├── cleaned_dataset.csv          # Final cleaned dataset ready for analysis (255 records)
├── task1_cleaning.py            # Python script for automated cleaning pipeline
├── task1_cleaning.ipynb         # Jupyter Notebook (step-by-step explanation + profiling)
├── report.md                    # Detailed cleaning metrics and results
├── data_dictionary.md           # Comprehensive field descriptions
├── requirements.txt             # Python dependencies
├── Images/                      # Charts & visualizations of data before/after cleaning
│   ├── age_hist_raw.png
│   ├── age_hist_cleaned.png
│   ├── income_boxplot_raw.png
│   ├── income_boxplot_cleaned.png
│   ├── gender_counts_raw.png
│   └── gender_counts_cleaned.png
├── LICENSE                      # Open-source license (MIT)
└── README.md                    # Project documentation (this file)
```

---

## 🛠 Tools & Technologies Used
- **Python 3.x** – Data cleaning and preprocessing
- **Pandas** – Data handling and transformations
- **NumPy** – Numerical computations
- **Matplotlib/Seaborn** – Data visualization (before/after comparisons)
- **Jupyter Notebook** – Interactive analysis and documentation

---

## 📊 Dataset Information
**Source**: Customer Segmentation Dataset (Mall Customer Data style)

### Dataset Columns Handled:
- **CustomerID** - Unique customer identifier
- **Gender** - Customer gender (with inconsistencies)
- **Age** - Customer age (missing values and outliers)
- **Annual Income (k$)** - Income with various formats and symbols
- **Spending Score (1-100)** - Customer spending metric
- **JoinDate** - Multiple date formats
- **Country** - Inconsistent country naming
- **Email** - Validation and cleaning
- **PurchaseCount** - Transaction history
- **LastPurchaseDate** - Date standardization
- **Churn** - Customer retention status

---

## 🧹 Data Cleaning Steps Performed

### 1. **Handling Missing Values**
- Identified using `.isnull().sum()`
- Filled `Age` with **median**, `Annual Income` with **mean**, `Spending Score` with **median**
- Missing `JoinDate` and `LastPurchaseDate` were filled with the **mode or logical replacements**
- **Categorical columns**: Filled with mode (Gender, Country)
- **Email validation**: Separate flag for invalid emails

### 2. **Removing Duplicates**
- Removed using `.drop_duplicates()`
- Removed 45 exact duplicate records
- Ensured unique records per `CustomerID`
- Maintained data integrity while eliminating redundancy

### 3. **Standardizing Text Data**
- **Gender** standardized → `Male`, `Female`, `Unknown`
- **Country** standardized → e.g., `"usa"`, `"U.S.A"`, `"us"` → `United States`
- **Email** validated for proper format (`@` and domain)
- **Column Headers**: Converted to snake_case format
- **Text Data**: Stripped whitespace and standardized casing

### 4. **Fixing Data Types**
- Converted `Age` to **integer**
- Converted `JoinDate` and `LastPurchaseDate` to **datetime**
- Converted categorical fields (`Gender`, `Churn`) to consistent formats
- `Annual Income` → Float with currency symbol removal
- `Spending Score` → Integer with range validation

### 5. **Outlier Treatment**
- Identified outliers using **IQR method** on `Annual Income` and other numerical columns
- Applied **capping** to reduce the influence of extreme values
- Treated invalid entries (negative ages, unrealistic values)
- Age range constrained to realistic values (10-100)

### 6. **Column Name Standardization**
- Converted to **lowercase**
- Replaced spaces & special characters with underscores (`annual_income_k`)
- Ensured consistent naming convention throughout dataset

### 7. **Data Validation & Business Logic**
- **Email format validation** with proper checking
- **Date consistency validation** (last purchase ≥ join date)
- **Churn flag standardization** (Y/Yes/True/1 → 1, others → 0)

---

## 📊 Results & Performance Metrics

### **Data Quality Before Cleaning:**
- **Total Records**: 300
- **Missing Values**: 47 entries across columns
- **Duplicate Records**: 45
- **Inconsistent Formats**: 89 entries
- **Data Quality Score**: 68%

### **Data Quality After Cleaning:**
- **Total Records**: 255 (clean, unique records)
- **Missing Values**: 0 (completely resolved)
- **Duplicate Records**: 0 (100% removed)
- **Consistent Formats**: 100% achieved
- **Data Quality Score**: 98%

### **Key Improvements Achieved:**
1. **100% Data Integrity** - No missing values or duplicates
2. **Format Consistency** - Uniform data formats across all columns
3. **Business Readiness** - Dataset ready for analysis and modeling
4. **Automated Pipeline** - Reproducible cleaning process

---

## 📸 Visual Insights (Before vs After Cleaning)
- **Age Distribution**: Unrealistic values (e.g., 5, 150) replaced with valid ages
- **Annual Income**: Outliers capped, missing values filled
- **Gender Counts**: Standardized across multiple inconsistent labels
- **Country Field**: Normalized to consistent country names

*All visuals are available in the `/Images` folder*

---

## 🚀 How to Run This Project

### **Prerequisites**
- Python 3.7+
- pip package manager

### **Installation & Execution**

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

### **Quick Start Alternative**
1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Run the cleaning pipeline**:
```bash
python task1_cleaning.py
```

3. **Explore the results**:
- Check `cleaned_dataset.csv` for the final cleaned data
- Review `report.md` for detailed cleaning metrics
- View `Images/` folder for visual comparisons

---

## 📜 Deliverables
- ✅ `raw_dataset.csv` → original messy dataset (300 records)
- ✅ `cleaned_dataset.csv` → final processed dataset (255 records)
- ✅ `task1_cleaning.py` → reproducible cleaning pipeline
- ✅ `task1_cleaning.ipynb` → notebook with explanation + profiling
- ✅ `report.md` → summary of issues and fixes
- ✅ `data_dictionary.md` → detailed field descriptions
- ✅ Visual comparisons → before/after cleaning in Images folder

---

## 📘 Interview Prep Questions (with Answers)

### 1. **What are missing values and how do you handle them?**
**Answer**: Missing values are blanks or nulls in a dataset. They can be handled by:
- Removing rows/columns with `dropna()`
- Filling with statistical measures using `fillna()` (mean/median/mode)
- Predictive imputation for advanced cases

### 2. **How do you treat duplicate records?**
**Answer**: Use `.drop_duplicates()` in Pandas or "Remove Duplicates" in Excel. Keep the first occurrence unless business logic requires specific handling.

### 3. **Difference between `dropna()` and `fillna()`?**
**Answer**: 
- `dropna()` removes rows/columns with missing values
- `fillna()` replaces missing values with specified values (mean, median, mode, or custom)

### 4. **What is outlier treatment and why is it important?**
**Answer**: Outliers are extreme values that don't follow the data pattern. Treatment is important because outliers can skew statistical analyses and machine learning models. Common methods include capping, transformation, or removal.

### 5. **Explain the process of standardizing data**
**Answer**: Standardization involves making data consistent across the dataset:
- Text normalization (lowercase/uppercase)
- Category standardization (Male/M → Male)
- Date format consistency
- Unit standardization

### 6. **How do you handle inconsistent data formats (e.g., dates)?**
**Answer**: Use `pd.to_datetime()` in Python with appropriate format specifications, or use Excel's "Format Cells" feature to standardize date formats.

### 7. **What are common data cleaning challenges?**
**Answer**: 
- Missing data handling decisions
- Duplicate identification and removal
- Inconsistent category labels
- Outlier detection and treatment
- Data type conversions
- Text cleaning and standardization

### 8. **How do you check data quality?**
**Answer**: 
- Summary statistics (`.describe()`)
- Missing value analysis (`.isnull().sum()`)
- Unique value counts (`.nunique()`)
- Data type validation (`.dtypes`)
- Data profiling and validation rules

---

## 💡 Key Learnings
- **Hands-on practice** in data cleaning and preprocessing
- **Advanced Pandas** data manipulation techniques
- **Comprehensive data quality assessment** methods
- **Automated data cleaning pipeline** development
- **Statistical methods** for missing value imputation
- **Business logic implementation** for data validation

---

## 📈 Next Steps
The cleaned dataset is now ready for:
- **Exploratory Data Analysis (EDA)**
- **Customer Segmentation Analysis**
- **Predictive Modeling**
- **Business Intelligence Dashboards**

---

## 📄 License
This project is licensed under the MIT License - feel free to use, modify, and share.

---

## 👥 Author & Contributing

### **Author**
**Manish Sharma**  
Data Analyst Intern Candidate  
Elevate Labs Solutions  
manishsharma93155@gmail.com

### **Contributing**
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🎯 Interview Preparation
This project demonstrates practical skills in handling real-world data challenges, preparing you for technical interviews focusing on data cleaning, preprocessing, and quality assurance.

**🚀 Ready for Analysis!** - The dataset is now clean, validated, and prepared for advanced analytical tasks.

---

## 📞 Contact
manishsharma93155@gmail.com
