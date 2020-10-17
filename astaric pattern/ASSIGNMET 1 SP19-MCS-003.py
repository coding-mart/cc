if __name__=="__main__":

    #astraic pattern
    #Coding Mart O@$!m
    '''
    enter the postive number: 5
    *****
    **  *
    * * *
    *  **
    *****
    '''
    #please remove comments and run the task
    #get number from user.
    number = int(input("enter the postive number"))
    #this if chek number must be grate than zero. their else is at the end of code.
    if (number >0 ):
        #task 1
        #using for loop
        
        #this loop is use for row,
        for row in range(1,number+1,1):
            #this loop use for column.
            for col in range(1,number+1,1):
                #if any condition true in below if then print star.
                if(row == 1 or row == number or col == 1 or col == number or row == col):
                    print("*",end = "")
                #if not any above condition true then print space.
                else:
                    print(" ",end = "")
            #this print \r return to starting position
            print("\r")
        

        #task 2
        #comment task 1 then uncomment tsak 2 and run.
        #using while loop
        '''
        #initialize row with one
        row=1
        #initialize column with one
        col=1
        #this while loop control the rows
        #outer loop
        while(number+1 > row):
            #this while loop control the column
            #inner loop
            while(number+1 > col):
                #if any condition true in below if then print star.
                if(row == 1 or row == number or col == 1 or col == number or row == col):
                     print("*",end = "")
                #if not any above condition true then print space.
                else:
                    print(" ",end = "")
                 #one incremrt in column   
                col=col+1
                #this print \r return to starting position
            print("\r")
            #one increment in row
            row=row+1
            #again intilize column with one for next itration of row
            col=1
        '''    
    #if the number is zero or less then zero then this else will execute.
    else:
        print("number is zero or negative")
        
    
