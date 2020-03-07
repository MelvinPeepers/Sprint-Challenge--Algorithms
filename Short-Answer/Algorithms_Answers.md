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
