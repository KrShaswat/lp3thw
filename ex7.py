print("Mary had a little lamb.")
# whole format thing can be done inside a print
print("Its fleece  was white as {}.".format('snow'))
print("And everywhee that Mary went.")
# it seems we can now multiply strings too
print("."*10) #should print 10 .s
# variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# cheese and burger are in different lines
# instead of "\n" its " " for end of line
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)