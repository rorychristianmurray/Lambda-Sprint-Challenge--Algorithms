# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0 # O(1)
    while (a < n * n * n):# O(n * n * n = n^3)
      a = a + n * n # O(1)
```

This gives O(n^3 + 1 + 1) = O(n^3)

```
b)  sum = 0 # O(1)
    for i in range(n): # O(n) n increases, we increase by i operations
      j = 1 # O(1)
      while j < n: # O(n)
        j *= 2 O(1)
        sum += 1 O(1)
```

This gives
O(1) + O(n + 1)(O(n + 2)) = O(n^2 + 3n + 3)

= O(n^2)

```
c)  def bunnyEars(bunnies):
      if bunnies == 0: # O(1)
        return 0 O(1)

      return 2 + bunnyEars(bunnies-1) # O(n)
```

This is an example of recursion. A call to bunnyEars giving it bunnies - 1 will function as a loop in big O, and means that as the length of bunnies increases, the amount of operations will increase linearly by n. Inside the recursive function, we only have O(1) terms, giving the big O complexity as:

O(n)

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

## Answer

## Understand

n story building means list of length n

There is a value f we are looking for that dictates behavior
for list = building, we want to find the floor where we minimize the sum of dropped + broken eggs

## Plan

inputs: list of length n (the building)
output: int f (floor where sum is minimized)
assumptions: n (or f) cant be negative
edge cases:
similar problems: search functions like iterative and binary search
base cases:
f = 0 (as a starting point)
min = 0 (will track the min value we are looking at)
max = len(building) (will track the max value we are looking at)
