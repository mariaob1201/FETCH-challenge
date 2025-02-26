import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Box Plot from DataFrame
def box_plot(df, column, title="Box Plot", xlabel="Category", ylabel="Values"):
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, y=column)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Pie Chart from DataFrame
def pie_chart(df, column, title="Pie Chart"):
    sizes = df[column].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=sizes.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    plt.title(title)
    plt.show()

# Scatter Plot from DataFrame
def scatter_plot(df, x_column, y_column, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis"):
    plt.figure(figsize=(6, 4))
    plt.scatter(df[x_column], df[y_column], alpha=0.7, edgecolors="k")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Histogram from DataFrame
def histogram(df, column, bins=10, title="Histogram", xlabel="Values", ylabel="Frequency"):
    plt.figure(figsize=(6, 4))
    plt.hist(df[column], bins=bins, alpha=0.7, color="blue", edgecolor="black")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# T-Test from DataFrame
def t_test(df, column1, column2):
    t_stat, p_value = stats.ttest_ind(df[column1], df[column2], equal_var=False)
    print(f"T-statistic: {t_stat:.4f}, P-value: {p_value:.4f}")
    if p_value < 0.05:
        print("Result: Statistically significant difference (reject H0)")
    else:
        print("Result: No significant difference (fail to reject H0)")

# Example DataFrame
data = {
    'Category': np.random.choice(['A', 'B', 'C'], size=100),
    'Values': np.random.normal(50, 10, 100),
    'Group1': np.random.normal(50, 10, 100),
    'Group2': np.random.normal(55, 10, 100)
}
df = pd.DataFrame(data)

# Example usage
box_plot(df, 'Values', title="Example Box Plot")
pie_chart(df, 'Category', title="Example Pie Chart")
scatter_plot(df, 'Group1', 'Group2', title="Example Scatter Plot")
histogram(df, 'Values', bins=20, title="Example Histogram")
t_test(df, 'Group1', 'Group2')
