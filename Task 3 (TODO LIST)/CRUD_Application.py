lists = ['eat', 'code']

def add(item):
    lists.append(item)

def Read():
    for item in lists:
        print(item)

def Remove(item):
    if item in lists:
        lists.remove(item)
        print(f"'{item}' has been removed.")
    else:
        print(f"'{item}' not found in list.")

def Update(index, new_value):
    if 0 <= index < len(lists):
        lists[index] = new_value
        print(f"Item at index {index} updated to '{new_value}'.")
    else:
        print("Invalid index.")

print("Welcome to Console application for basic CRUD operations!")

while True:
    print("\nChoose an option:")
    print("1. Add")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        item = input("Enter item to add: ")
        add(item)

    elif choice == "2":
        print("Current list:")
        Read()

    elif choice == "3":
        index = int(input("Enter index to update: "))
        new_value = input("Enter new value: ")
        Update(index, new_value)

    elif choice == "4":
        item = input("Enter item to delete: ")
        Remove(item)

    elif choice == "5":
        print("Exiting the application.")
        break

    else:
        print("Invalid choice. Please try again.")

    #Final list
    print("\n Final list:")
    Read()