import paramiko

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect("10.135.7.21",username="root",password="ldcc!2626")

    print('ssh connected')

    ssh.close()

except Exception as err:
    print(err)