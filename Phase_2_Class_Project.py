#Justin Stevens
#   CIS261
#   Project Phase 2

def getname():
    name = input ("Enter employee name (END to terminate): ")
    return name

def GetDatesWorked():
    fromdate = float(input ("Enter first date worked in format mm/dd/yyyy: "))
    todate = float(input ("Enter last date worked in format mm/dd/yyyy: "))
    datesworked= fromdate, todate
    return datesworked


def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def calculatetaxandnetpay(totalhours, hourlyrate, taxrate):
    tax = float(totalhours) * float(hourlyrate) * float(taxrate)
    netpay = float(totalhours) * float(hourlyrate) - tax
    return tax, netpay
def gettotalhours():
    totalhours = float(input ("Enter total hours: "))
    return totalhours
def gethourlyrate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def gettaxrate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate
def getgrosspay(totalhours, hourlyrate):
    grosspay = float(totalhours) * float(hourlyrate)
    return grosspay
def employeeinfo(name, totalhours, hourlyrate, taxrate, tax, grosspay, netpay):
    print("")
    print("Employee name:", name)
    print("Total hours:", totalhours)
    print("Hourly rate:", hourlyrate)
    print("Tax rate:", taxrate)
    print("Income tax:", tax)
    print("Gross pay:", grosspay)
    print("Net pay:", netpay)
    print("")
def totalinfo(datesworked, totalemployees, totalhours, totaltax, totalgrosspay, totalnetpay):
    print("")
    print("Dates worked:", datesworked)
    print("Total number of employees:", totalemployees)
    print("Total hours:", totalhours)
    print("Total tax:", totaltax)
    print("Total gross pay:", totalgrosspay)
    print("Total net pay:", totalnetpay)
    print("")

if __name__ == "__main__":
    totalemployees = 0
    totalhours = 0
    totaltax = 0
    totalgrosspay = 0
    totalnetpay = 0

    while True:
        name = getname()
        if name == "End":
            break

        hours = gettotalhours()
        hourlyrate = gethourlyrate()
        taxrate = gettaxrate()
        grosspay = getgrosspay(hours, hourlyrate)
        tax, netpay = calculatetaxandnetpay(hours, hourlyrate, taxrate)
        employeeinfo(name, hours, hourlyrate, taxrate, tax, grosspay, netpay)

        # update total
        totalemployees += 1
        totalhours += hours
        totaltax += tax
        totalgrosspay += grosspay
        totalnetpay += netpay
    
    totalinfo(totalemployees, totalhours, totaltax, totalgrosspay, totalnetpay)


