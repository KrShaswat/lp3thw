i = 0 
numbers = []
def add_num(times, list = [], increment = 0):
    i = 0
    while i<times:
        print(f"At the top i is {i}")
        list.append(i)

        i += increment
        print("Number now: ", list)
        print(f"At the bottom i is {i}")
    return list

numbers = add_num(7)
print("The numbers: ")

for num in numbers:
    print(num)