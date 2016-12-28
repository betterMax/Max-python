from sys import argv

script, filename = argv

# type some descriptions, give two options
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# ask for which option
raw_input("?")

# open the file
print "Opening the file..."
target =open(filename, 'w')

# delete the file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# Collect new staff for the file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# write the new staff in the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# close the file
print "And finally, we close it."
target.close()
