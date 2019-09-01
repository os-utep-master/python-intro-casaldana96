import re

# create empty dictionaries
d = dict()  # search dictionary
d2 = dict()  # declaration dictionary


with open('search.txt', 'r') as searchIn, open('declaration.txt', 'r') as declarationIn:
    # search text
    for line in searchIn:
        # remove newline char
        line = line.strip()
        # convert chars to lowercase
        line = line.lower()
        line = re.sub('[!@#$,".:;]', '', line)
        line = re.sub("[-,']", ' ', line)
        # split line into words
        words = line.split()
        # count words
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    # declaration text
    for line in declarationIn:
        # remove newline char
        line = line.strip()
        # convert chars to lowercase
        line = line.lower()
        line = re.sub('[!@#$,".:;]', '', line)
        line = re.sub("[-,']", ' ', line)
        # split line into words
        words = line.split()
        # count words
        for word in words:
            if word in d2:
                d2[word] = d2[word] + 1
            else:
                d2[word] = 1

with open('searchKey.txt', 'w') as searchOut, open('declarationKey.txt', 'w') as declarationOut:
    # print in output files
    for key in sorted(d.keys()): # sort words alphabetically
        searchOut.write(str(key) + " " + str(d[key]) + "\n")

    for key in sorted(d2.keys()):
        declarationOut.write(str(key) + " " + str(d2[key]) + "\n")
