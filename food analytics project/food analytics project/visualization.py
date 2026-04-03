import pandas as pd
import matplotlib.pyplot as plt


def top_products_chart(df):
    print("\nTop Products Chart")
    print("-----------------")

    product_sales = df.groupby('product')['amount'].sum().sort_values(ascending=False).head(5)

    product_sales.plot(kind='bar')
    plt.title("Top 5 Products")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def sales_trend_chart(df):
    print("\nSales Trend Chart")
    print("-----------------")

    temp_df = df.copy()  # safe copy

    temp_df['date'] = pd.to_datetime(temp_df['date'])
    daily_sales = temp_df.groupby('date')['amount'].sum()

    daily_sales.plot()
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()





def run_all_visuals(df):
    top_products_chart(df)
    sales_trend_chart(df)
   