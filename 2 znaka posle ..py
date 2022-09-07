grade = input().split()

""" Finds how many elements in input equals A and finds its median value with 2 signs after dot """

suma = 0
for a in grade:
    if a.upper() == 'A':
        suma += 1
leng = len(grade)
final = float(suma/leng)
'{0:.2f}'.format(final)

print("{0:.2f}".format(final))
