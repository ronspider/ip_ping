from ping3 import ping, verbose_ping


sub_ran_min = 0
sub_ran_max = 20
ip_add = "192.168.12."

sub_range = [x for x in range(sub_ran_min,sub_ran_max)]

for ip in sub_range:
    search_ip = ip_add + str(ip)
    result = ping(search_ip)
    print(result)



'''
https://github.com/kyan001/ping3

https://www.packetswitch.co.uk/how-to-ping-sweep-your-network-with-python/
https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/
'''
