a = int(input())
ls = []
ls2 = []
for i in range(a):
    ls.append(int(input()))

for i in ls:
    if i >= 15:
        ls2.append(i)
print(len(ls2))