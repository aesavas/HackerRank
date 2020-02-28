"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/triangle-quest-2/editorial
"""
# For this question, this is my best solution. It is not correct but I can do only this :D
for i in range(1, int(input())+1):
    print(*(list(range(1, i+1))+list(range(i-1, 0, -1))))


"""
There is a math trick in this question. I did not know that. If you do not know it, probably you can not do it.
Integers greater than 0 and less than 10:
(10**1)//9 = 1
(10**2)//9 = 11
(10**3)//9 = 111
(10**4)//9 = 1111
(10**5)//9 = 11111
(10**6)//9 = 111111
(10**7)//9 = 1111111
(10**8)//9 = 11111111
(10**9)//9 = 111111111
 
 and 

 1 * 1 = 1
 11 * 11 = 121
 111 * 111 = 12321
 1111 * 1111 = 1234321
 11111 * 11111 = 123454321
 111111 * 111111 = 12345654321
 1111111 * 1111111 = 1234567654321
 11111111 * 11111111 = 123456787654321
 111111111 * 111111111 = 12345678987654321

So, we can solve like this if we know this math trick
"""
for i in range(1, int(input())+1):
    print(int((10**i//9)**2))

"""
And also, another solution that the owner of the problem offer like this:
(I think, he is joking to everyone :D)
"""
for i in range(1, int(input())+1):
    print([1, 121, 12321, 1234321, 123454321, 12345654321,
           1234567654321, 123456787654321, 12345678987654321][i-1])
