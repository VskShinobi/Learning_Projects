"""def LargeSmallSum(length,arr)

The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest largest element from the even positions and second smallest from the odd position of given ‘arr’

Assumption:

All array elements are unique
Treat the 0th position a seven
note

Return 0 if array is empty
Return 0, if array length is 3 or less than 3
Example

Input

arr:3 2 1 7 5 4

Output

7

Explanation

Second largest among even position elements(1 3 5) is 3
Second largest among odd position element is 4
Thus output is 3+4 = 7"""

def LargeSmallSum(length,arr):4

    odd = []
    even = []
    for i in range(length):
        if i % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])

    even = sorted(even)
    odd = sorted(odd)
    print(even[len(even)-2] + odd[len(odd)-2])




length = int(input())
arr = list(map(int, input().split()))
LargeSmallSum(length,arr)
