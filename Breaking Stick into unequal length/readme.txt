Problem Statement

Write an (efficient!) Python program that, given a stick of integer length N, breaks it up into smaller sticks of integer but all un-equal lengths. For example: For N = 10, one possibility is (1,2,3,4). However (1,1,1,3,4) is not valid due to the repeated 1s.
How many unique ways are there to break up the stick of length N? Please note that permutations of a break-up are not to be counted, i.e., you are to count, (1,2,3,4) and (2,1,3,4) as a single breakup.  
Plot the performance of your program scale with N? For this, run your program multiple times and take the minimum time taken for a given value of N for the plot. You can use the value range of N = 10,20,40,80, 100, 200, 400, 800, 1000, 2000, 4000, 8000, 10000 and so on.
What are the Big-O time and space complexities of your algorithm?
Challenge for BONUS Marks: Write a Python program that, given a square with side length N breaks it into squares of integer but all unequal lengths