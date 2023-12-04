# TODO: Implement a function that returns a list of numbers from 1 to n (already provided in original list)
def generate_numbers(n):
    a =[]
    for i in range(1,n+1):
        a.append(i)
    return a
# TODO: Implement a 8qw9lfunction that takes two lists as arguments, merges them into one list, and then sorts the merged list in ascending order
def merge_and_sort_lists(list1, list2):
    a = list1+list2
    for i in range(0,len(a)):
        for b in range (0,len(a)-i-1):
            if a[b]>a[b+1]:
                a[b],a[b+1]=a[b+1],a[b]
    return a
# TODO: Implement a function that removes all duplicate values in a list and returns a list with only the unique elements in the order they appeared
def remove_duplicates(my_list):
    r = []
    for i in my_list:
        if i not in r:
            r.append(i)
        
    return r
# TODO: Implement a function that checks whether a list is a sublist of another list. A sublist is a sequence of consecutive elements that are part of another list
def is_sublist(list1, list2):
    a = 0
    for i in list1:
        if i in list2:
            a += 1
    if a == len(list1):
        return True
    else:
        return False
# TODO: Implement a function that rotates the elements of a list to the right by `k` places. `k` is non-negative
def rotate_list(my_list, k):
    if my_list==[] or k == 0:
        return my_list
    k = k % len(my_list) 
    r = my_list[-k:] + my_list[:-k]

    return r

