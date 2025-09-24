"""
task1_cleaning.py - robust script to clean raw_dataset.csv and save cleaned_dataset.csv
"""
import pandas as pd, numpy as np
def normalize_col(col):
    s = col.strip().lower()
    s = s.replace(" ", "_").replace("(", "").replace(")", "").replace("$","").replace("%","").replace(",","").replace("-","_")
    while "__" in s: s = s.replace("__","_")
    s = s.strip("_")
    return s
def clean_income(x):
    if pd.isnull(x): return np.nan
    s = str(x).strip().lower().replace("$","").replace("k","").replace(",","")
    if s in ["n/a","na","none",""]: return np.nan
    try: return float(s)
    except: return np.nan
def standardize_gender(x):
    if pd.isnull(x): return np.nan
    s = str(x).strip().lower()
    if s in ["m","male"]: return "Male"
    if s in ["f","female"]: return "Female"
    return "Unknown"
def validate_email(x):
    if pd.isnull(x): return (np.nan, False)
    s = str(x).strip().lower()
    if "@" not in s or s.count("@")>1: return (s, False)
    local, domain = s.split("@",1)
    if "." not in domain: return (s, False)
    return (s, True)
def clean_churn(x):
    if pd.isnull(x): return 0
    return 1 if str(x).strip().lower() in ["y","yes","true","1","1.0"] else 0
def main():
    raw = pd.read_csv("raw_dataset.csv")
    raw.columns = [normalize_col(c) for c in raw.columns]
    df = raw.drop_duplicates().copy()
    df['gender'] = df['gender'].apply(standardize_gender)
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df.loc[(df['age']<10)|(df['age']>100), 'age'] = np.nan
    df['age'] = int(df['age'].median(skipna=True))
    income_cols = [c for c in df.columns if 'annual' in c and 'income' in c]
    if income_cols:
        df['annual_income_k'] = df[income_cols[0]].apply(clean_income)
    else:
        df['annual_income_k'] = np.nan
    df['annual_income_k'] = df['annual_income_k'].fillna(df['annual_income_k'].mean())
    spend_cols = [c for c in df.columns if 'spending' in c]
    if spend_cols:
        df['spending_score_1_100'] = pd.to_numeric(df[spend_cols[0]], errors='coerce')
    else:
        df['spending_score_1_100'] = np.nan
    df['spending_score_1_100'] = df['spending_score_1_100'].fillna(int(df['spending_score_1_100'].median()))
    join_cols = [c for c in df.columns if 'join' in c]
    if join_cols:
        df['joindate'] = pd.to_datetime(df[join_cols[0]], errors='coerce')
    else:
        df['joindate'] = pd.NaT
    last_cols = [c for c in df.columns if 'last' in c and 'purchase' in c]
    if last_cols:
        df['lastpurchasedate'] = pd.to_datetime(df[last_cols[0]], errors='coerce')
    else:
        df['lastpurchasedate'] = pd.NaT
    df['lastpurchasedate'] = df['lastpurchasedate'].fillna(df['joindate'])
    country_cols = [c for c in df.columns if 'country' in c]
    if country_cols:
        df['country'] = df[country_cols[0]].apply(lambda x: x.strip().title() if pd.notnull(x) else x)
    else:
        df['country'] = np.nan
    email_cols = [c for c in df.columns if 'email' in c]
    if email_cols:
        emails = df[email_cols[0]].apply(validate_email)
        df['email_clean'] = emails.apply(lambda t: t[0])
        df['email_valid'] = emails.apply(lambda t: t[1])
    else:
        df['email_clean'] = np.nan; df['email_valid'] = False
    df['purchasecount'] = pd.to_numeric(df['purchasecount'], errors='coerce').fillna(0).astype(int)
    churn_cols = [c for c in df.columns if 'churn' in c]
    if churn_cols:
        df['churn_flag'] = df[churn_cols[0]].apply(clean_churn).astype(int)
    else:
        df['churn_flag'] = 0
    Q1 = df['annual_income_k'].quantile(0.25)
    Q3 = df['annual_income_k'].quantile(0.75)
    IQR = Q3 - Q1
    if IQR==0:
        lower, upper = df['annual_income_k'].min(), df['annual_income_k'].max()
    else:
        lower, upper = Q1-1.5*IQR, Q3+1.5*IQR
    df['annual_income_k_capped'] = df['annual_income_k'].clip(lower=lower, upper=upper)
    final_cols = ['customerid','gender','age','annual_income_k','annual_income_k_capped','spending_score_1_100','joindate','lastpurchasedate','country','email_clean','email_valid','purchasecount','churn_flag']
    for c in final_cols:
        if c not in df.columns:
            df[c] = np.nan
    final = df[final_cols].copy()
    final['joindate_clean'] = final['joindate'].dt.strftime('%d-%m-%Y')
    final['lastpurchasedate_clean'] = final['lastpurchasedate'].dt.strftime('%d-%m-%Y')
    final.to_csv('cleaned_dataset.csv', index=False)
    print('cleaned_dataset.csv generated.')
if __name__ == '__main__':
    main()
