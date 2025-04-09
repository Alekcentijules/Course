def string_to_codes(string: str) -> dict:
    codes = {}
    for ch in string:
        if ch not in codes:
            codes[ch] = ord(ch)
    return codes

result = string_to_codes("Cherry-cherry lady!")
print(f"Your result: {result}")