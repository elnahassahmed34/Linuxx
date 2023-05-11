while True:
    print("\nWelcome Plz choose Function\n")
    print("1. isalpha()")
    print("2. partition()")
    print("3. upper()")
    print("4. Exit")
    choice = input("\nEnter your choice: ")
    
    data = "Ahmed Elnahass 1234"

    if choice == '1':
        print("Returns True if all characters in the string are in the alphabet")
        print(data)
        print(data.isalpha())
    elif choice == '2':
        print("Returns a tuple where the string is parted into three parts")
        print(data)
        print(data.partition())
    elif choice == '3':
       print("Converts a string into upper case")
       print(data)
       print(data.upper())
    elif choice == 27:
        print("\nThank you for using the ATM Machine. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
