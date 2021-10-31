






my_str = input()
my_str_ns = ""
for x in my_str:
    if x != ' ':
        my_str_ns += x

reversed_str = my_str[::-1]
rev_str_ns = ""
for x in reversed_str:
    if x != ' ':
        rev_str_ns += x

if my_str_ns == rev_str_ns:
    print(my_str, 'is a palindrome')
else:
    print(my_str, 'is a not palindrome')