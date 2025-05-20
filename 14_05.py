# All Types of Operators in One Page

# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")
print()

# 2. Comparison Operators
print("Comparison Operators:")
print(f"{a} == {b} : {a == b}")
print(f"{a} != {b} : {a != b}")
print(f"{a} > {b} : {a > b}")
print(f"{a} < {b} : {a < b}")
print(f"{a} >= {b} : {a >= b}")
print(f"{a} <= {b} : {a <= b}")
print()

# 3. Logical Operators
x = True
y = False
print("Logical Operators:")
print(f"{x} and {y} = {x and y}")
print(f"{x} or {y} = {x or y}")
print(f"not {x} = {not x}")
print()

# 4. Assignment Operators
num = 5
print("Assignment Operators:")
print(f"Initial num: {num}")
num += 3
print(f"After += 3: {num}")
num *= 2
print(f"After *= 2: {num}")
num -= 4
print(f"After -= 4: {num}")
num /= 2
print(f"After /= 2: {num}")
num %= 3
print(f"After %= 3: {num}")
print()

# 5. Bitwise Operators
m = 6   # 110
n = 3   # 011
print("Bitwise Operators:")
print(f"{m} & {n} = {m & n}")
print(f"{m} | {n} = {m | n}")
print(f"{m} ^ {n} = {m ^ n}")
print(f"~{m} = {~m}")
print(f"{m} << 1 = {m << 1}")
print(f"{m} >> 1 = {m >> 1}")
print()

# 6. Membership Operators
text = "apple"
print("Membership Operators:")
print(f"'a' in '{text}' = {'a' in text}")
print(f"'z' not in '{text}' = {'z' not in text}")
print()

# 7. Identity Operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("Identity Operators:")
print(f"list1 is list2 = {list1 is list2}")   # True
print(f"list1 is list3 = {list1 is list3}")   # False
print(f"list1 == list3 = {list1 == list3}")   # True (same content)
