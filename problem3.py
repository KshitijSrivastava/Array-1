

"""
## Problem 3
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

https://leetcode.com/problems/spiral-matrix/

Example 1:

Input:

[

[ 1, 2, 3 ],

[ 4, 5, 6 ],

[ 7, 8, 9 ]

]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:

[

[1, 2, 3, 4],

[5, 6, 7, 8],

[9,10,11,12]

]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""



class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        output = []
        
        nrows = len(matrix)                         #count the number of rows
        ncols = len(matrix[0])                      #count the number of columns
        
        left = 0                                    #left pointer
        right = ncols - 1                           #right pointer
        
        top = 0                                     #top pointer
        bottom = nrows - 1                          #bottom pointer
        
        direction = "r"                             #initial direction set to right
        
        i = 0                                       #initial pointers
        j = 0
        
        while left <= right and top <= bottom:      #while all pointers do not cross
            
            if direction == "r":
                
                while j <= right:                  #keep travering right until hit right ptr
                    output.append( matrix[i][j] )
                    
                    if j == right:                  #if reach the last node then break
                        break
                    j += 1
                
                i += 1                              #chnage the pointer to bottom row
                top += 1                            #top column has traversed, update it
                direction = "d"                     #change the direction
                continue
            
            elif direction == "d":
                while i <= bottom:                 #keep traversing bottom until you reach bottom
                    output.append( matrix[i][j] )
                    
                    if i == bottom:                #if the pointer reaches the bottom, break
                        break
                    i += 1
                
                j -= 1                             #chenge the pointer
                right -= 1                         #right most column has been updated, reduce it
                direction = "l"                     #change the direction to right
                continue
            
            elif direction == "l":
                while j >= left:                    #continue left till you reach left ptr 
                    output.append( matrix[i][j] )
                    
                    if j == left:                   #if you reach the left ptr break
                        break
                    
                    j -= 1
                i -= 1                              #Make pointer upwards
                bottom -= 1                         #update the bottom ptr since bottom row traversed
                direction = "u"                     #change the direcion pointer
                continue
                
            elif direction == "u":                  #if the direction is up
                
                while i >= top:                     #keep going up till you reach top ptr
                    output.append(matrix[i][j])
                    if i == top:                    #if reach the top ptr, break
                        break
                
                    i -= 1
                j += 1                              #go right, so update the pointer
                left += 1                           #left most col travered, so update it
                direction = "r"                     #change the direction to right
                
        
        return output            
            
            
                
        