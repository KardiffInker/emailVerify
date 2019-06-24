import re
def emailverify():    
	regex= '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
    with open("emaillist.txt", "r") as emaillist:
        listy= []
    for line in emaillist:
        line=line.strip()
        listy.append(line)
        emails=[]
    for i in listy:
        email=str(i)
        match=re.match(regex, email)
        if match == None:
            print("badSyntax")
			print(i)
        else:
            emails.append(i)
			emails.sort
			print(emails)