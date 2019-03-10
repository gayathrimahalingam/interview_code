# given two sorted arrays find the median of these two sorted arrays (combined)

'''
solution: Median is the middle element
1. divide the arrays as left part and right part
2. criteria for the left part and right part (includes both A and B's left part)
    a. len(left_part) = len(right_part)
    b. max(left_part) <= min(right_part)
3. the median will be (max(left_part) + min(right_part)) / 2

NOTE: array A is split at i th position and array B is split at j th position
    i + j = m - i + n - j  (or m-i+n-j+1) m = size(A) n = size(B)
    if n >= m, i = 0 to m and j = (m+n+1)/2 - i
    and
    B[j-1] <= A[i] and A[i-1] <= B[j]

'''
# Time Complexity: O(log(min(m,n)))

import os

def median(A, B):
    m = len(A)
    n = len(B)

    if m > n:
        # switch them
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin = 0
    imax = m 
    half_len = (m + n + 1) / 2
    while (imin <= imax):
        i = (imin + imax) / 2
        j = half_len - i 
        if i < m and B[j-1] > A[i]:
            # i is too small, increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect
            if i == 0:
                max_of_left = B[j-1]
            elif j == 0:
                max_of_left = A[i-1]
            else:
                max_of_left = max(A[i-1], B[j-1])

            if (m+n)%2 == 1:
                return max_of_left

            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])
            
            return (max_of_left + min_of_right)/2.0
    