foods = ("Biriyani", "Chicken Momo", "Beef kala Bhuna", "Mutton Curry", "Borhani")
for i in foods:
    print(i)

print("\n")
try:
    foods[2] = "Cashewnut Salad"
except Exception as e:
    print(e, "\n")

foods = ("Biriyani", "Chicken Momo", "Fried Rice", "Thai Vegetabels", "Jarda")
for i in foods:
    print(i)