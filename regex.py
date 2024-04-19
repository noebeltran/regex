import re

regex = r"(www\.)\w{3,}\.n"
findall = re.search(regex, "https://www.moure.dev")
print(findall)