word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for x in croatia:
    word = word.replace(x, '*')

print(len(word))
