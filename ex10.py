print "I am 6'2\" tall." # escape double-quote inside string
print 'I am 6\'2" tall.' # escape single-quote inside string

tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\a \\cat."

fact_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fact_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,