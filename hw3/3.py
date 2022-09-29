import re
pattern_a = r'[a-zA-Z][a-z]*ime[^a-zA-Z0-9]'
with open('wordlist.txt', 'r') as file:
    s = file.read()
    list_of_words = s.split(', ')
    #print(s)
    a = re.findall("[a-zA-Z]*ime,", s)
    b = re.findall("[a-zA_Z]ave[a-b]*", s)
    c = re.findall("[a-zA-Z]*[r|s|t|l|n|e][a-z]*", s)
    d = re.findall("[a-zA-Z]*[r|s|t|l|n][a-z]*", s) 
    e = re.findall("\s[^aeiou]+,", s)
    f = re.findall("\s[a|e|i|o|u]+,", s)
print('All words ending in ime:')
for word in a:
    new_word = re.sub(',', '', word)
    print(new_word, end = ' ')
print('\nAll words whose second, third, and fourth letters are ave:')
for word in b:
    print(word, end = ' ')
print(f'\n{len(c)} words contain at least one of the letters r, s, t, l, n, e')    
print(f'{round(len(d) * 100/len(list_of_words))}% of words contain at least one of the letters r, s, t, l, n')
print('All words with no vowels:')

for word in e:
    new_word = re.sub(',', '', word)
    word1 = new_word.strip(" ")
    print(word1, end = ' ')
print('\nAll words that contain only vowel:')
for word in f:
    new_word = re.sub(',', '', word)
    word1 = new_word.strip(" ")
    print(word1, end = ' ')