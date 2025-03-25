#!/home/autotech/ip_check/bin/env python3

from ping3 import ping # verbose_ping
import openpyxl
import shutil
from IPy import IP
from datetime import datetime


# Get ISO Date_Time 
def get_time(form):
    if form == "dt":
        return_value =datetime.today().strftime('%Y%m%d_%H%M%S')
    if form == "d":
        return_value = datetime.today().strftime('%Y%m%d')
    if form == "t":
        return_value = datetime.today().strftime('%H:%M:%S')
    return return_value

def make_backup(source_file, destination_file):
    '''Creates a backup file before writing to the file'''
    shutil.copy2(source_file,  destination_file)
    print(f"File '{source_file}' copied to '{destination_file}' successfully (overwritten if existed).")

def ip_scan(search_ip):
    try:
        IP(search_ip)
        result = ping(search_ip)
        result_type = type(result)

        if result_type == type(None):
            print("timed out")
            return "timed out"

        elif result_type == float:
            print(f"reached in {round(result, 7)} seconds")
            return round(result,11)

        elif result_type == bool:
            print("unknown")
            return "unknown"

    except:
        print("no ip address")
        return "no ip address"


# Open source workbook: wb = woorkbook, ws = worksheet
file_backup = "bu_current_ip_log.xlsx"
file_source = "current_ip_log.xlsx"
make_backup(file_source, file_backup)
wb_source = openpyxl.load_workbook(file_source)
ws_source = wb_source.active

# Define scan range/rows in the file to open
# for testing use a shorter range
scan_range = ws_source.max_row + 1
# scan_range = 20

# Start time
start_time = get_time("dt")
print(f"Started at {start_time}")

# Header information for new columns
ws_source["P1"].value = f"Last scan started {start_time}"
ws_source["Q1"].value = "Response [time in sec]"



# Loop over the rows read Col C and update Col Q and P
# IF ip_scan returns a float AND Col Q is float OR Col Q is a none float
# OR ip_scan returns a none float AND Col Q is a none float
# ELSE Col P and Q will not be updated and will retain the last time and result
for row in range(2,scan_range):

    for column in "C":
        cell_col_C = "{}{}".format(column,row)
        string_ip = str(ws_source[cell_col_C].value)
        print(f"{get_time('t')}... Scanning... {string_ip}... ", end="")
        cell_result = ip_scan(string_ip)
        if type(cell_result) == float:
            for column in "P":
                cell_col_P = "{}{}".format(column,row)
                ws_source[cell_col_P].value = get_time("dt")
            for column in "Q":
                cell_col_Q = "{}{}".format(column,row)
                ws_source[cell_col_Q].value = cell_result
        elif type(cell_result) != float:
            for column in "Q":
                cell_col_Q = "{}{}".format(column,row)
                cell_value_Q = ws_source[cell_col_Q].value
                try: # check 
                    cell_value_float = float(cell_value_Q)
                    continue
                except:
                    for column in "P":
                        cell_col_P = "{}{}".format(column,row)
                        ws_source[cell_col_P].value = get_time("dt")
                    for column in "Q":
                        cell_col_Q = "{}{}".format(column,row)
                        ws_source[cell_col_Q].value = cell_result
    
    # Write results into a log file
    with open(f'{get_time("d")}_ip_scan_log.txt', 'a') as the_file:
        the_file.write(f"{ws_source[cell_col_P].value}, {string_ip}, {ws_source[cell_col_Q].value}\n")

# Save current workbook and a copy with start time stamp
wb_source.save(file_source)

# wb_source.save(f"{start_time}_{file_source}")
print("Saved")
# print(f"Finished at {get_time("dt")}")
