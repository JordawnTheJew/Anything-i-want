website = input("Give me a web address: ") #Ask user for Web address

https = website.startswith('https') #Condition that webadress string beigns properly

if https == True:
    print('Thank you for a correct address') #If True

if https == False:
    print ('INVALID LINK: Please ensure your web address starts with hypertext secure protocol (https) ') #If False