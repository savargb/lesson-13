def cube_cube(num):
    return num * num * num

def check_number(num):
    if num % 3 == 0:
        print(cube_cube(num))
    else:
        print("not divisible")

num = float(input("Enter a number"))
check_number(num)




