import os
import shlex
import subprocess

def harden_package_manager(package_name):
    # Security: Use shlex.quote to prevent shell injection
    safe_name = shlex.quote(package_name)
    print(f"Hardening package: {safe_name}")
    try:
        subprocess.run(["apt-get", "install", "--only-upgrade", safe_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to harden: {e}")
