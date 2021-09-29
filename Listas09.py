total = []

a = input("Telefonou para a vítima?")
if a == "y":
    total.append(1)
else:
    total.append(0)

b = input("Esteve no local do crime?")
if b == "y":
    total.append(1)
else:
    total.append(0)

c = input("Esteve no local do crime?")
if c == "y":
    total.append(1)
else:
    total.append(0)

d = input("Esteve no local do crime?")
if d == "y":
    total.append(1)
else:
    total.append(0)

e = input("Esteve no local do crime?")
if e == "y":
    total.append(1)
else:
    total.append(0)

sum = total[0] + total[1] + total[2] + total[3] + total[4]

categorias = ["Inocente", "Suspeito", "Cúmplice", "Cúmplice", "Assassino"]
print(categorias[sum-1])