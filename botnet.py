from fabric.api import *

del env.hosts[:]
env.passwords.clear()
env.host_string = '127.0.0.1'

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
        if result == "Error":
            env.hosts.remove(host)
            del env.passwords[host]

def get_hosts():
    selected_hosts = []
    for host in raw_input("Hosts (eg: 1 2): ").split():
        selected_hosts.append(env.hosts[int(host)])
    return selected_hosts

def get_shell():
    host = int(raw_input("Host: "))
    try:
        execute(open_shell, host=env.hosts[host])   
    except:
        print "HOST ERROR"

def execute_cmd():
    try:
        cmd = raw_input("Command: ")
        for host, result in execute(run_command, cmd, hosts=get_hosts()).items():
            print "[" + host + "]: " + cmd
            print ('-' * 80) + '\n' + result + '\n'
    except:
        print "HOST ERROR"

def put_file():
    file_name = raw_input("Enter file: ")
    execute(put, file_name, hosts=env.hosts)

def list_hosts():
    print ('-' * 80)
    print "Running Hosts ..."
    for count, host in enumerate(env.hosts):
        print "%s. %s" % (count, host)
    print ('-' * 80)

def menu():
    pass

if __name__ == "__main__":
    check_hosts()
    menu()


