import inspect
import moment

#Login Page

url="https://opensource-demo.orangehrmlive.com/"
username ="Admin"
password= "admin123"

#This will call current function for screen capture
def callfuction():
    return inspect.stack()[1][3]

def cueeentTime():
    currentime = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
    return currentime
def testName():
    return callfuction()
