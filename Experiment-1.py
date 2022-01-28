# Without package nltk
import os
import sys
stopwords = ['.',',','-',"'","–",'>','a','they','the','his','so',
            'and','were','from','that',
            'of','in','only','with','to']

s = input("Enter the sentence/para to remove stopwords or 'file/File' to open a file: ")
file = False
if s in ["File","file"]:
    fname = input("Enter the filename: ")
    file = True
if os.path.isfile(fname):
    s = open(fname, 'r').read()
else:
    print("No such file exists")
    print("Exiting...")
    sys.exit(1)
filtered = []
sens = []

# Remove basic words
for x in s.split(' '):
    if x not in stopwords:
        if x == '\n' and file:
            sens.append(' '.join(filtered))
            filtered = []
        else:
            filtered.append(x)

# Removes deeper commas or full stops
for i in range(len(filtered)):
    filtered[i] = ''.join([f for f in filtered[i] if f not in stopwords[:5]])
if not file:
    print()
    print("Array of tokens without stopwords --")
    print(filtered)
    print()
    print("Final Answer is")
    print(' '.join(filtered))
else:
    store = open('output.txt','w+')
    store.writelines(sens)
    store.close()
    print("Your file is stored as output.txt")
