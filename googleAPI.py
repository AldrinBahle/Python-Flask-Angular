import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("uzrCreds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("btyOffering")
offeringcat = sheet.worksheet("offeringCat")
offeringdetail = sheet.worksheet("offeringDetail")
offerinlocation = sheet.worksheet("offeringLocation")

catData = offeringcat.get_all_records
detailData = offeringdetail.get_all_records
locationData = offerinlocation.get_all_records

pprint(catData())
print(" ")
pprint(detailData())
print(" ")
pprint(locationData())