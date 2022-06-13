from datetime import datetime
import time
import os

username=os.getlogin()
#print(username)#prints the usersname(I need it for getting the path where a file can be stored.)


os.system('cmd /c "echo off"')
os.system('cmd /c "color B"')
global Subject
Subject=input("Subject: ")


path_documents="C:\\Users\\"+username+"\\Documents\\"+Subject+".txt"
path_desktop="C:\\Users\\"+username+"\\Desktop\\"+Subject+".txt"
#path_assigned_by_user=""+Subject+".txt"



file2 = open(path_documents,"a+")
start=0
k=0


def c1():
	global Subject
	#os.system('cmd /c "echo off"')	
	#os.system('cmd /c "color B"')	
	
	
	file2.write("\nDate: ")
	file2.writelines(t)
	file2.write("\n")
	file2.writelines("subject: ")


	
	file2.write(Subject)
	file2.write("\n")
	file2.write("Topic: ")
	topic=input("Topic: ")
	file2.write(topic)
	file2.write("\n")
	file2.write("Note: ")
	
	c2()

def c2():
	global k
	k=k+1
	c=str(k)
	note=input("Note : ")
	file2.write(note)
	file2.write("\n")


while True:
	now = datetime.now()
	date_time = now.strftime("%m/%d/%Y")
	ch=now.strftime("%M")
	t=date_time
	start
	#print(ch)
	if ch=='0' or ch=='00' or ch==0 :
		c1()
	elif(start==0):
		c1()
		start=1
	else:
		c2()



#hange file access modes
file2.close()


'''







'''