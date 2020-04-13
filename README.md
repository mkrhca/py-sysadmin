### Managing passwords  
<pre>
$ cat handling_password.py
import sys
import paramiko
import time

ip_address = "192.168.2.106"
username = "student"
password = "training"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()
ssh_client.connect(hostname=ip_address,\
                                    username=username, password=password)
print ("Successful connection", ip_address)
ssh_client.invoke_shell()
remote_connection = ssh_client.exec_command('cd /tmp; mkdir work\n')
remote_connection = ssh_client.exec_command('mkdir test_folder\n')
#print( remote_connection.read() )
ssh_client.close
$ 

$ python3 handling_password.py
Successful connection 192.168.2.106
</pre>  

### Executing external commands  
<pre>
$ cat execute_external_commands.py
import subprocess
subprocess.call(["ls"])
subprocess.call(["touch", "sample.txt"])
subprocess.call(["ls"])
print("Sample file created")
subprocess.call(["rm", "sample.txt"])
subprocess.call(["ls"])
print("Sample file deleted")
$ 

$ python3 execute_external_commands.py
file1.txt      execute_external_commands.py     
file1.txt      execute_external_commands.py   sample.txt
Sample.txt file created
file1.txt      execute_external_commands.py
Sample.txt file deleted
$ 
</pre>  

### Prompting for a password and validating  
<pre>
$ cat getpass_example.py 
import getpass
try:
  p = getpass.getpass("Enter your password: ")
except Exception as error:
  print('ERROR', error)
else:
  print('Password entered:', p)
$ 

$ python3 getpass_example.py
Enter your password:
Welcome!!
$ 			
</pre>  

### Reading configuration files  
<pre>
$ cat read_simple.ini
[bug_tracker]
url =https://timesofindia.indiatimes.com/

$ cat read_config.py 
from configparser import ConfigParser
p = ConfigParser()
p.read('read_simple.ini')
print(p.get('bug_tracker', 'url'))

$ python3 read_config_file.py
https://timesofindia.indiatimes.com/
$
</pre>  

### Making backups  
<pre>
$ cat take_backup.py 
import os
import shutil
import time
from sh import rsync

def check_dir(os_dir):
  if not os.path.exists(os_dir):
    print (os_dir, "does not exist.")
    exit(1)
	
def ask_for_confirm():
  ans = input("Do you want to Continue? yes/no\n")
  global con_exit
  if ans == 'yes':
    con_exit = 0
    return con_exit
  elif ans == "no":
    con_exit = 1
    return con_exit
  else:1
    print ("Answer with yes or no.")
    ask_for_confirm()
	
def delete_files(ending):
  for r, d, f in os.walk(backup_dir):
    for files in f:
      if files.endswith("." + ending):
        os.remove(os.path.join(r, files))

backup_dir = input("Enter directory to backup\n")   # Enter directory name
check_dir(backup_dir)
print (backup_dir, "saved.")
time.sleep(3)
backup_to_dir= input("Where to backup?\n")
check_dir(backup_to_dir)
print ("Doing the backup now!")
ask_for_confirm()

if con_exit == 1:
  print ("Aborting the backup process!")
  exit(1)

rsync("-auhv", "--delete", "--exclude=lost+found", "--exclude=/sys", "--exclude=/tmp", "--exclude=/proc",
"--exclude=/mnt", "--exclude=/dev", "--exclude=/backup", backup_dir, backup_to_dir)
$ 
</pre>  

### Comparing data  
<pre>
$ cat file1.csv 
Id,Name,Gender,Age,Address
101,John,Male,20,New York
102,Mary,Female,18,London
103,Aditya,Male,22,Mumbai
104,Leo,Male,22,Chicago
105,Sam,Male,21,Paris
106,Tina,Female,23,Sydney
$ 

$ cat file2.csv 
Id,Name,Gender,Age,Address
101,John,Male,21,New York
102,Mary,Female,20,London
103,Aditya,Male,22,Mumbai
104,Leo,Male,23,Chicago
105,Sam,Male,21,Paris
106,Tina,Female,23,Sydney
$ 

$ cat compare_data.py
import pandas as pd
df1 = pd.read_csv("file1.csv")
df2 = pd.read_csv("file2.csv")
s1 = set([ tuple(values) for values in df1.values.tolist()])
s2 = set([ tuple(values) for values in df2.values.tolist()])
s1.symmetric_difference(s2)
print (pd.DataFrame(list(s1.difference(s2))), '\n')
print (pd.DataFrame(list(s2.difference(s1))), '\n')
$ 

$ python3 compare_data.py
     0     1       2   3         4
0  102  Mary  Female  18    London
1  104   Leo    Male  22   Chicago
2  101  John    Male  20  New York


     0     1       2   3         4
0  101  John    Male  21  New York
1  104   Leo    Male  23   Chicago
2  102  Mary  Female  20    London
$
</pre>
