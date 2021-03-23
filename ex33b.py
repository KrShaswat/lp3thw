# sudy drill rewrite using for
def add_num(times, list = [], increment = 1.0):
    for i in range(0,times, increment):
        print("Number being added in list: ", i)
        list.append(i)

        print("Numbers in list now: ", list)
    return list
