#code 1
def early_termination_for(n):
    for i in range(n):
        if i > 5:
            print(f"{i} is less than 5")
        else:
            print(f"{i} is greater than 5")

#code 2
def nested_if_for(n):
    for i in range(n):
        if i % 2 == 0:
            if i % 4 == 0:
                print("Divisible by 4")
            else:
                print("Even but not divisible by 4")
        else:
            print("Odd")

#code 3
def combined_loops(n):
    for i in range(n):
        while i > 0:
            i -= 1
            print(i)

#code 4
def nested_loops(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

#code 5
def check_all_positive(numbers):
    for num in numbers:
        if num > 50:
            print("Greater than 50")
        elif num == 50:
            print("Equal to 50")
        else:
             print("Smaller than 50")
