def prefix_sum(arrLst):
    for i in range(1, len(arrLst)):
        arrLst[i] = arrLst[i] + arrLst[i-1]
    return arrLst

arrLst = [10, 20, 6, 11, 8]
print(f"Before : {arrLst}")

# Output ---------------
# Before : [10, 20, 6, 11, 8]
# Array after Prefix Sum : 
# [10, 30, 36, 47, 55]
