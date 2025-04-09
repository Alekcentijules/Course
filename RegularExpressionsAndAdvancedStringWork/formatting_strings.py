for i in range(8):
    s = f"int: {i:d}; hex: {i:#x}, oct: {i:#o}; bin: {i:#b}"
    print(s)



price = 22.22
quantity = 6
total = f"Total: {price * quantity:.2f}"
print(f"\n{total}")



width = 7
for num in range(12):
    print(f"{num:^10} {num**2:^10} {num**3:^10}")



completion = 0.946
formatted = f"{completion:.1%}"
print(f"\n{formatted}")

progress = 0.66
formatted = f"\n{progress:.0%}"
print(formatted)