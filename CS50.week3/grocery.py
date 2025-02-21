grocery = {}
while True:
    try:
        item = input().upper()
        if item in grocery :
            grocery[item] += 1
        else:
            grocery[item] = 1
    except (EOFError,KeyError):
        for key in sorted(grocery) : 
            print(grocery[key],key)
        break
