def bubble_sort(arrLst):
    n = len(arrLst)
    for i in range(n):
        for j in range(n):
            if arrLst[i] < arrLst[j]:
                arrLst[i], arrLst[j] = arrLst[j], arrLst[i]            
    return arrLst

arrLst = [12, 45, 81, 16, 37, 4, 91, -56, 78, 1, -7, 24, -34]

print(f"Before Sort : {arrLst}")
bubble_sort(arrLst)
print(f"After Bubble Sort : {arrLst}")

# Output ---------------
# Before Sort : [12, 45, 81, 16, 37, 4, 91, -56, 78, 1, -7, 24, -34]
# After Bubble Sort : [-56, -34, -7, 1, 4, 12, 16, 24, 37, 45, 78, 81, 91]
