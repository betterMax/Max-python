print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you are %r old, %r tall and %r heavy." % (
  age, height, weight)
print "so, you are %s old, %s tall and %s heavy." % (
  age, height, weight)

print "How much is the apple?",
apple_each = int(raw_input())
print "OK. I would take some."
print "Cool. How many do you want?",
apple_number = int(raw_input())
x = apple_each * apple_number
print "Here you go. It is " + str(x) + " yuan at total."
