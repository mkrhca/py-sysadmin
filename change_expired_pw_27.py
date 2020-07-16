import paramiko

def change_expired_password_over_ssh(host, username, current_password, new_password):
   '''
   If got error on login then set with interactive mode.
   '''
   ssh_conn = paramiko.SSHClient()
   ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   ssh_conn.load_system_host_keys()
   ssh_conn.connect(hostname=host, username=username, password=current_password)

   interact = ssh_conn.invoke_shell()
   buff = ''
   while not buff.endswith('UNIX password: '):
       resp = interact.recv(9999)
       buff += resp
   interact.send(current_password + '\n')

   buff = ''
   while not buff.endswith('New password: '):
       resp = interact.recv(9999)
       buff += resp

   interact.send(new_password + '\n')

   buff = ''
   while not buff.endswith('Retype new password: '):
       resp = interact.recv(9999)
       buff += resp

   interact.send(new_password + '\n')


   interact.shutdown(2)
   if interact.exit_status_ready():
       print "EXIT :", interact.recv_exit_status()

   print "Last Password"
   print "LST :", interact.recv(-1)

change_expired_password_over_ssh('13.235.71.179', 'testuser', 'singapore123456', 'L96CfZKLdvB+x1y') 


