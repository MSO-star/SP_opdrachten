def sort(lst):
    for i in range(1, len(lst)):
        while i > 0 and lst[i] < lst[i - 1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i = i-1
    return lst

print(sort([2,7,5,4,2]))