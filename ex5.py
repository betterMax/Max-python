# My name is Zed A. Shaw
name = 'Zed A. Shaw'
# My age is 35
age = 35 # not a lie
# My height is 74 # inches
height = 74
# My weight is 180 lbs
weight = 180
# I have bule eyes
eyes = 'Blue'
# I have white teeth
teeth = 'White'
# My hair is brown
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
  age, height, weight, age +height+weight)

height_cm = height * 2.54
weight_kg = weight * 0.454

print "He's %d cm tall." % height_cm
print "He's %d kg heavy." % weight_kg
