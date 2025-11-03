import os #Importing a library into your code

print(os.system('df -h'))  #Linux for Windows - Disk Space
print(os.system('net statistics server | find "Statistics since"')) #Uptime and Load Average
print(os.system('(Get-CimInstance -ClassName Win32_OperatingSystem).LastBootUpTime')) #RAM