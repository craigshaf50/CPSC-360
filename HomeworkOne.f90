program myprogram
    ! program for addition, subtraction, multiplication, and division
    implicit none
    ! type declarations
    real :: a, b, result 
    
    ! assigning values
    a = 40.0
    b = 10.0
    print *, 'a = ',a, ' b = ',b
    
    ! addition
    result = a + b
    print *, 'the sum of a plus b is: ', result
    
    ! subtraction 
    result = a - b
    print *, 'the difference of a minus b is: ', result
    
    ! multiplication
    result = a * b
    print *, 'the product of a miltiplied by b is: ', result
    
    ! division
    result = a / b
    print *, 'the quotient of a divided by b is: ', result
    
end program myprogram

    
