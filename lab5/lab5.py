######lab 5 #####
if __name__=="__main__":
    table = []
    file = open ("Table.txt","r")
    data =file.readlines()
    i=0
    for line in data:
        table.insert(i,[])
        line= line.replace("\n","")
        line= line.replace("\t","")
        for char in line:
            table[i].append(int(char))
    i=i+1
    
    file.close()
    print (table)
