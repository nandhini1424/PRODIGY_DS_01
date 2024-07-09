import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('diabetes.csv')

print(df.head())


def plot_histograms(df, columns, n_rows, n_cols):
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 10))
    for i, col in enumerate(columns):
        ax = axes[i // n_cols, i % n_cols]
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f'Histogram of {col}')
    plt.tight_layout()
    plt.show()


def plot_bar_charts(df, columns, n_rows, n_cols):
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 10))
    for i, col in enumerate(columns):
        ax = axes[i // n_cols, i % n_cols]
        sns.countplot(x=col, data=df, ax=ax)
        ax.set_title(f'Bar chart of {col}')
    plt.tight_layout()
    plt.show()


numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
categorical_columns = df.select_dtypes(include=['object']).columns


plot_histograms(df, numerical_columns, n_rows=3, n_cols=3)


if len(categorical_columns) > 0:
    plot_bar_charts(df, categorical_columns, n_rows=1, n_cols=len(categorical_columns))
else:
    print("No categorical columns to plot.")
    
def plot_histograms(df, columns, n_rows, n_cols):
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 10))
    for i, col in enumerate(columns):
        ax = axes[i // n_cols, i % n_cols]
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f'Histogram of {col}')
    plt.tight_layout()
    plt.show()


def plot_bar_charts(df, columns, n_rows, n_cols):
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 10))
    for i, col in enumerate(columns):
        ax = axes[i // n_cols, i % n_cols]
        sns.countplot(x=col, data=df, ax=ax)
        ax.set_title(f'Bar chart of {col}')
    plt.tight_layout()
    plt.show()


numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
categorical_columns = df.select_dtypes(include=['object']).columns

plot_histograms(df, numerical_columns, n_rows=3, n_cols=3)

