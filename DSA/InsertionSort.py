def insertion_sort(lst):
    for i in range(1, len(lst)):
        current = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > current:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current
    return lst

lst = [1, -7, 78, 12, 9, 54, -2, 6, -77, 66]

print(f"Original : {lst}")
insertion_sort(lst)
print(f"After Insertion Sort : {lst}")

# Output ---------------
# Original : [1, -7, 78, 12, 9, 54, -2, 6, -77, 66]
# After Insertion Sort : [-77, -7, -2, 1, 6, 9, 12, 54, 66, 78]
