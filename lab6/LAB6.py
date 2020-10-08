######lab 6 #####
if __name__=="__main__":
    table = []
    file = open ("table7.txt","r")
    data =file.readlines()
    
    i=0
    for line in data:
        table.insert(i,[])
        line= line.replace("\n","")
        line= line.replace("\t","")
        for char in line:
            table[i].append(int(char))
        i=i+1
    
    
    print (table)
    file.close()
    file = open ("states.txt","r")
    data =file.readlines()
    state=0
    for line in data:
        for char in line:
            #print(char)
            if char == '0':
                state = table[state][0]
            if char == '1':
                state = table[state][1]
            print(state)

    
    file.close()
    
