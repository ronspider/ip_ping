from ping3 import ping, verbose_ping
from datetime import datetime
import openpyxl
from IPy import IP
'''https://pypi.org/project/ping3/'''

'''
sub_ran_min = str(000)
sub_ran_max = str(200)
ip_add = "10.10.61."

ip_add_str = "10.10.61" + sub_ran_min + "-" + sub_ran_max
sub_range = [x for x in range(sub_ran_min,sub_ran_max)]
ws_result.title = "IP scan" + ip_add + sub_ran_min + "-" + sub_ran_max
'''

# Open source workbook
file_name = "current_ip_log.xlsx"
wb_source = openpyxl.load_workbook(file_name)
first_ws = wb_source.get_sheet_names()[0]
worksheet = wb_source.get_sheet_by_name(first_ws)


for row in range(2,worksheet.max_row+1):
    for column in "C":
        cell_name = "{}{}".format(column,row)
        string_ip = worksheet[cell_name].value
        try:
            print(IP(string_ip))
        except:
            print(f"{string_ip} is not an IP")
            continue


'''
# Create a workbook to save results
wb_result = Workbook()
ws_result = wb_result.active

def write_to_file(line):
    print(line)
    with open('somefile.txt', 'a') as the_file:
        the_file.write(line + '\n')

def to_xlsx(count, time, ipadd, reach, took):
    ws_result.cell(count,1).value = time
    ws_result.cell(count,2).value = ipadd
    ws_result.cell(count,3).value = reach
    ws_result.cell(count,4).value = took
    wb_result
.save("myworkbook.xlsx")

# Set up the work sheet header
to_xlsx(1,"Timestamp","IP Address","Reached YES/NO","Time in sec")


row_write = 2
reach = "No"
took = 0.000000

for ip in sub_range:
    now_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    now = str(now_time)
    search_ip = ip_add + str(ip)
    result = ping(search_ip)
    result_type = type(result)
    
    # print(search_ip, type(result), result)
    if result_type == type(None):
        write_to_file((f"{now} {search_ip} wasn't reached, possible not available."))
        reach, took = "N", 0.000000
        to_xlsx(row_write,now,search_ip,reach,took)
        row_write += 1
    
    elif result_type is not bool:
        write_to_file((f"{now} {search_ip} was reached in {round(result,6)} seconds."))
        reach, took = "Yes", round(result,6)
        to_xlsx(row_write,now,search_ip,reach,took)
        row_write += 1
    
    else:
        write_to_file((f"{now} {search_ip} wasn't reached."))
        reach, took = "N", 0.000000
        to_xlsx(row_write,now,search_ip,reach,took)
        row_write += 1
'''



