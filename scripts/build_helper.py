import subprocess
import os

def automate_build(repo_url):
    """Automates the process of cloning, configuring, and building from source."""
    folder = repo_url.split("/")[-1].replace(".git", "")
    print(f"Cloning {repo_url}...")
    subprocess.run(["git", "clone", repo_url], check=True)
    os.chdir(folder)
    
    steps = ["./configure", "make", "sudo make install"]
    for step in steps:
        print(f"Executing: {step}")
        try:
            subprocess.run(step.split(), check=True)
        except:
            print(f"SKIP: {step} failed or not needed.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: build_helper <repo_url>")
        sys.exit(1)
    automate_build(sys.argv[1])
