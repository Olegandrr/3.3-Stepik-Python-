import re
import requests
yes = 'No'

A, B = input(), input()

A = requests.get(A)
pattern = r'https:.*html'
link_from_A = re.findall(pattern, A.text)
for i in link_from_A:
    if i == B:
        i = requests.get(i)
        link_from_i = re.findall(pattern, i.text)
        for x in link_from_i:
            if x == B:
                yes = 'yes'
                break

    else:
        i = requests.get(i)
        link_from_i = re.findall(pattern, i.text)
        for x in link_from_i:
            if x == B:
                yes = 'yes'
                break
print(yes)


