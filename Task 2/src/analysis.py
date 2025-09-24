# analysis.py - Lightweight version for the sample dataset included with this project.
import pandas as pd, numpy as np, matplotlib.pyplot as plt, os
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / 'data'
OUT_DIR = ROOT / 'outputs' / 'charts'
OUT_DIR.mkdir(parents=True, exist_ok=True)
RAW = DATA_DIR / 'Superstore_sample.csv'
CLEAN = DATA_DIR / 'Superstore_cleaned.csv'
print('Loading', RAW)
df = pd.read_csv(RAW, low_memory=False)
# Standardize column names
df.columns = [c.strip().replace(' ','_') for c in df.columns]
# Parse dates
for col in ['Order_Date','Ship_Date']:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
# Numeric conversions
for col in ['Sales','Profit','Discount','Quantity']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
# Drop essential missing
essentials = [c for c in ['Order_ID','Order_Date','Sales','Profit'] if c in df.columns]
df = df.dropna(subset=essentials)
df = df.drop_duplicates()
# Shipping days
if 'Order_Date' in df.columns and 'Ship_Date' in df.columns:
    df['Shipping_Days'] = (df['Ship_Date'] - df['Order_Date']).dt.days
# Derived fields
df['Profit_Margin'] = df.apply(lambda r: r['Profit']/r['Sales'] if r.get('Sales') and r['Sales'] != 0 else np.nan, axis=1)
if 'Order_Date' in df.columns:
    df['Order_Year'] = df['Order_Date'].dt.year
    df['Order_Month'] = df['Order_Date'].dt.month
    df['Order_Month_Name'] = df['Order_Date'].dt.strftime('%b')
    df['Order_Quarter'] = df['Order_Date'].dt.to_period('Q')
# Save cleaned CSV
df.to_csv(CLEAN, index=False)
print('Saved cleaned CSV to', CLEAN)
# Create charts
# 1. Sales & Profit over time (monthly)
if 'Order_Date' in df.columns:
    ts = df.set_index('Order_Date').resample('M').sum()[['Sales','Profit']]
    plt.figure(figsize=(10,5))
    plt.plot(ts.index, ts['Sales'], marker='o', label='Sales')
    plt.plot(ts.index, ts['Profit'], marker='o', label='Profit')
    plt.title('Sales and Profit Over Time (Monthly)')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'sales_profit_over_time.png')
    plt.close()
# 2. Sales by Region
if 'Region' in df.columns:
    region_sales = df.groupby('Region').agg(Sales=('Sales','sum')).reset_index()
    plt.figure(figsize=(8,5))
    plt.bar(region_sales['Region'], region_sales['Sales'])
    plt.title('Sales by Region')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'sales_by_region.png')
    plt.close()
# 3. Profit margin by category
if 'Category' in df.columns:
    cat = df.groupby('Category').agg(Sales=('Sales','sum'), Profit=('Profit','sum'))
    cat['Profit_Margin'] = cat['Profit']/cat['Sales']
    cat = cat.reset_index()
    plt.figure(figsize=(8,5))
    plt.bar(cat['Category'], cat['Profit_Margin'])
    plt.title('Profit Margin by Category')
    plt.ylabel('Profit Margin')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'profit_margin_by_category.png')
    plt.close()
# 4. Top products by profit
if 'Product_Name' in df.columns:
    top = df.groupby('Product_Name').agg(Profit=('Profit','sum')).sort_values('Profit', ascending=False).head(10)
    plt.figure(figsize=(10,6))
    plt.barh(top.index[::-1], top['Profit'][::-1])
    plt.title('Top 10 Products by Profit')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'top10_products_profit.png')
    plt.close()
# 5. Discount vs Profit scatter
if 'Discount' in df.columns:
    plt.figure(figsize=(8,6))
    plt.scatter(df['Discount'], df['Profit'], alpha=0.7)
    plt.xlabel('Discount')
    plt.ylabel('Profit')
    plt.title('Discount vs Profit')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'discount_vs_profit.png')
    plt.close()
print('Charts saved to', OUT_DIR)
