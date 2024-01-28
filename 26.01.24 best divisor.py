#Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

#Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

#Input Format

#A single integer denoting .

#Constraints

#Output Format

#Print an integer denoting the best divisor of .

#Sample Input 0

#12
#Sample Output 0

#6
#Explanation 0

#The set of divisors of  can be expressed as . The divisor whose digits sum to the largest number is  (which, having only one digit, sums to itself). Thus, we print  as our answer.

#Submissions: 141
#Max Score: 10
#Difficulty: Easy
#Rate This Challenge:

    
#More
 
1
#!/bin/python3
2
​
3
import math
4
import os
5
import random
6
import re
7
import sys
8
​
9
​
10
​
11
if __name__ == '__main__':
12
    n = int(input().strip())
13
    l=[]
14
    for i in range(1,n+1):
15
        if(n%i==0):
16
            l.append(i)
17
    d={}
18
    for i in l:
19
        s1=0
20
        if(i<10):
21
            d[i]=i
22
​
23
        else:
24
            j=i
25
            while(i>0):
26
                s1+=i%10 
27
                i//=10 
28
            if s1 not in d:
29
                d[s1]=j
30
            else:
31
                if j<d[s1]:
32
                    d[s1]=j
33
​
34
    k=max(d.keys())
35
    print(d[k])
36
​
