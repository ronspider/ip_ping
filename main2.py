from ping3 import ping, verbose_ping
from datetime import datetime
import openpyxl
from IPy import IP
'''https://pypi.org/project/ping3/'''

# Function
def ip_scan(search_ip):
    result = ping(search_ip)
    result_type = type(result)
    try:
        IP(search_ip)
        if result_type == type(None):
            return f"wasn't reached."

        elif result_type is not bool:
            return f"was reached in {round(result,6)} seconds."

        else:
            return f"wasn't reached."
    except:
        print("no ip found")


# Open source workbook
file_name = "current_ip_log.xlsx"
wb_source = openpyxl.load_workbook(file_name)
worksheet = wb_source.active

# Define scan range/rows in the file to open
scan_range = worksheet.max_row + 1
# scan_range = 15

# Loop over the rows read Col C and write results to Col P
for row in range(2,scan_range):
    for column in "C":
        cell_name = "{}{}".format(column,row)
        string_ip = str(worksheet[cell_name].value)
        print(f"Scanning... {string_ip}")
        cell_result = ip_scan(string_ip)
        for column in "P":
            new_cell_name = "{}{}".format(column,row)
            worksheet[new_cell_name].value = cell_result

# Save current workbook in a copy
wb_source.save("file_output.xlsx")