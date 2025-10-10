#Author: Robin Bengtsson
#Date: 2025-10-10

input_string = input("vilka tabeller vill du beräkna? ")


if input_string:
    input_list = input_string.split()
    
    for i in input_list:
        for j in range(1,11):
            print(f"{i} * {j} = {int(i)*j}")
        print("\n")
else:
    print("Du har inte angett något värde")


