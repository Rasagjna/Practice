text = "The agents's phone number is 408-555-1234. Call soon!"
print('phone' in text)
import re

pattern = 'phone'
match = re.search(pattern, text)
print(re.search(pattern, text))
print(re.search('NOT IN TEXT', text))
print(match.span())
print(match.start())
print(match.end())
text = 'my phone once, my phone twice'
match = re.search('phone', text)
print(match)
matches = re.findall('phone', text)
print(matches)
print(len(matches))
for match in re.finditer('phone', text):
    # print(match.span())
    print(match.group())
# ///////////////////////////////////////
# \d - a digit, \w - alphanumeric, \s - whitespace, \D - a non digit
# \D - a non digit , \W - Non-alphanumeric, \S - Non-whitespace
text = "my phone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone)
print(phone.group())

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results=re.search(phone_pattern,text)
print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))
# print(results.group(7)) #error
print(re.search(r'cat|dog','The cat is here'))
print(re.findall(r'...at','the cat in the hat went splat.'))
print(re.findall(r'^\d','1 is a number'))
print(re.findall(r'\d$','the number is 2'))
phrase="there are 3 numbers 34 inside 5 this sentence"
pattern=r'[^\d]+'
print(re.findall(pattern,phrase))
test_phrase='this is a string!but it has punctuation.How can we remove it?'
print(re.findall(r'[^!.?]+',test_phrase))
print(' '.join(re.findall(r'[^!.?]+',test_phrase)))
text='Only find the hypen-words in this sentence. But you do not know how long-ish they are'
pattern=r'[\w]+-[\w]+'
print(re.findall(pattern,text))
text='Hello, would you like some catfish?'
texttwo="Hello, would you like to take a catnap?"
textthree="Hello, have you seen this caterpillar?"
print(re.search(r'cat(fish|nap|erpillar)',textthree))
