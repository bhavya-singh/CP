#Author	:	Bhavya Singh
#Date	:	23-May-2020
#Name	:	Check if all enemies are killed with bombs placed in a matrix


#THEORY:

The given problem can be solved by the following approach:

Get the character Matrix
Traverse to find all bomb indices in the matrix
For each bomb found, see if any enemy is present in its vertical or horizontal direction. If present kill that enemy, i.e. change E to X
After all traversals, check if any enemy is present in the matrix or not.
Print Yes if all enemies are killed, else print No.

#PROBLEM:

Given a Character matrix as input, the task is to check whether all the enemies are killed or not based on below conditions:

1. The matrix can contain 3 characters
X –> Denotes the War area.
B –> Denotes the bomb.
E –> Denotes the Enemies.

2. Bomb ‘B’ can blast in only horizontal and vertical directions from one end to another.

3. If all enemies are killed by the present bombs, print Yes, else print No

Examples:

Input: matrix =
XXEX
XBXX
XEXX
XXBX 
Output: Yes

Input: matrix =
XXEX
XBXX
XEXX
XXXX
Output: No


#CODE

def Kill_Enemy(s, row, col): 
    i, j, x, y = 0, 0, 0, 0; 
  
    # Loop to evaluate the Bomb 
    for i in range(row): 
        for j in range(col): 
              
            # Check if this index is a bomb 
            if (s[i][j] == 'B'): 
  
                # Kill all enemies 
                # in horizontal direction 
                for x in range(row): 
                    if (s[x][j] != 'B'): 
                        s[x][j] = 'X'; 
  
                # Kill all enemies 
                # in vertical direction 
                for y in range(col): 
                    if (s[i][y] != 'B'): 
                        s[i][y] = 'X'; 
  
    # All bombs have been found 
  
    # Check if any enemy is still present 
    for i in range(row): 
        for j in range(col): 
  
            if (s[i][j] == 'E'): 
  
                # Since an enemy is present 
                # Return 0 denoting No as output 
                return 0; 
  
    # Since all enemies are killed 
    # Return 1 denoting Yes as output 
    return 1; 
  
# Driver Code 
if __name__ == '__main__': 
  
    # Get the input matrix 
    s = [['X','X','E','X'], 
        ['X','B','X','X'], 
        ['X','E','X','X'], 
        ['X','X','B','X']] 
  
    # Calculate Rows and columns of the String 
    row = len(s); 
    col = len(s[0]); 
  
    # Check if all enemies will be killed or not 
    if (Kill_Enemy(s, row, col) == 1): 
        print("Yes"); 
    else: 
        print("No"); 