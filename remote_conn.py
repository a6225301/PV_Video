import wmi
def sys_version(ipaddress, user, password):
    conn = wmi.WMI(computer=ipaddress, user=user, password=password)
    
    for sys in conn.Win32_OperatingSystem():
        
        print sys.NumberOfProcesses  

if __name__ == '__main__':
    sys_version(ipaddress="218.3.235.102", user="qu", password="qwaszx")