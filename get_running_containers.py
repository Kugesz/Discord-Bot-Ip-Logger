import subprocess

def get_running_containers():
    try:
        # Run the 'docker ps' command and capture the output
        result = subprocess.run(['docker', 'ps'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        containers = result.stdout.strip().split('\n')
        return containers
    except subprocess.CalledProcessError as e:
        print(f"Error running docker ps: {e.stderr}")
        return []
    except FileNotFoundError:
        print("Docker is not installed or not found in PATH.")
        return []
