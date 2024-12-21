import subprocess

def get_running_containers():
    # Run the 'docker ps' command and capture the output
    result = subprocess.run(['docker', 'ps'], stdout=subprocess.PIPE, text=True)
    containers = result.stdout.strip().split('\n')
    return containers