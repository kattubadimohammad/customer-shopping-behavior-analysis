import pandas as pd
from pathlib import Path

URL = "https://raw.githubusercontent.com/09shravan/Customer_Sales_Analysis_Behaviour/main/DATA%20ANALYSIS/shopping_behavior_updated.csv"
OUT = Path("powerbi")
OUT.mkdir(exist_ok=True)

df = pd.read_csv(URL)
print("Shape:", df.shape)
print("Exact duplicates:", df.duplicated().sum())
print("Missing values:\n", df.isna().sum())

# Standardize column names for analysis
rename = {c: c.strip().lower().replace(" ", "_").replace("(", "").replace(")", "") for c in df.columns}
df = df.rename(columns=rename)

# Basic cleaning
if "review_rating" in df.columns:
    df["review_rating"] = df["review_rating"].fillna(df.groupby("category")["review_rating"].transform("median"))
for c in df.select_dtypes(include="object").columns:
    df[c] = df[c].astype(str).str.strip()

def age_group(age):
    if age <= 24: return "18-24"
    if age <= 34: return "25-34"
    if age <= 44: return "35-44"
    if age <= 54: return "45-54"
    return "55+"

df["age_group"] = df["age"].apply(age_group)
df.to_csv(OUT / "customer_shopping_behavior_powerbi.csv", index=False)

df.groupby("category", as_index=False)["purchase_amount_usd"].agg(["sum", "count", "mean"]).reset_index().to_csv(OUT / "category_summary.csv", index=False)
df.groupby("age_group", as_index=False)["purchase_amount_usd"].agg(["sum", "count", "mean"]).reset_index().to_csv(OUT / "age_summary.csv", index=False)
df.groupby("location", as_index=False)["purchase_amount_usd"].agg(["sum", "count", "mean"]).reset_index().sort_values("sum", ascending=False).to_csv(OUT / "location_summary.csv", index=False)

kpis = pd.DataFrame({"metric": ["Total Sales", "Transactions", "Average Purchase", "Average Rating"], "value": [df.purchase_amount_usd.sum(), len(df), df.purchase_amount_usd.mean(), df.review_rating.mean()]})
kpis.to_csv(OUT / "kpi_summary.csv", index=False)
print(kpis)
