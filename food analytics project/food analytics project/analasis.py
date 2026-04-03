import pandas as pd

# df = pd.read_csv("cleaned_dataset.csv")

def revenue_analysis(df):
    print("\nRevenue Analysis")
    print("-----------------")

    total_revenue = df['amount'].sum()
    avg_order = df['amount'].mean()
    total_orders = len(df)

    print("Total revenue:", total_revenue)
    print("Average order value:", avg_order)
    print("Total orders:", total_orders)


def product_analysis(df):
    print("\nProduct Analysis")
    print("-----------------")

    product_sales = df.groupby('product')['amount'].sum().sort_values(ascending=False)

    print("Top 5 products:")
    print(product_sales.head().to_string())

    print("\nLeast 5 products:")
    print(product_sales.tail().to_string())


def category_analysis(df):
    print("\nCategory Analysis")
    print("-----------------")

    df['category'] = df['category'].str.strip().str.title()

    category_sales = df.groupby('category')['amount'].sum().sort_values(ascending=False)

    print(category_sales.to_string())


def customer_analysis(df):
    print("\nCustomer Analysis")
    print("-----------------")

    total_customers = df['customer'].nunique()
    orders_per_customer = df['customer'].value_counts()

    print("Total customers:", total_customers)

    print("\nTop customers:")
    print(orders_per_customer.head().to_string())


def repeat_customer_analysis(df):
    print("\nRepeat Customer Analysis")
    print("-----------------")

    orders_per_customer = df['customer'].value_counts()

    repeat_customers = orders_per_customer[orders_per_customer > 1].count()
    one_time_customers = orders_per_customer[orders_per_customer == 1].count()

    print("Repeat customers:", repeat_customers)
    print("One-time customers:", one_time_customers)


def monthly_sales_analysis(df):
    print("\nMonthly Sales Analysis")
    print("-----------------")

    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month

    monthly_sales = df.groupby('month')['amount'].sum()

    print(monthly_sales.to_string())


# def run_all(df):
#     revenue_analysis(df)
#     product_analysis(df)
#     category_analysis(df)
#     customer_analysis(df)
#     repeat_customer_analysis(df)
#     monthly_sales_analysis(df)