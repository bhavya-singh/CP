#Author	:	Bhavya Singh
#Date	:	29-May-2020
#Name	:	Cutting Paper Squares

#THEORY:

Each time a piece of paper is cut it becomes 2 pieces, adding 1 to the total number of pieces. Therefore to make x pieces from 1 piece there needs to be x-1 cuts, so the final answer is (n*m)-1.

Interestingly, this principle means that the cuts can be made in any order and configuration.

#PROBLEM:

Mary has an n x m piece of paper that she wants to cut into 1 x 1 pieces according to the following rules:

She can only cut one piece of paper at a time, meaning she cannot fold the paper or layer already-cut pieces on top of one another.
Each cut is a straight line from one side of the paper to the other side of the paper. For example, the diagram below depicts the three possible ways to cut a  3 x 2 piece of paper:
example-cutting-squares.png
Given  n and m, find and print the minimum number of cuts Mary must make to cut the paper into n.m squares that are      1 x 1 unit in size.

Note : you have to write the complete code for taking input and print the result.

Input Format

A single line of two space-separated integers denoting the respective values of  n and m.

Constraints

1<=n, m<=109

Output Format

Print a long integer denoting the minimum number of cuts needed to cut the entire paper into  1 x 1 squares.

Sample Input

3 1
Sample Output

2
Explanation

Mary first cuts the  3 x 1 piece of paper into a 1 x 1 piece and a 2 x 1 piece. She then cuts the 2 x 1 piece into two 1 x 1 pieces:

cutting-paper-squares.png
Because it took her two cuts to get n x m=3 pieces of size  1 x 1, we print 2  as our answer.


#CODE

n, m = map(int, input().split())
print ( (m*n) - 1)

#Alternate:

import java.util.*;
public class Main
{
    public static void main(String []args)
    {
        Scanner sc=new Scanner(System.in);
        long r=sc.nextLong();
        long c=sc.nextLong();
        long i,j,k,count=0;
        /*if(r==1)
            count+=(c-1);
        else if(c==1)
            count+=(r-1);
        else
        {
         for(i=0;i<c;i++)
          {
            for(j=1;j<r;j++)
                count++;
          }
        }*/
        //count=c-1;
        //count+=((count+1)*(r-1));
        System.out.println((c*r)-1);
    }
}