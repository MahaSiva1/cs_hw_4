"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Maha Sivasubramanian and <FULL NAME>, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: ms94594
UT EID 2:
"""


def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        # simplest cast: []
        # target was 0, then we would return True, otherwise False
        return target == 0
        # next simple case: [1]
        # target would have to be 1, recursively solve this problem, after chooseing the number
        # or not choosing the number

    #possible choices
    # choose the number, or don't choose the number, and update our target
    target -= nums[start]
    if group_sum(start + 1, nums, target):
        return True
    #undo our choice
    target += nums[start]
    #other choice, which was not choosing the number
    return group_sum(start + 1, nums, target)


def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    if 6 in nums:
        target = target - 6
        target = target - nums[start]
        if group_sum(start + 1, nums, target):
            return True
        target = target + nums[start]
        return group_sum(start + 1, nums, target)
    else:
        target = target - nums[start]
        if group_sum(start + 1, nums, target):
            return True
        target = target + nums[start]
        return group_sum(start + 1, nums, target)



def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0

    target = target - nums[start]
    if group_no_adj(start + 2, nums, target):
        return True

    target = target + nums[start]
    #other choice, which was not choosing the number
    return group_no_adj(start + 1, nums, target)



def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    target = target - nums[start]
    if group_sum_5(start + 1, nums, target):
        return True
    if not nums[start] % 5 == 0:
        target = target + nums[start]
    return group_sum_5(start+1,nums,target)




def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    #target = target - nums[start]
    count = 1
    n = nums[start]
    for i in range(start+1, len(nums)):
        if nums[i] == nums[i - 1]:
            #print n
            count += 1
        else:
            break
    if count>1:
        target -= count * n
        if group_sum_clump(start + count, nums, target):
            return True
        target = target + count * n
        return group_sum_clump(start + count, nums, target)
    else:
        target = target - nums[start]
        if group_sum_clump(start + 1, nums, target):
            return True
        target = target + nums[start]
        return group_sum_clump(start + 1, nums, target)




    #if group_sum(start + 1, nums, target):
        #return True
    #this is undoing the step if not true, when do we want to not undo?
    # when there is clump of numbers w the same value
    ##target = target + nums[start]
    ##return group_sum(start + 1, nums, target)


def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    sum1 = []
    sum2 = []
    start = 0
    val = split_helper(nums, start, sum1, sum2)
    return val

def split_helper(nums, start, sum1, sum2):
    #put it into sum1
    '''
    sum1.append(nums[1])
    do the recursion 
    if false-> take it out of sum1 
    add nums[start] to sum2
    '''
    if start >= len(nums):
        return sum(sum1) == sum(sum2)
    sum1.append(nums[start])
    if split_helper (nums, start + 1, sum1, sum2):
        return True
    sum1.pop()
    sum2.append(nums[start])
    val1 =  split_helper(nums, start + 1, sum1, sum2)
    sum2.pop()
    return val1






def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    sum1 = []
    sum2 = []
    start = 0
    val = odd_10_helper(nums, start, sum1, sum2)
    return val

def odd_10_helper(nums, start, sum1, sum2):
    """helper function that the odd_10 function will use"""

    if start >= len(nums):
        return sum(sum1) % 2 != 0 and sum(sum2) % 10 == 0
    sum1.append(nums[start])
    if odd_10_helper(nums, start + 1, sum1, sum2):
        return True
    sum1.pop()
    sum2.append(nums[start])
    val1 = odd_10_helper(nums, start + 1, sum1, sum2)
    sum2.pop()
    return val1



def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    # two different sums you need to keep track of
    sum1 = []
    sum2 = []
    start = 0
    val = split53_help(nums, start, sum1, sum2)
    return val

def split53_help(nums, start, sum1, sum2):
    """helper function that split53 will use"""
    if start >= len(nums):
        #return (sum(sum1) == sum(sum2)) and (sum(sum1) % 5 == 0 and sum(sum2) % 3 == 0)
        return sum(sum1) == sum(sum2)
    if nums[start] % 5 == 0:
        sum1.append(nums[start])
        if split53_help(nums, start + 1, sum1, sum2):
            return True
        sum1.pop()

    elif nums[start] % 3 == 0:
        sum2.append(nums[start])
        val1 = split53_help(nums, start + 1, sum1, sum2)
        sum2.pop()
        return val1
    else:
        sum1.append(nums[start])
        if split53_help(nums, start + 1, sum1, sum2):
            return True
        sum1.pop()

        sum2.append(nums[start])
        val2 = split53_help(nums, start + 1, sum1, sum2)
        sum2.pop()
        return val2
    return False
