def main():
    time = input("What time is it?")
    x = convert(time)
    if 8 > x > 7 :
        print("breakfast time")
    elif 13 > x > 12 :
        print("lunch time")
    elif 19 > x > 18 :
        print("dinner time")
    else:
        print("")

def convert(time):
    hr,min = time.strip().split(":")
    hr = float(hr)
    min = float(min)/60
    return hr+min
main()