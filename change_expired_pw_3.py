import time
from contextlib import closing
import paramiko

def wait_until_channel_endswith(channel, endswith, wait_in_seconds=15):
    """Continues execution if the specified string appears at the end of the channel

    Raises: TimeoutError if string cannot be found on the channel
    """

    timeout = time.time() + wait_in_seconds
    read_buffer = b''
    while not read_buffer.endswith(endswith):
        if channel.recv_ready():
           read_buffer += channel.recv(4096)
        elif time.time() > timeout:
            raise TimeoutError(f"Timeout while waiting for '{endswith}' on the channel")
        else:
            time.sleep(1)
			
def change_expired_password_over_ssh(host, username, current_password, new_password):
    """Changes expired password over SSH with paramiko"""
    with closing(paramiko.SSHClient()) as ssh_connection:
        ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_connection.connect(hostname=host, username=username, password=current_password)
        ssh_channel = ssh_connection.invoke_shell()

        wait_until_channel_endswith(ssh_channel, b'UNIX password: ')
        ssh_channel.send(f'{current_password}\n')

        wait_until_channel_endswith(ssh_channel, b'New password: ')
        ssh_channel.send(f'{new_password}\n')

        wait_until_channel_endswith(ssh_channel, b'Retype new password: ')
        ssh_channel.send(f'{new_password}\n')

        wait_until_channel_endswith(ssh_channel, b'all authentication tokens updated successfully.\r\n')
		
		
change_expired_password_over_ssh('192.168.1.1', 'username', 'expired-password', 'new-password')
