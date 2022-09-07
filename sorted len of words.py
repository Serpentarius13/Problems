""" Searches for len of words and prints how many words has the same length in input """

words = input().split()
lengths = []
for i in words:
    leng = len(i)
    lengths.append(leng)

len2 = lengths.copy()
same = {}
c = 0

for a in lengths:
    for b in words:
        if len(b) == a:
            c += 1
    same[a] = c
    c = 0


for k in sorted(same):
    a = same.get(k)
    print(f"{k}: {a}")
