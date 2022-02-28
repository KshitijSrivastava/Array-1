
"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

https://leetcode.com/problems/diagonal-traverse/

Example:

Input:

[

[ 1, 2, 3 ],

[ 4, 5, 6 ],

[ 7, 8, 9 ]

]

Output: [1,2,4,7,5,3,6,8,9]
"""

"""
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        
        idx = 0
        output =  [0] * (m * n)
        
        up = True
        i = 0
        j = 0
        
        print(output)
        while i < m and j  < n:
            #print(output)
            
            if up:
                
                while i >= 0 and j < n:
                    output[idx] = int(mat[i][j])
                    idx += 1
                    
                    i -= 1
                    j += 1
                
                if j >= n:
                    j -= 1
                    i += 2
                    up = False
                elif i < 0:
                    i += 1
                    up = False
                    
                continue
            else:
                
                while i < m and j >= 0:
                    output[idx] = int(mat[i][j])
                    idx += 1
                    
                    j -= 1
                    i += 1
                
                if i >= m:
                    i -= 1
                    j += 2
                    up = True
                
                elif j < 0:
                    j += 1
                    up = True
                continue
                    
        # print("output = ", output)
        # print(mat)
        return output
                