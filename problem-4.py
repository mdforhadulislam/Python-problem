user_first_number=int(input("Enter Your First Number: "))
user_symbol_number=input("Enter Your symbol: ")
user_secoend_number=int(input("Enter Your Secoend Number: "))

if user_symbol_number=='+' and len(user_symbol_number)==1:
    print(user_first_number+user_secoend_number)
elif user_symbol_number=='-' and len(user_symbol_number)==1:
    print(user_first_number-user_secoend_number)
elif user_symbol_number=='/' and len(user_symbol_number)==1:
    print(user_first_number/user_secoend_number)
elif user_symbol_number=='*' and len(user_symbol_number)==1:
    print(user_first_number*user_secoend_number)
else:
    print("Nothing")

