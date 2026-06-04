li=[i for i in range(10)]
print(li)
li= list(map(lambda x:x**2, li))
print(f"after map function: {li}")
li= list(filter(lambda x: x%2==0 and x%3==0,li))
print(f"after filter function: {li}")