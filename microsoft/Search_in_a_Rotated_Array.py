"""
Given a sorted and rotated array A of N distinct elements which is rotated at some point, 
and given an element key. The task is to find the index of the given element key in the array A.

Example 1:

Input:
N = 9
A[] = {5, 6, 7, 8, 9, 10, 1, 2, 3} // {8, 9, 10, 1, 2, 3, 5, 6, 7}
key = 10
Output:
5
Explanation: 10 is found at index 5. in O(log(n))
"""

def search(arr : list, low : int, target : int):
          high = len(arr) - 1
          while low <= high:
            
            mid = (low + high) // 2
            print(arr, low, high, mid)
            if arr[mid] == target:
              return mid
            # Check if the left half is sorted
            if arr[low] <= arr[mid]:
              # Check if the target is in the left half
              if arr[low] <= target <= arr[mid]:
                high = mid - 1
              else:
                print("30")
                low = mid + 1
            # The right half must be sorted
            else:
              # Check if the target is in the right half
              if arr[mid] <= target <= arr[high]:
                low = mid + 1
              else:
                high = mid - 1
          return -1

print(search([5, 6, 7, 8, 9, 10, 1, 2, 3],0,10))