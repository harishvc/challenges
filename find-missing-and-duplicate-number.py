'''
Question:
There are numbers from 1 to N in an array. out of these, one of the number gets duplicated and one is missing. 
The task is to find out the duplicate number. Conditions: you have to do it in O(n) time without using any auxilary space (array, bitsets, maps etc..).

Source:
http://www.geekinterview.com/question_details/39488

Solution:
mark the missing number as M and the duplicated as D
1) compute the sum of regular list of numbers from 1 to N call it RegularSum
2) compute the sum of your array (the one with M and D) call it MySum
now you know that MySum-M+D=RegularSum
this is one equation.
the second one uses multiplication:
3) compute the multiplication of numbers of regular list of numbers from 1 to N call it RegularMultiplication
4) compute the multiplication of numbers of your list  (the one with M and D) call it MyMultiplication
now you know that MyMultiplication=RegularMultiplication*D/M
at this point you have two equations with two parameters, solve and rule!

'''
