"""
Shopping List Manager Description:

The **Shopping List Manager** is a simple Python-based tool designed to help users keep track of their shopping items. It uses Python lists to dynamically manage the shopping list, providing essential functions like adding, removing, and viewing items.

Key Features:

1. **Add Items**  
   Users can add any number of items to their shopping list by entering the item name. The tool ensures that each added item is stored dynamically.

2. **Remove Items**  
   Users can remove items from the list by providing the exact name of the item they wish to delete. If the item is not found, a helpful message is displayed.

3. **View List**  
   The current shopping list is displayed in an easy-to-read numbered format. If the list is empty, the tool informs the user accordingly.

4. **Exit Option**  
   Users can gracefully exit the tool by selecting the exit option in the menu.

User Experience:

- **Interactive Menu**  
  The tool continuously presents a menu with clear options, making it easy for users to interact with the system.
  
- **Error Handling**  
  Handles invalid inputs gracefully, ensuring a smooth user experience.

- **Dynamic Data Management**  
  The use of Python lists allows real-time updates to the shopping list without any restrictions on the number of items.

Use Case Scenarios:

- **Daily Grocery Shopping**  
  A user can maintain a running list of groceries they need to buy and update it as needed.

- **Event Planning**  
  Helps event organizers keep track of supplies by adding or removing items from the list during preparations.

"""

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item cannot be empty.")
        
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        
        elif choice == '3':
            if shopping_list:
                print("Current Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("The shopping list is currently empty.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
