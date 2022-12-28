
def binary_search(arr, n, l, r):
    if r >= l:
        m = (l+r)//2

        if arr[m] == n:
            print("element found at ",m)
        elif arr[m] < n:
            binary_search(arr, n, m+1, r)
        else:
            binary_search(arr, n, l, m-1)
    else:
        print("element not found")

binary_search([12,13,14,56,405],4505,0,4)