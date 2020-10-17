#Coding Mart O@$!m
if __name__=="__main__":
    
    file = open("identifier.txt","r")#identifier dfa table
    data = file.readlines()
    table1 = []        
    i = 0
    for line in data:
        temp = []
        x = line
        x = x.replace("\n","")
        x= x.replace("\t","")
        for char in x:
            if char != 'N':
                temp.append(int(char))
            else:
                temp.append(char)
        table1.append(temp)
    print("\n\tfianl table for identifier ")
    print(table1)
    finalstate1=table1[len(table1)-1]
    print(finalstate1)
    file.close()
    
    
    file = open("digits.txt","r")#digit dfa table
    data = file.readlines()
    table2 = []        
    i = 0
    for x in data:
        table2.insert(i,[])
        x= x.replace("\t","")
        x= x.replace("\n","")
        for val in x:
            table2[i].append(int(val))
        i=i+1
    print("\n\tfinal table for digit ")
    print(table2)
    finalstate2=table2[len(table2)-1]
    print(finalstate2)
    file.close()


    file = open("src1.txt","r") #input source file.
    seplist=['=','(','{',' ','}',')','[',']','==','!','!=','&&','|','||','>','>=','<','<=','\t','\n']
    keyword=['int','float','if','while','class','include','do','for','return','void','switch','break']
    table3=[]
    sep=[]
    string=""
    string1=""
    data2=file.readlines()
    for line in data2:
        print(line)
        for char in line:
            if(char in seplist):
                                 #backtrak logic
                string1=string1+char
                if(string1=="=="):
                    table3.append(string)
                    sep.remove('=')
                    sep.append(str("=="))
                    string=""
                    string1=""
                elif(string1==">="):
                    table3.append(string)
                    sep.remove('>')
                    sep.append(str(">="))
                    string=""
                    string1=""
                else:
                    table3.append(string)
                    sep.append(str(char))
                    string=""
                
                
            else:
                string=string+char
    
    table3.append(string)
    print(table3)
    print(sep)
                            #for token identification read lexems from list
    q=0
    for lexem in table3:
        statech=0
        statedig=0
        for char in lexem:
            if((ord(char)>=65 and ord(char)<=96) or (ord(char)>=97 and ord(char)<=122) or char=='_'):
                statech=table1[statech][0]
            elif((ord(char)>=48 and ord(char)<=57)):
                statedig=table2[statedig][0]
            else:
                statech=table1[statech][3]
                
            if statech == 'N':
                print(lexem , 'Invalid token')
                break;
            

        if(statech in finalstate1 and statedig in finalstate2):
            print(lexem,' is invalid token')
        elif statech in finalstate1:
            if(lexem in keyword):
                print(lexem,' is a keyword')
            else:
                print(lexem,'is an identifier token')
        
        else:
            if statedig in finalstate2:
                print(lexem,' is a digit token')
        print(sep[q],' is a seperator')
        q=q+1
  
   
    file.close()
