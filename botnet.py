from fabric.api import *

del env.hosts[:]
env.passwords.clear()
env.host_string = '127.0.0.1'
running_hosts = {}

for line in open('hosts.txt', 'r').readlines():
    host, passw = line.split()
    env.hosts.append(host)
    env.passwords[host] = passw

def run_command(command):
    try:
        with hide('running', 'stdout', 'stderr'):
            if command.strip()[0:5] == "sudo":
                results = sudo(command)
            else:
                results = run(command)
    except:
        results = 'Error'
    
    return results

def check_hosts():
    for host, result in execute(run_command, "uptime", hosts=env.hosts).items():
        if result != "Error":
            running_hosts[host] = result

def get_hosts():
    selected_hosts = []
    for host in raw_input("Hosts (eg: 1 2): ").split():
        selected_hosts.append(env.hosts[int(host)])
    return selected_hosts

def get_shell():
    host = int(raw_input("Host: "))
    execute(open_shell, host=env.hosts[host])   

def execute_cmd():
    cmd = raw_input("Command: ")
    for host, result in execute(run_command, cmd, hosts=get_hosts()).items():
        print "[" + host + "]: " + cmd
        print ('-' * 80) + '\n' + result + '\n'

def list_hosts():
    for count, host in enumerate(running_hosts):
        print "%s. %s %s" % (count, host)


