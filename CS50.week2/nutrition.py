fruits = {
          "apple":130,
          "avocado":50,
          "banana":110,
          "cantaloupe":50,
          "grapefruit":60,
          "grapes":90,
          "honeydewmelon":50,
          "kiwifruit":90,
          "lemon":20,
          "nectarine":60,
          "orange":80,
          "orange":80,
          "peach":60,
          "pear":100,
          "pineapple":50,
          "pulms":70,
          "strawberries":50,
          "sweet cherries":100,
          "tangerine":50,
          "watermelon":80
          }

user_input = input("item: ").lower()

while True:
    if user_input in fruits :
        print(f"calories: {fruits[user_input]}")
        break
    else:
        break 
