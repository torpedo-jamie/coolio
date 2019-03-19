def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
    return items

def merge(left, right):

    '''Returns array, merged from two input array arguments'''
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if len(left) == 0:
        result = result + right
    if len(right) == 0:
        result = result + left
    return result

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items) <= 1:
        return items

    mid = int(len(items) / 2)
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items) <= 1:
        return items

    pivot = items[-1] # last item of array is pivot in this case
    small = []
    large = []
    duplicate = []
    for item in items[0:]:
        if item < pivot:
            small.append(item)
        elif item > pivot:
            large.append(item)
        elif item == pivot:
            duplicate.append(item)

    small = quick_sort(small)
    large = quick_sort(large)
    return small + duplicate + large
