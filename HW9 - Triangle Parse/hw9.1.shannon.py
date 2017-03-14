

three_dig_seq = range(100,1000)
# and an empty list for the palindromes
list_palindromes = []

a = 0
b = 0
for n1 in three_dig_seq:
    for n2 in three_dig_seq:
        number =  n1 * n2
        number = str(number)
        if number == number[::-1] and n1 * n2 > a * b:
        	a = n1
        	b = n2
        	list_palindromes.append(int(number))
 

print("{} x {} = {}".format(a, b, max(list_palindromes)))