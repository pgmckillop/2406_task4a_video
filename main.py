import pandas as pd
from matplotlib import pyplot as plt


# Outputs the initial menu and checks validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Recoats Adventure Park ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total income by source")
        print("### 2. Income by payment type and source")
        print("### 3. Total income by day")
        print("### 4. Exit")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            print('Choice accepted!')
            flag = False

    return choice


# Submenu for totals, provides type check validation for the input
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total income by source ##############")
        print("####################################################")
        print("")
        print("########## Please select an income source ##########")
        print("### 1. Tickets")
        print("### 2. Gift Shop")
        print("### 3. Snack Stand")
        print("### 4. Pictures")

        choice = input('Enter your number selction here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            print('Choice accepted!')
            flag = False

    return choice


# takes the total submenu input and converts the number to a string of the source name
def convert_total_men_coice(total_men_choice):
    if total_men_choice == "1":
        tot_choice = "Tickets"
    elif total_men_choice == "2":
        tot_choice = "Gift Shop"
    elif total_men_choice == "3":
        tot_choice = "Snack Stand"
    else:
        tot_choice = "Pictures"

    return tot_choice

# Utility function to load the data from the CSV file
def load_data():
    # Load the CSV data into a pandas DataFrame
    return pd.read_csv('Task4a_data.csv')


# creates a new dataframe with the selected income source then creates a total row
# outputs the final total in a message
def get_total_data(total_choice):
    df = pd.read_csv("Task4a_data.csv")

    income = df[["Day", total_choice]]

    total = income[total_choice].sum()

    msg = "The total income from {} was: £{}".format(total_choice, total)
    return msg


# menu option 2 code
def show_income_by_payment_type_and_source():
    df = load_data()
    # Get unique payment types from the data
    payment_types = df['Pay Type'].unique()
    print("\nAvailable Payment Types:")
    for i, payment_type in enumerate(payment_types, start=1):
        print(f"{i}. {payment_type}")

        # User selects a payment type
    payment_choice = int(input("\nSelect a payment type by entering its number: "))
    if payment_choice < 1 or payment_choice > len(payment_types):
        print("Invalid choice. Returning to main menu.")
        return
    selected_payment_type = payment_types[payment_choice - 1]

    # Get unique sources from the data (Tickets, Gift Shop, Snack Stand, Pictures)
    # Sources coded as literals for simplicity
    sources = ['Tickets', 'Gift Shop', 'Snack Stand', 'Pictures']
    print("\nAvailable Sources:")
    for i, source in enumerate(sources, start=1):
        print(f"{i}. {source}")

    # User selects a source
    source_choice = int(input("\nSelect a source by entering its number: "))
    if source_choice < 1 or source_choice > len(sources):
        print("Invalid choice. Returning to main menu.")
        return
    selected_source = sources[source_choice - 1]

    # Filter the DataFrame based on the selected payment type
    filtered_df = df[df['Pay Type'] == selected_payment_type]

    # Get the total income for the selected source over time
    total_income = filtered_df[selected_source]

    # Display the total income
    print(f"\nTotal income for {selected_source} paid by {selected_payment_type} over time:")
    print(total_income)

    # Plot the income over time
    plt.figure(figsize=(10, 6))
    plt.style.use('bmh')
    plt.bar(filtered_df['Day'], total_income)
    plt.xlabel('Day')
    plt.ylabel('Income')
    plt.title(f'Income for {selected_source} by {selected_payment_type} Over Time')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# menu option 3 code
def show_total_income_by_day():

    df = load_data()
    # Calculate the total income for each day of the week
    df['Total Income'] = df[['Tickets', 'Gift Shop', 'Snack Stand', 'Pictures']].sum(axis=1)
    total_income_by_day = df.groupby('Day')['Total Income'].sum()

    # Display the total income by day
    print("\nTotal income for each day of the week:")
    print(total_income_by_day)

    # Plot the total income by day
    plt.figure(figsize=(10, 6))
    plt.style.use('ggplot')
    total_income_by_day.plot(kind='bar', color='skyblue')
    plt.xlabel('Day')
    plt.ylabel('Total Income')
    plt.title('Total Income by Day of the Week')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()


# main menu loop
while True:
    main_menu_choice = main_menu()
    if main_menu_choice == "1":
        total_men_choice = total_menu()
        total_choice = convert_total_men_coice(total_men_choice)
        print(get_total_data(total_choice))
    elif main_menu_choice == "2":
        show_income_by_payment_type_and_source()
    elif main_menu_choice == "3":
        show_total_income_by_day()
    elif main_menu_choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else: print("Invalid choice. Please try again.")
