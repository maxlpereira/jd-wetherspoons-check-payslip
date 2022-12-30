import payslipbot as pb
import send_email as se
import time
from datetime import datetime
import maskpass

currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H:%M:%S")
currentTime = datetime.strptime(currentTime, "%H:%M:%S")
startTime = input('What hour would you like to start?')

if startTime == '':
    finalTime = 1
else:
    startTime += ':00:00'
    startTime = datetime.strptime(startTime, "%H:%M:%S")
    finalTime = currentTime - startTime
    finalTime = int(finalTime.total_seconds())
    
employeeNumber = input('Employee number: ')
employeePass = input('Password: ')
dayBirth = int(input('Day of birthday(2 digits): '))
monthBirth = int(input('Month of birthday(2 digits): '))
yearBirth = int(input('Year of birthday(2 digits): '))
answer2 = input("Mothers maiden name: ")
answer1 = input("1st schools name: ")


check_payslip = False
while check_payslip is not True:    
    count_check = 0
    check_payslip = pb.PayslipBot(employeeNumber, employeePass, dayBirth, monthBirth, yearBirth, answer1, answer2)
    time.sleep(finalTime)
    check_payslip.login()
    time.sleep(10)
    check_payslip.securityquentions()
    time.sleep(7)
    while count_check <= 7:
        if check_payslip.checknew() is False:
            time.sleep(55)
            check_payslip.driver.refresh()
            count_check += 1
        else:
            print('Payslip is on')
            exit()
    check_payslip.driver.close()
        
        
