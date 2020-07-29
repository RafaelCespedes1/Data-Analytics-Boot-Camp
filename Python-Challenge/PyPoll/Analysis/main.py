import os
import csv
csvpath=os.path.join("Resources","election_data.csv")
with open(csvpath) as csvfile:
    readableFile=csv.reader(csvfile)
    csvHeader=next(readableFile)
    names = ["Khan", "Correy", "Li", "O'Tooley"]
    namesDict = {}
    total_votes=0
    for row in readableFile:
        name=row[2]
        if name in namesDict:
            namesDict[name]=namesDict[name]+1
        else:
            namesDict[name]=1
        total_votes=total_votes+1    
print("Election Results")
print("------------------------")
print("Total Votes: ", total_votes)            
print("------------------------")
print(names[0] +str(":  ") +str(round(100*namesDict[names[0]]/total_votes,5)) +str("%  (") +str(namesDict[names[0]])+str(")"))
print(names[1] +str(":  ") +str(round(100*namesDict[names[1]]/total_votes,5)) +str("%  (") +str(namesDict[names[1]])+str(")"))
print(names[2] +str(":  ") +str(round(100*namesDict[names[2]]/total_votes,5)) +str("%  (") +str(namesDict[names[2]])+str(")"))
print(names[3] +str(":  ") +str(round(100*namesDict[names[3]]/total_votes,5)) +str("%  (") +str(namesDict[names[3]])+str(")"))
MaxDictVal = max(namesDict, key=namesDict.get)
print("------------------------")
print("Winner:  " +str(MaxDictVal))
print("------------------------")
pathToWriteFile=os.path.join("Analysis","output.txt")
write_file=open(pathToWriteFile, 'w+')
write_file.write(str("Election Results"+'\n'))
write_file.write(str("------------------------"+'\n'))
write_file.write(str("Total Votes: " +str(total_votes)+'\n'))
write_file.write(str("------------------------"+'\n'))
write_file.write(str(names[0])+ ": " +str(round(100*namesDict[names[0]]/total_votes,5)) + "%  (" +str(namesDict[names[0]])+ ")"+'\n')
write_file.write(str(names[1])+ ": " +str(round(100*namesDict[names[1]]/total_votes,5)) + "%  (" +str(namesDict[names[1]])+ ")"+'\n')
write_file.write(str(names[2])+ ": " +str(round(100*namesDict[names[2]]/total_votes,5)) + "%  (" +str(namesDict[names[2]])+ ")"+'\n')
write_file.write(str(names[3])+ ": " +str(round(100*namesDict[names[3]]/total_votes,5)) + "%  (" +str(namesDict[names[3]])+ ")"+'\n')
write_file.write(str("------------------------"+'\n'))
write_file.write(str("Winner: ") +str(MaxDictVal) +'\n')
write_file.write(str("------------------------"+'\n'))