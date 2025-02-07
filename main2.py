from ping3 import ping, verbose_ping
from datetime import datetime
from openpyxl import Workbook
'''https://pypi.org/project/ping3/'''

sub_ran_min = 130
sub_ran_max = 140
ip_add = "10.10.61."
ip_add_str = "10.10.61" + str(sub_ran_min) + "-" + str(sub_ran_max)

sub_range = [x for x in range(sub_ran_min,sub_ran_max)]

wb = Workbook()
ws = wb.active

ws.title = "IP scan" + ip_add + str(sub_ran_min) + "-" + str(sub_ran_max)


def write_to_file(line):
    print(line)
    with open('somefile.txt', 'a') as the_file:
        the_file.write(line + '\n')

def to_xlsx(count, time, ipadd, reach, took):
    ws.cell(count,1).value = time
    ws.cell(count,2).value = ipadd
    ws.cell(count,3).value = reach
    ws.cell(count,4).value = took
    wb.save("myworkbook.xlsx")

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




