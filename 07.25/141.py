num = int(input('Введите число в диапазоне от 0 до 999: '))

nums = {1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen'}
tens = {2:'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety'}

num_to_word = ''

   
if len(str(num)) == 3:
    if num // 100 > 0:
        num_to_word += f'{dict(list(nums.items())[:10])[num // 100]} hundred'
units_and_tens = num % 100
if units_and_tens > 0:
    if units_and_tens in nums.keys():
        if len(num_to_word) > 0:
            num_to_word += ' '
        num_to_word += nums[units_and_tens]
    else:
        if len(num_to_word) > 0:
            num_to_word += ' '
        if units_and_tens // 10 > 0:
            num_to_word += tens[units_and_tens // 10]
        if int(str(units_and_tens)[-1]) > 0:
            if units_and_tens // 10 > 0:
                num_to_word += ' '
            num_to_word += nums[int(str(units_and_tens)[-1])]
if num == 0:
    num_to_word = 'zero'

print(num_to_word)
