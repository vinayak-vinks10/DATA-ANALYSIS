from colorama import Fore,Style,init
import data_loader
import analasis
import visualization
import report

init(autoreset=True)
def menu():
    print("\n" + "="*50)
    print(Fore.YELLOW + Style.BRIGHT + "📊 SALES ANALYSIS REPORT".center(50))
    print("="*50)

    print(Fore.GREEN + Style.BRIGHT + "\nMAIN MENU\n")

    print(Fore.WHITE + "1️. Load Data")
    print(Fore.CYAN + "2️. Preview Data")
    print(Fore.CYAN + "3️. Revenue Analysis")
    print(Fore.CYAN + "4️. Product Analysis")
    print(Fore.CYAN + "5️. Customer Analysis")
    print(Fore.CYAN + "6️. Sales Trends")
    print(Fore.CYAN + "7️. Visualization")
    print(Fore.CYAN + "8️. Generate Report")
    
    print(Fore.RED + "9️. Exit")

    print("="*50 +"\n")
def main ():
    input("\nPress Enter to continue...")
    df=None
    while True:
        menu()
        try:
            choice = int(input("Choose option: "))
            
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choice == 9:
            print("Thank you for using the system")
            break
        
        elif choice == 1:
            df = data_loader.process_data("food_sales.csv")
            print("Data loaded and cleaned successfully")
        elif df is None and choice !=1:
           
            print("\n⚠️ Please load data first (Option 1).")
            continue
        
        elif choice == 2 :
             data_loader.data_preview(df)
        elif choice == 3:
             analasis.revenue_analysis(df)
        elif choice == 4:
             analasis.product_analysis(df)
        elif choice == 5:
             analasis.customer_analysis(df)
        elif choice == 6:
             visualization.sales_trend_chart(df)
        elif choice == 7:
             visualization.run_all_visuals(df)
        elif choice == 8:
            report.generate_report(df)
        else:
         
            print("\nInvalid choice\n")
        
        
