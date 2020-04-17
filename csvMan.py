import csv

def printExcel(ssRow,posRow,tmpRow):
    with open('tmp.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(ssRow)
        spamwriter.writerow(posRow)
        spamwriter.writerow(tmpRow)

def printPlayers(player):
    with open('tmp.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')        
        spamwriter.writerow(player)


def correctTheDNF():
    with open('gr1.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')    
            with open('correct.csv', 'w', newline='') as f:                
                for row in spamreader: 
                    #print(str(len(row)) + str(row))                   
                        spamwriter = csv.writer(f, delimiter=',')                               
                        if len(row) > 0:
                            if(row[0].isdigit()):
                                addValue = 0
                                lastRow = int(row[0])                             
                                spamwriter.writerow(row) 
                                #print(row)                                               
                            elif row[0] == "":
                                addValue +=1                                  
                                row[0] = str(lastRow + addValue)
                                #print(row)
                                spamwriter.writerow(row)   
                            else: 
                                #print(row)                           
                                spamwriter.writerow(row)  
                        else:    
                            #print(row)                        
                            spamwriter.writerow(row)      
                          

def countPlayers():
    count = 0
    foundOnce = False
    with open('gr1.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')                    
            for row in spamreader:
                if len(row) > 0:                                           
                    if "Pos" == row[0]:                        
                        if(foundOnce):                            
                            return count

                        count = 0
                        foundOnce = True
                    else:
                        count +=1                      
                    
correctTheDNF()                
nop = countPlayers() #number of players
print("Players are " + str(nop - 1))        
with open('gr1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    counter = 0
    ssRow = []
    posRow = []

    tmpRow = []

    loopare = 0
    for row in spamreader:
        if len(row) > 0:
            if "SS1 " in row[0]:
                loopare +=1                
            if len(row[0]) > 2  and 'S' == row[0][0] and 'S' == row[0][1]:
                ssRow.append(row[0])
                for x in range(6):
                    ssRow.append("") 
                if loopare == 2: 
                    ssRow.append("")             
            elif "Pos" == row[0]:
                for x in row:
                    posRow.append(x)
                posRow.append("")        
            
    

    printExcel(ssRow,posRow,tmpRow)
    player = []
    players = [[]]
    
    
    for a in range(1,nop):           
        with open('correct.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')      
            loopare = 0                         
            for row in spamreader:                                   
                if len(row) > 0: 
                    if "SS1 " in row[0]:                        
                        loopare +=1
                        print(loopare)                                                                                   
                    if str(a) == row[0]:
                        for x in row:
                            player.append((x))
                        player.append("") 
                        
                        if len(row) < 6: # oi DNF
                            player.append("")
                            player.append("")    
                                
                            
                          
                 
            printPlayers(player)
            player = []            
                
#print(players[1])
        
   








