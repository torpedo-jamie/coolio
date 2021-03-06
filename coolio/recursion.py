def sum_array(array):

    '''Return sum of all items in array'''
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):

    '''Return n!'''
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def reverse(word):

    '''Return word in reverse'''
    if len(word) <= 1:
        return word
    else:
        return reverse(word[1:]) + word[0]
