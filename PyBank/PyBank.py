import os
import csv

csvpath = os.path.join("budget_data.csv")

totalmonths = 0
total = 0
profitloss = []
profitlossdict = {}
totalchange = 0
greatestinc = 0
greatestincmonth = ""
greatestdec = 0
greatestdecmonth = ""

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        totalmonths = totalmonths + 1
        total = total + int(row[1])
        profitloss.append(int(row[1]))
        profitlossdict[int(row[1])] = row[0]

    #print(profitlossdict)

    print("Financial Analysis")
    print("-----------------------------------------")
    print(f"Total Months: {totalmonths}")
    print(f"Total: ${total}")
    
    for x in range(0, totalmonths - 1):
        totalchange = totalchange + (profitloss[x+1] - profitloss[x])

        if greatestinc < (profitloss[x+1] - profitloss[x]):
            greatestinc = profitloss[x+1] - profitloss[x]
            greatestincmonth = profitlossdict[profitloss[x+1]]
        if greatestdec > (profitloss[x+1] - profitloss[x]):
            greatestdec = profitloss[x+1] - profitloss[x]
            greatestdecmonth = profitlossdict[profitloss[x+1]]

    averagechange = round(totalchange / (totalmonths - 1),2)

    print(f"Average Change: ${averagechange}")
    print(f"Greatest Increase in Profits: {greatestincmonth} (${greatestinc})")
    print(f"Greatest Decrease in Profits: {greatestdecmonth} (${greatestdec})")

headers = ["Total Months: ", "Total: ", "Average Change: ","Greatest Increase in Profits: ", "Greatest Decrease in Profits: "]
data = [totalmonths, total, averagechange, f"{greatestincmonth} (${greatestinc})", f"{greatestdecmonth} (${greatestdec})"]
output = zip(headers,data)

#for values in output:
    #print(values)


output_path = os.path.join("PyBank.txt")

with open(output_path, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerows(output)





        