from ping3 import ping # verbose_ping
import openpyxl
from IPy import IP
from datetime import datetime


# Get Dates
now_date = datetime.today().strftime('%Y%m%d')
now_date_iso = datetime.today().strftime('%Y-%m-%d')


# Get Time
def get_time():
    return datetime.today().strftime('%H:%M:%S')


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
# wb = woorkbook, ws = worksheet
file_source = "current_ip_log.xlsx"
wb_source = openpyxl.load_workbook(file_source)
ws_source = wb_source.active

# Define scan range/rows in the file to open
# for testing use a shorter range
# scan_range = ws_source.max_row + 1
scan_range = 15

# Header information for new columns
result_header_1 = f"IP Scan Time on {now_date_iso}"
result_header_2 = "Response time"
ws_source["P1"].value = result_header_1
ws_source["Q1"].value = result_header_2

# Loop over the rows read Col C and write results to Col P
for row in range(2,scan_range):
    for column in "C":
        cell_name = "{}{}".format(column,row)
        string_ip = str(ws_source[cell_name].value)
        print(f"Scanning... {string_ip}")
        cell_result = ip_scan(string_ip)
        
        for column in "P":
            new_cell_name_1 = "{}{}".format(column,row)
            ws_source[new_cell_name_1].value = get_time()
        
        for column in "Q":
            new_cell_name_2 = "{}{}".format(column,row)
            ws_source[new_cell_name_2].value = cell_result
           
# Save current workbook in a copy
wb_source.save(f"{now_date}_{file_source}")
