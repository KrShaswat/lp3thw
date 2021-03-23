# function take 2 parameters and just prints . . .
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.")

# it takes number
print("We can give the function numbers directly:")
# calling function with numbers
cheese_and_crackers(20, 30)

# it also takes variable
print("OR, we can use varibles from our script")
amount_of_cheese = 10
amount_of_cracker = 50
# calling the functions with variables
cheese_and_crackers(amount_of_cheese, amount_of_cracker)

# yeah seperated by , we can do math for each varible input to the function
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# math will take varoble and numbers too
print("And we can combine the two, varible and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_cracker + 1000)