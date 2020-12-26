from .farm.animals import *
from animalsay.home.animals import * # both lines above work

flg = []
animals = {'cow':cow, 'bunny':bunny, 'cat':cat}


def string_processing(text):
    args = str(text)
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

def say(animal, text):
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