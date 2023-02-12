def Tupplize(listy):
    for i in listy:
        listy = (i, listy)

def QuickSortT(listy: list[tuple]):
    # Want to retain the original index of each list

    # Base Case
    if listy == []:
        return []

    index: int = 0               
    pivot: tuple = listy[index]    
    small: list[tuple] = []              
    large: list[tuple] = []
    for items in listy[index+1:]:
        if pivot[1] < items[1]:
            small.append(items)
        else: 
            large.append(items)

    return QuickSortT(small) + [pivot] + QuickSortT(large)

# Directly Modifying Lists
def Normalize(listy):
    for i in range(len(listy)):
        listy[i] -= listy[0]


def FindGreatIndex(listy, targy):
    for i in range(len(listy)):
        if targy <= listy[i]:
            return i


def twoSum(nums: list[int], target: int) -> list[int]:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # BREAKING DOWN THE PROBLEM
    # Only started writing code, when we know what to do


    Snums: list[tuple] = QuickSortT(nums)
    # Property Added: the left item will be smaller than the right item 

    #Normalize(Snums)
    #target -= Snums[0]
    # Property Added: Every number is 0 or above + normalized target

    #Snums[:FindGreatIndex(Snums, target)]
    # Property Added: No numbers is >=target

    # Next step: How to traverse the list
    # WE STILL HAVE THE SAME PROBLEM LOL

    # if the arrows ever meet, there is no soln
    # for i in range(len(Snums)):
    
    a: int = 0
    b: int = len(Snums)-1
    while(a < b):
        if Snums[a][1] + Snums[b][1] == target:
            return [Snums[a][0], Snums[b][0]]
        elif Snums[a][1] + Snums[b][1] > target:
            b -= 1
        elif Snums[a][1] + Snums[b][1] < target:
            a += 1

#       for i in range(len(nums)):
#           for j in range(i + 1, len(nums)):
#               if nums[i] + nums[j] == target:
#                   return [i,j]

print(twoSum([2,7,11,15], 9))
