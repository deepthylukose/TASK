import re
def border(word):
    size = max(len(i) for i in word)
    print('*' * (size + 4))
    for i in word:
        print('* {:<{}} *'.format(i,size))
    print('*' * (size + 4))

sentence=raw_input("Enter the input:")
x=re.compile('[\.]')
if all(a.isalpha() or a.isspace() or x.match(a) for a in sentence):
    word = sentence.split()
    border(word)
else:
    print "Enter only letters and spaces"