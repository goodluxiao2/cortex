import subprocess
import os

def fix_docker_permissions():
    """Automates fixing Docker permissions for the current user."""
    user = os.getenv("USER") or os.getenv("LOGNAME")
    print(f"Detecting user: {user}")
    
    try:
        # Check if docker group exists
        subprocess.run(["getent", "group", "docker"], check=True, stdout=subprocess.PIPE)
        print("Docker group already exists.")
    except subprocess.CalledProcessError:
        print("Creating docker group...")
        subprocess.run(["sudo", "groupadd", "docker"], check=True)

    print(f"Adding user {user} to docker group...")
    subprocess.run(["sudo", "usermod", "-aG", "docker", user], check=True)
    
    print("Fixing /var/run/docker.sock permissions...")
    subprocess.run(["sudo", "chown", f"root:docker", "/var/run/docker.sock"], check=True)
    subprocess.run(["sudo", "chmod", "660", "/var/run/docker.sock"], check=True)
    
    print("SUCCESS: Please log out and back in for changes to take effect.")

if __name__ == "__main__":
    fix_docker_permissions()
