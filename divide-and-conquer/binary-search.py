import math

# TC: O(logn) bc in the worst case, we are cutting the list of length n into half until we theres no element
def binarySearch(list, target):
    left = 0
    right = len(target) - 1

    while(True):
        if(left < right):
            return -1

        mid = math.floor(left + right)/2

        if(list[mid] == target):
            return mid
        
        elif(list[mid] > target):
            right = mid - 1

        else:
            left = mid + 1
