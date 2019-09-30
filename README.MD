The following is a series of projects completed as part of Udacity Nanodegree program in Data Structures and Algorithms.
This is the first project, which is introduction to problem solving and basics of python

All tasks also involve reading data from the two csv files which account for the bulk of time and I have not considered those for calculating Big O for the algorithm.

C denotes the length of calls list for the worst case
T denotes the length of texts list for the worst case

Task 0:
Big O time : O(1)

Task 1:
Big O time : O(C+T)

Task 2:
For this task O(U) where U denotes the length of dictionary containing unique numbers and the time spent on the phone 
Big O time : O(C) + O(U)
We can safely ignore the time for iterating through the dictionary for individuals phone numbers because len(U) is a fraction of len(C) and we drop constants for Big O. 
Big O time : O(C)

Task 3:

Big O time : O(C) + O(sorttime)
If S denotes the length of the list with unique numbers from Bangalore. Found out that python uses merge sort which has a time complexity of O(SLogS) for the worst case

Big O time : O(C+SLogS)

Task 4:

Big O time : O(C + T + sorttime + weedoutduplicatestime)

If S denotes the length of the list with telemarketers from Bangalore. Merge sort will be used which has a time complexity of O(SLogS) for the worst case

O(weedout) takes the time of O(SLogN) where N is the length of non telemarketers

Big O time : O(C) + O(T) + O(SLogS) + O(SLogN)
