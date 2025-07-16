def linearSearch(arrLst, target):
    for i in range(len(arrLst)):
        if arrLst[i] == target:
            return i
    return -1

arrLst = [10, 20, 21, 34, 78, 9, 5]
target = 9

result_ls = linearSearch(arrLst, target)

if result_ls == -1:
    print("Not Found!")
else:
    print(f"{target} found in arrLst[{result_ls}].")

# Output ---------------
# 9 found in arrLst[5].
