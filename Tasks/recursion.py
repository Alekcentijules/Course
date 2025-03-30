def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5))


def discount_price(price, discount):
    def apply_discount():
        nonlocal price, discount
        price = price * (1 - discount)
    apply_discount()
    return price

result = discount_price(22, 0.22)
print(result)



def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    return factorial(n) // (factorial(n-k) - factorial(k))

result = number_of_groups(50, 7)
print(result)