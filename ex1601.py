from sys import argv

script, filename = argv

txt = open(filename)
print "We are gona open %s." % filename
print txt.read()
