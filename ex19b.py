from sys import argv
script, principle_argv = argv

def funKtion(amount, intrest = 0.03):
    return amount + (amount*intrest)

# to run this ten different ways
urmon = funKtion(1000)
print(urmon) #1

print(funKtion(1000)) #2

principle = 1000
print(funKtion(principle)) #3

urmon = funKtion(principle)
print(urmon) #4

urmon = funKtion(principle +100)
print(urmon) #5

print(funKtion(1000 + 100, 0.07)) # 6

print(funKtion(principle_argv)) # 7

urmon = funKtion(principle_argv)
print(urmon) # 8

