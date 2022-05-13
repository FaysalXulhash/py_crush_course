guests = ['Faysal', 'Sahin', 'Mahir']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()

print(f"{name}, please come to dinner.")

# here guests[3] ,[4] will produce error as they weren't defined

"""name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")
"""

#Here we will fix the error

guests.insert(3,'rabbi')
guests.insert(4,'mira')

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")