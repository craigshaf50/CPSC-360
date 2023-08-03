# Craig Shaffer
# CPSC 360
# 2-20-22
#
# Chapter 8: Programming Exercises 1-3

# 1. Rewrite the following pseudocode segment using a loop structure in the specified languages: Python
""" 
k = (j + 13) / 27 
loop: 
if k > 10 then goto out 
k = k + 1
i = 3 * k - 1 
goto loop 
out: . . . 
"""
j=1
i=1

k=(j+13)/27
while k<=10:
	k+=1
	i=3*k-1

# 2. Redo Programming Exercise 1, except this time make all the variables and constants floating-point type, 
# and change the statement k=k+1 to k=k+1.2
j=1.0
i=1.0

k=(j+13.0)/27.0
while k<=10.0:
	k+=1.2
	i=3.0*k - 1.0

# 3. Rewrite the following code segment using a multiple-selection statement in the following languages: Python
""" 
if ((k == 1) || (k == 2)) j = 2 * k - 1
if ((k == 3) || (k == 5)) j = 3 * k + 1
if (k == 4) j = 4 * k - 1
if ((k == 6) || (k == 7) || (k == 8)) j = k - 2 
"""
if k == 1 or k == 2:
    j = 2 * k - 1
elif k == 3 or k == 5:
    j = 3 * k + 1
elif k==4:
    j = 4 * k - 1
elif k == 6 or k == 7 or k == 8:
    j = k - 2 
# else:
#     print('k is not in range 1-8')