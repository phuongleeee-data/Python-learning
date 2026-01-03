my_foods = ['hot pot', 'BBQ', 'sushi', 'chicken', 'pizza']
for food in my_foods:
    print(f"The first three items in the list are {my_foods[:3]}")
    print(f"The three middle items in the list are {my_foods[2:]}")
    print(f"The last three items in the list are {my_foods[-3:]}")
    break

pizzas = ['pizza hải sản', 'pizza thịt xông khói', 'pizza phô mai', 'pizza xúc xích']
friends_pizzas = pizzas[:]

for pizza in pizzas:
    print(f"My favorite pizza is {pizza}")

for friend in friends_pizzas:
    print(f"My friend's favorite pizza is {friend}")


