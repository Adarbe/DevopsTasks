import subprocess
from tableprint import table

def get_proc_data(infotype):
    return(subprocess.getoutput("cat /proc/" + str(infotype)))


def print_proc_data(title , data, seperator,width):
    headers = ["Name", "Value"]
    tabledata = []
    for line in data.split("\n"):
        section = line.strip().split(seperator)

        if len(section) >= 2:
            tabledata.append([section[0],section[1]])
    tp = table(tabledata, headers,width=[20,width])

    print(tp)



memoinfo_status = get_proc_data("meminfo")
print_proc_data("memoinfo_status" , memoinfo_status,":",25)
devices_status = get_proc_data("devices")
print_proc_data("devices_status" , devices_status," ",20)
cpu_status = get_proc_data("cpuinfo")
print_proc_data("cpuinfo_status" , cpu_status,"\t",45)
disk_status = get_proc_data("diskstats")
print_proc_data("diskstats_status" , disk_status, "    ",90)