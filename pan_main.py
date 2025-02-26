import pandas as pd
import openpyxl
from ping3 import ping
import re


# Check if is IP address
def is_ip_address(ip):
	ip_str = str(ip)
	pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
	return bool(re.match(pattern, ip_str))


# Load Excel file into a DataFrame
def load_excel_file(file_path):
	try:
		df = pd.read_excel(file_path)
		return df
	except Exception as e:
		print(f"Error loading file: {e}")



def ip_scan(search_ip):
	result = ping(search_ip)
	result_type = type(result)

	if result_type == type(None):
		print(search_ip, "timed out")
		return "timed out"

	elif result_type == float:
		print(search_ip, result,"seconds")
		return str(round(result,5))

	elif result_type == bool:
		print(search_ip, "unknown")
		return "unknown"


file_path = 'sample_log.xlsx'  # replace with your Excel file path
data = load_excel_file(file_path)
df = data

print(df)

df['X'] = df['X'].astype(str)
df['Y'] = df['Y'].astype(str)

for index, row in df.iterrows():
	result = row['Adresse IP']
	scan_result = is_ip_address(result)
	df.loc[index,'X'] = 'scanned'
	if scan_result == True:
		df.loc[index,'Y'] = ip_scan(result)
	else:
		df.loc[index,'Y'] = 'no ip address'

print(df)
