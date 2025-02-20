camel = input("camelcase: ")

for i in camel:
    if i.isupper() and not i == camel[0] :
        camel = camel.replace(i, "_"+i.lower())

print(camel)