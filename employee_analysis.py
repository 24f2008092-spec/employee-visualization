# Email: 24f2008092@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\sharm\OneDrive\Desktop\employees.csv")

# Frequency count for Finance department
finance_count = (df["department"] == "Finance").sum()
print("Number of employees in Finance department:", finance_count)

# Histogram / count plot
sns.set_style("whitegrid")
plt.figure(figsize=(8,6))
sns.countplot(data=df, x="department")
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)

# Save image
plt.tight_layout()
plt.savefig("department_histogram.png")
print("Histogram saved as department_histogram.png")
