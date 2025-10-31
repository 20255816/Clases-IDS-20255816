ls = [input(), input(), input(), input(), input(), input()]
ls = list(map(float, ls))
total = (sum(ls)/6)

if total >= 9.5:
    print('Gana Premio :)')
else:
    print('No gana premio :(')