import re

from ModulesDatetimeTimeAndMath.working_with_random_variables import fruits

text = "Learning Python can be fun."
pattern = "Python"
match = re.search(pattern, text)

if match:
    print("Found: ", match.group(), "=", match.span(), "\n")
else:
    print("Not found")



import re

text = "Learning Python can be fun."
pattern = r"L\w*g"
match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Found: ", match.group(), "\n")



import re

text = "My email: sontaran345@sontar.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)

if match:
    print(f"Found: {match.group()} \n")
else:
    print("Not found")



import re

text = "My email: sontaran345@sontar.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, text)

if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print(f"User name: {user_name}")
    print(f"Domain name: {domain_name} \n")
else:
    print("Not found")



import re

text = "The year 2023 was more challenging than 2022"
pattern = r"\d+"
matches = re.findall(pattern, text)

print(f"Found: {matches} \n")



import re

text = "Python is a simple but powerful programming language."
pattern = r"\w+"
matches = re.findall(pattern, text)

print(f"Found: {matches} \n")



import re

text = "Contacts: example1@example.com, example2@sample.org"
pattern = r"\w+@\w+\.\w+"
matches = re.findall(pattern, text)

print(f"Found: {matches} \n")



import re

file_name = "My document Neuroengineering.txt"
pattern = r"\s"
replacement = "_"
formatted_name = re.sub(pattern, replacement, file_name)

print(f"Formatted name: {formatted_name} \n")



import re

text = "Python - is a powerful, versatile; language!"
pattern = r"[;,\-:!\.]"
replacement = ""
modified_text =re.sub(pattern, replacement, text)

print(f"Modified text: {modified_text} \n")



import re

phone = """
        Glasgo: 050-171-1634
        Tigernaht: 063-134-1729
        Dumix: 068-234-5612
        """
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"
formatted_phone = re.sub(pattern, replacement, phone)

print(f"Formatted phone: {formatted_phone} \n")



import re

text = "Python - is a simple, but powerful programming language."
pattern = r"\s+"
words = re.split(pattern, text)

print(f"Words: {words} \n")



import re

text = "Python - is a powerful; simple, versatile: language!"
pattern = r"[;,\-:\.!\s]+"
elements = re.split(pattern, text)

print(f"Elements: {elements} \n")



import re

text = "apple#banana!mango@orange;kiwi"
pattern = r"[#@;!]"
fruits = re.split(pattern, text)

print(f"Fruits: {fruits} \n")










