import re

regex = r"((M|m)+) [a-zA-Z0-1] {5,8} ((M|m)+)"
findall = re.search(regex, "https://moure.dev")
print(findall)

regex = r"((M|m)+) [a-zA-Z0-1]((M|m)+)"
findall = re.search(regex, "https://moure.dev")
print(findall).