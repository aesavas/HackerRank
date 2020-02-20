"""
    author : Ali Emre SAVAS
    Link : 
"""


thickness = int(input())  # This must be an odd number
c = 'H'
# Top Cone
for i in range(thickness):
    # 1)rjust  2)ljust
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    # 1)center 2)center
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))  # center

# Bottom Pillars
for i in range(thickness+1):
    # 1)center 2)center
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    # 1)rjust 2)ljust 3)rjust
    print(((c*(thickness-i-1)).rjust(thickness)+c +
           (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
