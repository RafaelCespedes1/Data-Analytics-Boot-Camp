import os
import csv
csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath) as csvfile:
    readableFile=csv.reader(csvfile)
    csvHeader=next(readableFile)
    firstRow = next(readableFile)
    previousPL=int(firstRow[1])
    totalDelta=0
    totalRowsForAverage=0
    totalMonths=1
    TotalPL = int(firstRow[1])
    Max_Increase_In_Profit_Amount= int(firstRow[1])
    Max_Increase_In_Loss_Amount=int(firstRow[1])
    Max_Increase_In_Profit_Month=firstRow[0]
    Max_Increase_In_Loss_Month=firstRow[0]

    for row in readableFile:
        Annual_Delta = int(int(row[1])-int(previousPL))
        totalDelta = int(totalDelta) + Annual_Delta
        totalRowsForAverage=totalRowsForAverage+1
        if Annual_Delta > int(Max_Increase_In_Profit_Amount):
            Max_Increase_In_Profit_Amount = int(Annual_Delta)
            Max_Increase_In_Profit_Month = row[0]
        if int(Annual_Delta) < int(Max_Increase_In_Loss_Amount):
            Max_Increase_In_Loss_Amount = int(Annual_Delta)
            Max_Increase_In_Loss_Month = row[0]
        previousPL = int(row[1])        
        totalMonths = totalMonths + 1
        TotalPL = TotalPL + int(row[1])
    print("Financial Analysis") 
    print("----------------------------")
    print("Total Months: ", totalMonths)
    print("Total: $", TotalPL)
    print("Average Change: $", round((totalDelta/totalRowsForAverage),2))
    print("Greatest Increase in Profits: ", Max_Increase_In_Profit_Month, " ($",Max_Increase_In_Profit_Amount,")")
    print("Greatest Decrease in Profits: ", Max_Increase_In_Loss_Month, " ($",Max_Increase_In_Loss_Amount,")")
    pathToWriteFile=os.path.join("Analysis","output.txt")
    write_file=open(pathToWriteFile, 'w+')
    write_file.write(str("Financial Analysis"+'\n'))
    write_file.write(str("----------------------------"+'\n'))
    write_file.write("Total Months: " +str(totalMonths)+'\n')
    write_file.write("Total: $" +str(TotalPL)+'\n')
    write_file.write("Average Change: $" +str(round((totalDelta/totalRowsForAverage),2))+'\n')
    write_file.write("Greatest Increase in Profits: " +str(Max_Increase_In_Profit_Month) +str(" ($") +str(Max_Increase_In_Profit_Amount) +str(")")+'\n')
    write_file.write("Greatest Decrease in Profits: " +str(Max_Increase_In_Loss_Month) +str(" ($") +str(Max_Increase_In_Loss_Amount) +str(")")+'\n')