from ping3 import ping # verbose_ping
import openpyxl
from IPy import IP
from datetime import datetime


now_date = datetime.today().strftime('%Y%m%d')
now_time = datetime.today().strftime('%H:%M:%S')

print(now_date)
print(now_time)


# Function
def ip_scan(search_ip):
    result = ping(search_ip)
    result_type = type(result)
    try:
        IP(search_ip)
        if result_type == type(None):
            print("no")
            return "no"

        elif result_type is not bool:
            print(f"{round(result,5)} sec")
            return f"{round(result,5)} s"

        else:
            return f"no"
    except:
        print("no ip")
        return "no ip"


# Open source workbook
file_name = "current_ip_log.xlsx"
wb_source = openpyxl.load_workbook(file_name)
worksheet = wb_source.active

# Define scan range/rows in the file to open
# for testing use a shorter range
scan_range = worksheet.max_row + 1
# scan_range = 15

# Header information for new columns
result_header_1 = f"IP Scan Time on {datetime.today().strftime('%Y-%m-%d')}"
result_header_2 = "Response time"
worksheet["P1"].value = result_header_1
worksheet["Q1"].value = result_header_2

# Loop over the rows read Col C and write results to Col P
for row in range(2,scan_range):
    for column in "C":
        cell_name = "{}{}".format(column,row)
        string_ip = str(worksheet[cell_name].value)
        print(f"Scanning... {string_ip}")
        cell_result = ip_scan(string_ip)
        
        for column in "P":
            new_cell_name_1 = "{}{}".format(column,row)
            worksheet[new_cell_name_1].value = datetime.today().strftime('%H:%M:%S')
        
        for column in "Q":
            new_cell_name_2 = "{}{}".format(column,row)
            worksheet[new_cell_name_2].value = cell_result
           
# Save current workbook in a copy
wb_source.save(f"{now_date}_{file_name}")
