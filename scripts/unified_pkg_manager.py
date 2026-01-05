import subprocess
import sys

def manage_pkgs(action, pkg_type, name):
    """Actions: install, remove. Types: snap, flatpak."""
    print(f"Action: {action}, Type: {pkg_type}, Name: {name}")
    try:
        if pkg_type == "snap":
            cmd = ["sudo", "snap", action, name]
        elif pkg_type == "flatpak":
            cmd = ["flatpak", action, "flathub", name] if action == "install" else ["flatpak", "uninstall", name]
        else:
            print("Unknown type.")
            return
        
        subprocess.run(cmd, check=True)
        print(f"SUCCESS: {action}ed {name} via {pkg_type}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: unified_pkg <action> <type> <name>")
        sys.exit(1)
    manage_pkgs(sys.argv[1], sys.argv[2], sys.argv[3])
