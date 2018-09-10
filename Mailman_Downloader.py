'''

PRESS F5 TO RUN

If you run in to problems email mrallinson@gmail.com
repo  = https://github.com/mattallinson/Mailman

please first run pip install -r requirements.txt in your terminal

This script uses Beautiful Soup and Requests 
to pull data off the KCL Mailman server. 


'''

import requests
from bs4 import BeautifulSoup

URL = "https://mailman.kcl.ac.uk/mailman/"
ADMIN = "admin/"
ROSTER = "roster/"

def mailinglist_cookies(mailinglist, password): # this opens up the admin page, enters the password, and saves the returned cookie to be passed to the next request
	try:
		cookie_request = requests.post(URL+ ADMIN + mailinglist, data = {'adminpw':password})
		cookie_request.raise_for_status()
		return cookie_request.cookies # raises exception if the password is incorrect (or any other 401 error)
	except:
		print("password error")
		return None

def make_roster(mailinglist, cookies): # takes the cookie from the cookie request and requests the roster
	roster_request = requests.get(URL+ ROSTER + mailinglist, cookies = cookies)
	roster_soup = BeautifulSoup(roster_request.text,'html.parser')
	roster_result_set = roster_soup.find_all('a')[:-4] # the last 4 links on the page are admin links
	roster = []
	for r in roster_result_set:
		roster.append(r.text.replace(' at ','@')) #the mailman list inexplicably uses a stupid ' at ' display format

	return roster

def main():
	mailinglist = input("What's the name of the mailing list you want to download?> ")

	while True:		
		password = input("What is the list admin password?> ")
		filename = mailinglist + '-mailinglist.txt'

		cookies = mailinglist_cookies(mailinglist, password)
		if cookies != None:
			roster = make_roster(mailinglist, cookies)		
			for count, email in enumerate(roster,1):
				
				print(count,"/",len(roster))

				with open(filename, 'a') as output:
					output.write(email + ';\n')
			
			print("Saved", len(roster), "email addresses in", filename)
			break		

if __name__ == '__main__':
	main()