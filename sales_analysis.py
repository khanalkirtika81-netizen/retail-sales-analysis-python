
import pandas as pd
import matplotlib.pyplot as plt

# Retail sales sample data
data = {
    "Product": ["Laptop", "Phone", "Monitor", "Notebook", "Chair"],
    "Category": ["Electronics", "Electronics", "Electronics", "Stationery", "Furniture"],
    "Quantity": [3, 6, 8, 50, 7],
    "Unit_Price": [750, 600, 250, 3, 120]
}

df = pd.DataFrame(data)

# Calculate revenue for each product
df["Revenue"] = df["Quantity"] * df["Unit_Price"]
df.to_csv("/Users/kirtikakhanal/Desktop/Project3_Python_Analysis/sales_analysis_results.csv", index=False)

# Display the analysis
print("RETAIL SALES ANALYSIS")
print(df)
print("\nTotal Revenue: $", df["Revenue"].sum())
print("\nRevenue by Category:")
print(df.groupby("Category")["Revenue"].sum())

# Create a chart
df.groupby("Category")["Revenue"].sum().plot(kind="bar")
plt.title("Revenue by Product Category")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("/Users/kirtikakhanal/Desktop/Project3_Python_Analysis/revenue_by_category.png")
plt.show()
