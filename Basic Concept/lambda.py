from setuptools.command.alias import alias

print(list(map(lambda x: x**2, [1,2,3,4])))

print(list(filter(lambda a: a%2==0, [1,2,3,4])))

print([x**2 for x in [1,2,3,4] if x%2==0])


