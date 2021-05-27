def my_fib(num1):
#  0 1 1 2 3 5 8 13 21
    c = 0
    for i in range (0,(num1+1)):
        if i == 0:
            print(0)
        elif i == 1:
            print(i)
            c += i
            print(c)
        else:
            c += (i - 1)   
            print(c) 

            





#main function
x = int(input("n ")) 
finaf_fib = my_fib(x) 
 