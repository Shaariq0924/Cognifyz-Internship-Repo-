def temperature_converter():
    print("Welcome to the Temperature Converter!")

    while True:
        print("\nchoose an option:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
    
        user_choice = input(("choose an from option(1 to 3): "))
        if(user_choice == "1"):
            C = float(input("Enter temperature in Celsius:"))
            C_to_F = (C*(9/5))+32
            print(f"{C}°C = {C_to_F:.2f}°F")
        elif(user_choice == "2"):
            F = float(input("Enter temperature in Fahrenheit:"))
            F_to_C = (F-32)*5/9
            print(f"{F}°F = {F_to_C:.2f}°C")
        elif(user_choice == "3"):
            print("Exiting the converter!")
            break
        else:    
            print("wrong option!")       

#calling the Temp fn
temperature_converter()


    



