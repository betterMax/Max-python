# import two types of code from two modules

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
# open the from_file and set the variable to be its content
in_file = open(from_file)
indata = in_file.read()

# count the length of its content
print "The input file is %d bytes long" % len(indata)

# judge if the file exists
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# open the to_file and write the content of from_file
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

# close both files
out_file.close()
in_file.close()
