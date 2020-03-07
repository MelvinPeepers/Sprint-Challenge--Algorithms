#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

<!-- Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following: -->

## Exercise I

a) a = 0 # single operation runtime O(1)
while (a < n _ n _ n): # for loop O(n) no nested loops
a = a + n \* n #

# I believe this is an O(n) runtime

b) sum = 0 # single operation runtime O(1)
for i in range(n): # for loop O(n) with a nested for loop
j = 1
while j < n: # nested for loop so we multiple log(n) ( logn \* O(n) = log(n)) )
j \*= 2
sum += 1

# I believe this is an log(n) runtime (formatting gets messed up when saving)

c) def bunnyEars(bunnies):
if bunnies == 0: # O(n)
return 0

      return 2 + bunnyEars(bunnies-1) # single operation runtime O(1)

# I believe this is an O(n) runtime

## Exercise II

<!-- # almost missed this -->

<!-- Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution. -->

I would start with a Binary Search which allows us to eliminate a bunch of option. Binary Search has a runtime of O(logn)
With a Binary Search you'll start in the middle. If the element is smaller then the middle, it can only be on the left of the array. ELSE it's on the right.
So with this in mind, we could drop the egg in the middle floor, and if it does break, then perform another egg drop at another middle point that's smaller (closer to you as there is less of a drop). If the egg doesn't break, you can drop the egg farther from you (in the middle floor between your first drop the farthest floor).
