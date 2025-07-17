# Binary Search
def binarySearch(arrLst, target):
    left, right = 0, len(arrLst) - 1
    while left <= right:
        mid = (left + right) // 2
        if arrLst[mid] == target:
            return mid
        if arrLst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 

arrLst = [10, 20, 21, 34, 78, 9, 5]
target = 9

arrLst.sort()
print(f"after sorted : {arrLst}")

result_bs = binarySearch(arrLst, target)

if result_bs == -1:
    print("Not Found!")
else:
    print(f"{target} found in arrLst[{result_bs}].")

# Output ---------------
# after sorted : [5, 9, 10, 20, 21, 34, 78]
# 9 found in arrLst[1].
