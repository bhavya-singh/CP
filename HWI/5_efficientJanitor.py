#Author	:	Bhavya Singh
#Date	:	30-May-2020
#Name	:	Lcuky Number

#PROBLEM:

The janitor of a high school is insanely efficient. By the end of the day, all of the waster from the trash cans in the school has been shifted into plastic bags which can carry waster weighting between 1.01 pounds and 3.00 pounds.

All of the plastic bags must be dumped into the trash cans outside the school. The janitor can carry at most 3.00 pounds at once.

One trip is described as selecting a few bags which together don't weigh more than 3.00 pounds, dumping them in the outdoor trash can and returning to the school. The janitor wants to make minimum number of trips to the outdoor trash can.

Given the number of plastic bags, n and the weights of each bag, determine the minimum number of trips if the janitor selects bags in the optimal way.

For example, given n=5, plastic bags weighing weights [1.01, 1.99, 2.5, 1.5, 1.01], the janitor can carry all of the trash out in 3 trips: [1.01+1.99, 2.5, 1.5+1.01]

Constraints

1 <= n <= 1000
1.01 <= weight <= 3.0

#CODE

n = int(input())
inp = list(map(float, input().split()))
inp.sort()
left = 0
trips = 0
i = len(inp)-1
if n==2 and sum(inp)<=3.00:
    print("1")
elif n == 2 and sum(inp)>3.00:
    print("2")
else:
    for i in range(len(inp)-1, -1, -1):
        if inp[i] > 1.99:
            trips += 1
        if inp[i] <= 1.99:
            if inp[left]+inp[i] <= 3.00:
                left += 1
            trips += 1
        if left >= i:
            break
    print(trips)