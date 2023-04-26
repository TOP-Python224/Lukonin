string = input(' > ')
binary = {'0', '1', 'b'}

if set(string).issubset(binary):
    print('ДА')
else:
    print('НЕТ')
