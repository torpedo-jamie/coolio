from coolio import myFunction

def test_sum_array():
    '''testing if sum_array works correctly'''

    assert myFunction.sum_array([1,2,3]) == 6, 'incorrect'

def test_fibonacci():
    '''testing if fibonacci works correctly'''

    assert myFunction.fibonacci(7) == 13, 'incorrect'

def test_factorial():
    '''testing if factorial works correctly'''

    assert myFunction.factorial(5) == 120, 'incorrect'

def test_reverse():
    '''testing if reverse works correctly'''

    assert myFunction.reverse('jamie') == 'eimaj', 'incorrect'

def test_bubble_sort():
    '''testing if bubble_sort works correctly'''

    assert myFunction.bubble_sort([5,2,6,8,1,2]) == [1, 2, 2, 5, 6, 8], 'incorrect'

def test_merge_sort():
    '''testing if merge_sort works correctly'''

    assert myFunction.merge_sort([5,2,6,8,1,2]) == [1, 2, 2, 5, 6, 8], 'incorrect'

def test_quick_sort():
    '''testing if quick_sort works correctly'''

    assert myFunction.quick_sort([5,2,6,8,1,2]) == [1, 2, 2, 5, 6, 8], 'incorrect'
