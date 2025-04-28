import pywhatkit as kit

try:
    phoneNumber = input("Enter the phone number (with country code): ") 
    message = input("Enter the message: ")
    hour = int(input("24-hour format: "))
    minute = int(input("Enter minute: "))
   

    kit.sendwhatmsg(phoneNumber, message, hour, minute)
    print(f"Message scheduled to be sent")
    
except Exception as e:
    print(e)
    
