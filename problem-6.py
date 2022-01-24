user_number= int(input("Enter Your Maultipation Number: "))
def print_namta(namata_num):
    for i in range(1,11):
        value=namata_num*i
        print( f'{namata_num} X {i} = {value}')

print_namta(user_number)

