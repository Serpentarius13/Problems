""" Find indexes of specific items in inputted list """

l = input().split()
number = input()
def checker(list, number):
    x = 0
    pos = ""
    if number in list:
        while x < len(list):
            a = list[x]
            if a == number:
                pos += f"{x} "
            x += 1
    else:
        return None
    return pos

print(checker(l,number))
