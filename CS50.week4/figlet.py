from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()


if len(sys.argv) == 1 :
    font = random.choice(font_list)
    print(font)
if len(sys.argv) == 3 :
    if sys.argv[1] == "-f" or sys.argv == "--font" :
        if sys.argv[2] in font_list:
            font = sys.argv[2]
        else :
            sys.exit("invalid command-line argument")
    else:
        sys.exit("provide -f or --font as secend command-line argument")
if len(sys.argv) == 2:
    sys.exit("too many command-line argument")


s = input("Input: ")
f = figlet.setFont(font=font)
print(figlet.renderText(s))