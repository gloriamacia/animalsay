import sys

from farm.animals import _cow 
# why does from farm.animals import * not work,
# like it seems to need a function, not a variable
from home.animals import _bunny, _cat


flg = []

animals = {'cow':_cow, 'bunny':_bunny, 'cat':_cat}

def string_processing(args):

    args = str(args)
    lines = args.split("\n")
    lines = [i.strip() for i in lines]
    lines = [i for i in lines if len(i) != 0]
    length = len(lines)
    
    if length == 1:

        flag = len(lines[0])
        if flag < 50:
            print("  " + "_" * flag)
            print("< " + lines[0] + " " * (flag - len(lines[0]) + 1) + ">")
            print("  " + "=" * flag)
            flg.append(flag)
        else:
            args = list("".join(lines[0]))
            for j, i in enumerate(args):
                if j % 50 == 0:
                    args.insert(j, "\n")
            string_processing("".join(args))
               
    else:
        flag = len(max(lines, key=len))
        if all(len(i) < 50 for i in lines):
            print("  " + "_" * flag)
            print(" /" + " " * flag + "\\")
            for i in lines:
                print("| " + i + " " * (flag - len(i) + 1) + "|")
            print(" \\" + " " * flag + "/")
            print("  " + "=" * flag)
            flg.append(flag)                    
        else:
            new_lines = []
            for i in lines:
                if len(i) > 50:
                    args = list("".join(i))
                    for j, i in enumerate(args):
                        if j % 50 == 0:
                            args.insert(j, "\n")
                    new_lines.append("".join(args))
                else:
                    new_lines.append(i + "\n")
            string_processing("".join(new_lines))
                    
def talk(animal, text):

    try:

        string_processing(text)
        flag = flg[-1]

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')

        animal_drawing = animals[animal]
        char_lines = animal_drawing.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag + 5) + i)

    except:
        print("I cannot say this! Give me something easier")


