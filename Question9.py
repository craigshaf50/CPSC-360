x = 7
y = 10
if x > 3 or y < 30:
    print('something')

#This is an example of short circuiting because the x>3.
#Since x (7) is greater than 3, python doesn't even evaluate
#y<30. This is because python has short circuit evaluation.
#Evaluating y<30 won't affect the outcome because an or statement 
#is always true if either of the terms is true.