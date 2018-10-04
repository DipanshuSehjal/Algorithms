# Problem Statement
A famous problem: Water Jug problem 

You are given a m litre jug and a n litre jug . Both the jugs are initially empty. The jugs don’t have markings to allow measuring smaller quantities. You have to use the jugs to measure d litres of water where d is less than n.
(X, Y) corresponds to a state where X refers to amount of water in Jug1 and Y refers to amount of water in Jug2
Determine the path from initial state (xi, yi) to final state (xf, yf), where (xi, yi) is (0, 0) which indicates both Jugs are initially empty and (xf, yf) indicates a state which could be (0, d) or (d, 0).

The operations you can perform are:

1. Empty a Jug, (X, Y)->(0, Y) Empty Jug 1
2. Fill a Jug, (0, 0)->(X, 0) Fill Jug 1
3. Pour water from one jug to the other until one of the jugs is either empty or full, (X, Y) -> (X-d, Y+d)


## External References:
https://www.geeksforgeeks.org/water-jug-problem-using-bfs/

https://www.eecis.udel.edu/~mccoy/courses/cisc4-681.10f/lec-materials/handouts/search-water-jug-handout.pdf

https://www.youtube.com/watch?v=qyiDvW9n4uc

https://www.youtube.com/watch?v=fWURLrQozHo

## BFS Algorithm
Jug problem is solvable iff gcd(a,b) divides target. Diophantine equation
with Extended Euclidean algorithm.

Make states on the fly!

The two water jug puzzle solved wth BFS:
We run breadth first search on the states and these states will be created
after applying allowed operations and we also use a dictionary to keep a record of visited states. 
Note that: This solution can also be achieved using depth first search