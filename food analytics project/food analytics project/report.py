import pandas as pd


def generate_report(df):
    with open("report.txt", "w") as f:
        f.write("="*40 + "\n")
        f.write("SALES REPORT\n")
        f.write("="*40 + "\n\n")

        # Revenue Analysis
        total_revenue = df['amount'].sum()
        avg_order = df['amount'].mean()
        total_orders = len(df)

        f.write("Revenue Analysis\n")
        f.write("-------------------------\n")
        f.write(f"Total Revenue: {total_revenue}\n")
        f.write(f"Average Order Value: {avg_order}\n")
        f.write(f"Total Orders: {total_orders}\n\n")

        # Product Analysis
        product_sales = df.groupby('product')['amount'].sum().sort_values(ascending=False)

        f.write("Product Analysis\n")
        f.write("-------------------------\n")
        f.write("Top 5 Products:\n")
        f.write(product_sales.head().to_string())
        f.write("\n\nLeast 5 Products:\n")
        f.write(product_sales.tail().to_string())
        f.write("\n\n")

        # Category Analysis
        temp_df = df.copy()
        temp_df['category'] = temp_df['category'].str.strip().str.title()
        category_sales = temp_df.groupby('category')['amount'].sum().sort_values(ascending=False)

        f.write("Category Analysis\n")
        f.write("-------------------------\n")
        f.write(category_sales.to_string())
        f.write("\n\n")

        # Customer Analysis
        total_customers = df['customer'].nunique()
        orders_per_customer = df['customer'].value_counts()

        f.write("Customer Analysis\n")
        f.write("-------------------------\n")
        f.write(f"Total Customers: {total_customers}\n")
        f.write("\nTop Customers:\n")
        f.write(orders_per_customer.head().to_string())
        f.write("\n\n")

        # Repeat Customers
        repeat_customers = orders_per_customer[orders_per_customer > 1].count()
        one_time_customers = orders_per_customer[orders_per_customer == 1].count()

        f.write("Customer Behavior\n")
        f.write("-------------------------\n")
        f.write(f"Repeat Customers: {repeat_customers}\n")
        f.write(f"One-time Customers: {one_time_customers}\n\n")

        # Monthly Sales
        temp_df = df.copy()
        temp_df['date'] = pd.to_datetime(temp_df['date'])
        temp_df['month'] = temp_df['date'].dt.month
        monthly_sales = temp_df.groupby('month')['amount'].sum()

        f.write("Monthly Sales\n")
        f.write("-------------------------\n")
        f.write(monthly_sales.to_string())
        f.write("\n\n")

        f.write("End of Report\n")

    print("\nReport generated successfully: report.txt")