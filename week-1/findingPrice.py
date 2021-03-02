price = 10000
total = 0
for i in range(1,14):
    price += price * 0.05
    if i == 10:
        print("price in 10 yrs :")
        print(price)
    if i > 10 :
        total += price
print("price after 4 years after 10years: ")
print(total)