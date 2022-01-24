user_number=int(input("Enter Your Number: "))

if user_number%2==0 and not user_number==0:
    print(f"{user_number} is Even number")
elif  not user_number%2==0 or user_number==0:
    print(f"{user_number} is odd number")
else:
    print("Nothing")
    