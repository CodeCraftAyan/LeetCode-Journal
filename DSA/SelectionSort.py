def selection_sort(lst):
    n = len(lst)

    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_i]:
                min_i = j   

        lst[i], lst[min_i] = lst[min_i], lst[i]

    return lst

lst = [12, 4, 56, 1, 7, -7, 71]

print(f"Original : {lst}")
selection_sort(lst)
print(f"After Selection sort : {lst}")

# Output ---------------
# Original : [12, 4, 56, 1, 7, -7, 71]
# After Selection sort : [-7, 1, 4, 7, 12, 56, 71]
