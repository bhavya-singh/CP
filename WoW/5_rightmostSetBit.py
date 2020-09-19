#Author	:	Bhavya Singh
#Date	:	23-May-2020
#Name	:	First set bit from right


#PROBLEM:

Given an integer an N. The task is to print the position of first set bit found from right side in the binary representation of the number.

Input:
The first line of the input contains an integer T, denoting the number of test cases. Then T test cases follow. The only line of the each test case contains an integer N.

Output:
For each test case print in a single line an integer denoting the position of the first set bit found form right side of the binary representation of the number. If there is no set bit print "0".

Constraints:
1 <= T <= 200
0 <= N <= 106

Example:
Input:
2
18
12

Output:
2
3

Explanation:
Testcase 1: Binary representation of the 18 is 010010, the first set bit from the right side is at position 2.

#CODE

def first_set_bit_right( n ):

    INT_SIZE = 32

    pos = 1

    for j in range( INT_SIZE ):

        if not ( n & 1<<j ):

            pos += 1

        else:

            break

    if pos<=32:

        return pos

    else:

        return 0



T = int(input())

for i in range(T):

    N = int(input())

    print( int(first_set_bit_right( N )) )