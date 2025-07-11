import bisect

_ALL_PALINDROMES = []

def _generate_palindromes(limit):
    palindromes_list = []

    for i in range(1, 10):
        palindromes_list.append(i)

    for i in range(1, 100000):
        s = str(i)
        
        even_pal_str = s + s[::-1]
        even_pal = int(even_pal_str)
        if even_pal < limit:
            palindromes_list.append(even_pal)
        
        for j in range(10):
            odd_pal_str = s + str(j) + s[::-1]
            