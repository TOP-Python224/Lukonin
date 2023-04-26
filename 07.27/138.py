dic = {
    1: '.,?!:',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ',
    0: ' '
}

dic1 = {}
for key, value in dic.items():
    for indx, letter in enumerate(value, 1):
        dic1[letter] = str(key) * indx
        
text = input().upper()

for i in text:
    print(dic1.get(i, ''), end='')