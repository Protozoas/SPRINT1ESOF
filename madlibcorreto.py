#! python3

import re

madText = open('madText.txt', 'w')

text = 'An ADJECTIVE panda walked to the NOUN ans then  VERB.A nearby NOUN was unaffected by these events.'

madText.write(text)
madText.close()

content = re.split('\W+', text)

for i in content:

    if i == "ADJECTIVE":
        replaceRegex = re.compile(r'(ADJECTIVE)')
        print('Enter an ADJECTIVE:')
        ADJECTIVE = input()
        output = replaceRegex.sub(ADJECTIVE, str(content))

    elif i == "NOUN":
        replaceRegex = re.compile(r'(NOUN)')
        print('Enter a NOUN:')
        NOUN = input()
        output = replaceRegex.sub(NOUN, str(output))

    elif i == "VERB":
        replaceRegex = re.compile(r'(VERB)')
        print('Enter an VERB:')
        ADVERB =  input()
        output = replaceRegex.sub(ADVERB, str(output))

    elif i == "NOUN":
        replaceRegex = re.compile(r'(NOUN)')
        print('Enter a NOUN:')
        VERB = input()
        output = replaceRegex.sub(VERB, str(output))

content = re.split('\W+', output)
#content = list(output.split(' '))
content = ' '.join(content)
print(content)
madLibs = open('madText2.txt', 'w')
madLibs.write(content)
madLibs.close()
