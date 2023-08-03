'''
j = -3;

for (i = 0 to i = 3 ; i ++ ) {

       switch  ( j + 2 ) {

           case 3:

           case 2: j -- ; break;

           case 0: j += 2 ; break;

           default: j = 0;

       }

       if ( j > 0 ) break;

       j = 3 - i

}
'''
j=-3
for i in range(0,4):
    j=j+2
    if j==3:
        j=3#this case was blank, just redifining variable to prevent errors
    elif j==2:
        j=j-1
        break
    elif j==0:
        j=j+2
        break
    else: #default case
        j=0
    if j>0:
        break
    j=3-i
