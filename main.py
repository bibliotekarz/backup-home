import paramiko
import subprocess
from dotenv import load_dotenv

load_dotenv()


def pack():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOSTNAME, PORT, USERNAME, PASSWORD)

    stdin, stdout, stderr = client.exec_command('tar cvzf cennik-inflacji.tgz cennik-inflacji')

    for line in stdout:
        print(line.strip('\n'))

    client.close()
    return


def get_rsync():
    subprocess.run(["touch", "l"])
    return


print(ssaj())


def delete():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOSTNAME, PORT, USERNAME, PASSWORD)

    stdin, stdout, stderr = client.exec_command('rm cennik-inflacji.tgz')

    for line in stdout:
        print(line.strip('\n'))

    client.close()
    return

# print(kasuj())

# https://docs.python.org/2/library/subprocess.html#replacing-shell-pipeline
