intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "This is string example!"
print(str.translate(trantab), "\n")



intab = "aeiou"
trantab = str.maketrans("", "", intab)

str = "This is second string example!!"
print(str.translate(trantab), "\n")



symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]
map = {}

for s, c in zip(symbols, code):
    map[ord(s)] = c
    map[ord(s.lower())] = c

result = "43 FD 65 ACDC".translate(map)
print(result)
print(map, "\n\n")



# Morze Code
morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}
table_morze_dict = {}

for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

print(table_morze_dict)
string = "Oh, Lolitto senioritto! You PERFAVORE!"
result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)