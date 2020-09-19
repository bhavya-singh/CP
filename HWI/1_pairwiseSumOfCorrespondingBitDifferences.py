#Author	:	Bhavya Singh
#Date	:	29-May-2020
#Name	:	Pair wise sum of corresponding bit differences

#THEORY:

A Simple Solution is to run two loops to consider all pairs one by one. For every pair, count bit differences. Finally return sum of counts. Time complexity of this solution is O(n2).

An Efficient Solution can solve this problem in O(n) time using the fact that all numbers are represented using 32 bits (or some fixed number of bits). The idea is to count differences at individual bit positions. We traverse from 0 to 31 and count numbers with i’th bit set. Let this count be ‘count’. There would be “n-count” numbers with i’th bit not set. So count of differences at i’th bit would be “count * (n-count) * 2”, the reason for this formula is as every pair having one element which has set bit at i’th position and second element having unset bit at i’th position contributes exactly 1 to sum, therefore total permutation count will be count*(n-count) and multiply by 2 is due to one more repetition of all this type of pair as per given condition for making pair 1<=i,j<=N.

Below is implementation of above idea.

#PROBLEM:

We define d(X, Y) as number of different corresponding bits in binary representation of X and Y. For example, d(3, 9) = 2, since binary representation of 3 and 9 are 0011 and 1001, respectively. The first and the third bit differ, so f(3, 9) = 2.

You are given an array of N positive integers, A1, A2 ,…, AN. Find sum of d(Ai, Aj) for all pairs (i, j) such that 1 = i, j = N. Return the answer modulo 10^9+7.

For example,

A= [3,7,9]

We return

  d(3,3) + d(3,7) + d(3,9)
+ d(7,3) + d(7,7) + d(7,9)
+ d(9,3) + d(9,7) + d(9,9)    
  0 + 1 + 2
+ 1 + 0 + 3
+ 2 + 3 + 0
= 12
Thus, we return 12


#CODE

class Solution:
    def cntBits(self, A):
        result = 0
        for i in range(0, 32):
            count = 0
            for j in range(0, len(A)):
                if ( A[j] & (1<<i) ):
                    count += 1
            result += count*(len(A)-count)*2
        return result