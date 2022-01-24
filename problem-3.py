user_number_A = input("Enter Your First Number: ")
user_number_B = input("Enter Your Secoend Number: ")
user_number_C = input("Enter Your Third Number: ")

if user_number_A>user_number_C and user_number_A>user_number_B:
    print(f"{user_number_A} is Biggest Number")
elif user_number_B>user_number_A and user_number_B>user_number_C:
    print(f"{user_number_B} is Biggest Number")
elif user_number_C>user_number_A and user_number_C>user_number_B:
    print(f"{user_number_C} is Biggest Number")
else:
    print("Nothing")
    
