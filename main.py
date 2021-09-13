answer = sum([1, 2, 3])
print(answer)
arr = range(0,7)
print(arr)
print(range(0,7))
print(sum(range(0, 7)))

cubes = [1, 8, 27]
cubes.append(4 ** 3)
print(cubes) #should be [1, 8, 27, 64]

str = "cool"

print(str[-2])

words = ["dog", "house"]

for word in words:
  print(len(word))

def func(x):
  return x + 1

f = func
print(f(2) + func(2))

word = "chicken"
print(word[:-2]) #guess is chick
print(word[-2:]) #guess is en