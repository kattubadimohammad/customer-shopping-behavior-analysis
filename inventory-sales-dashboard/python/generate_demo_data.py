import numpy as np
import pandas as pd

np.random.seed(42)

categories = ["Beverages", "Snacks", "Personal Care", "Home Care", "Staples"]
products = {
    "Beverages": ["Tea", "Coffee", "Juice", "Soft Drinks"],
    "Snacks": ["Biscuits", "Chips", "Nuts", "Cookies"],
    "Personal Care": ["Shampoo", "Soap", "Toothpaste", "Skincare"],
    "Home Care": ["Detergent", "Cleaners", "Tissues", "Dishwash"],
    "Staples": ["Rice", "Flour", "Sugar", "Cooking Oil"],
}
locations = ["Bengaluru", "Hyderabad", "Chennai", "Mumbai", "Pune", "Delhi"]

rows = []
for _ in range(1200):
    category = np.random.choice(categories)
    demand = np.random.randint(30, 300)
    stock = np.random.randint(20, 500)
    filled = min(demand, stock + np.random.randint(10, 250))
    rows.append({
        "Category": category,
        "Product": np.random.choice(products[category]),
        "Location": np.random.choice(locations),
        "Sales": np.random.randint(500, 7000),
        "Closing Stock": stock,
        "PO Qty": np.random.randint(10, 250),
        "Demand": demand,
        "Filled Qty": filled,
    })

df = pd.DataFrame(rows)
df["Fill Rate"] = df["Filled Qty"] / df["Demand"] * 100
df["Instock"] = np.where(df["Closing Stock"] > 0, 1, 0)
df["Sell Through"] = df["Filled Qty"] / (df["Filled Qty"] + df["Closing Stock"]) * 100
df.to_csv("inventory_sales_demo.csv", index=False)
print("Created inventory_sales_demo.csv")
