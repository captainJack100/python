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
    try:
        execute(put, file_name, hosts=get_hosts())
    except:
        print "HOST ERROR"

def list_hosts():
    print ('-' * 80)
    print "Running Hosts ..."
    for count, host in enumerate(env.hosts):
        print "%s. %s" % (count, host)
    print ('-' * 80)

def options():
    print "0: Exit"
    print "1: List Options"
    print "2: List Hosts"
    print "3: Execute Command"
    print "4: Get Shell"
    print "5: Put File"
    print "\n"
    
def menu():
    available_choices = {1: options, 2: list_hosts, 3: execute_cmd, 4: get_shell, 5: put_file}
    options()

    choice = int(raw_input("Choice: "))
    
    while (choice != 0):
        if (choice not in available_choices.keys()):
            print "Choice not Available. Try again!"
            choice = int(raw_input("Choice: "))
            continue     
        
        available_choices[choice]()
        choice = int(raw_input("Choice: "))

if __name__ == "__main__":
    check_hosts()
    menu()


