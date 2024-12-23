import docker

def get_running_containers():
    client = docker.from_env()

    # List all running containers
    containers = client.containers.list()

    return containers