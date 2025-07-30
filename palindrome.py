def palindrome(number):
    converted_number = str(number)
    reversed_num = converted_number[::-1]
    return converted_number == reversed_num
