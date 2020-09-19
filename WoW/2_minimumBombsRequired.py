#Author	:	Bhavya Singh
#Date	:	23-May-2020
#Name	:	Minimum Bombs Required


#THEORY:

We can make a constructive way to kill all aliens. Since everyone either moves to the left or to the right, we have to make sure that all the even positions are attacked, once at the start to injure aliens and the other time at the end. When we attack aliens at the even positions first time they move to the odd position buildings, so attack them at odd to kill all the previous even positions and injure the odd position aliens. The odd position aliens get injured and will move to the even position, so attack them at the even at the end to kill them.
The number of ways will be n/2 + n/2 + n/2 which is n + n/2.

#PROBLEM:

There are aliens in n buildings (minimum of 1 in each) and you have to kill all of them minimum number of bombings. Buildings are numbered as 1 – n. Aliens in a bombed building gets injured at the first bombing and die at the second. When a building is bombed for the first time, aliens in that building try to escape to the nearest building (for first building the nearest one is the second one and for nth building it is n-1). Calculate the minimum number of bombs required to kill all the aliens and the order of bombings.
Example:

Input: 3
Output: 4 
        2 1 3 2 
Explanation: Minimum number of bombs required are 4.
             First bomb the 2nd building, aliens 
             will  move to 1st or 3rd to save
             themselves. Then bomb at 1st building, 
             if some aliens have moved from 2nd 
             building to 1st they will be killed and
             the 1st building aliens will be injured,
             and they will move to the 2nd building
             as it is nearest to them. Now, bomb at
             the 3rd building to kill aliens who 
             moved from the 2nd building to 3rd and
             injure 3rd building aliens so they move 
             to 2nd building as it is nearest to them.
             Now, bomb at the 2nd building again and
             all aliens who moved from 1st or 3rd
             building will be killed.

Input: 2
Output: 3
        2 1 2  

#CODE

"""Python program to find number of 
bombings required to kill all aliens"""

# function to print where to shoot 
def bomb_required(n): 
	
	# no. of bombs required 
	print(n+n // 2) 
	
	# bomb all the even positions 
	for i in range(2, n + 1, 2): 
		print(i, end = " ") 
	
	# bomb all the odd positions 
	for i in range(1, n + 1, 2): 
		print(i, end = " ") 
	
	# bomb all the even positions again 
	for i in range(2, n, 2): 
		print(i, end = " ") 

# Driver Code		 
bomb_required(3) 
