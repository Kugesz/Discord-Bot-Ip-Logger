from get_ip import get_public_ip
from get_running_containers import get_running_containers
from datetime import datetime
import re
from tabulate import tabulate

# class Container:
#     def __init__(self, image, status, ports, names):
#         self.image = image
#         self.status = status
#         self.ports = ports
#         self.names = names

#     def __str__(self):
#         return f"| {self.image:<15} | {self.status:<10} | {self.ports:<10} | {self.names:<20} |"

def get_message():
    ip = get_public_ip()
    containers = get_running_containers()
#     containersString = containersString = [
#     'CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS     NAMES',
#     'a1b2c3d4e5f6   my-image       "python app.py"          2 hours ago     Up 2 hours     80/tcp    my-container',
#     'b2c3d4e5f6g7   another-image  "node server.js"         3 hours ago     Up 3 hours     3000/tcp  another-container',
#     'c3d4e5f6g7h8   db-image       "postgres"               4 hours ago     Up 4 hours     5432/tcp  db-container',
#     'd4e5f6g7h8i9   redis-image    "redis-server"           5 hours ago     Up 5 hours     6379/tcp  redis-container',
#     'f6g7h8i9j0k1   python-image   "python script.py"       7 hours ago     Up 7 hours     5000/tcp  python-container'
# ]
    containers = []
    for i in range(1, len(containers)):
        parts = re.split(r'\s{2,}', containers[i])
        # print(parts)
        # container = Container(
        #     image =  parts[1],
        #     status = parts[4],
        #     ports =  parts[5],
        #     names =  parts[6],
        # )
        # containers.append(container)
        port_number = parts[5].split('/')[0]

        # need to fix the table for the links
        containers.append([parts[1], parts[4], parts[5], parts[6]])
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Public IP: {ip}\nContainers:\n"

    # message += "| IMAGE           | STATUS     | PORTS      | NAMES                |\n"
    # for container in containers:
    #     message += str(container) + "\n"
    
    headers = ["IMAGE", "STATUS", "PORTS", "NAMES"]

    message += "```"+tabulate(containers, headers=headers, tablefmt="grid")+"```"

    return message

print(get_message())