import os
import platform
import subprocess

def get_uptime():
    system = platform.system()
    if system == "Windows":
        # Windows: use 'net stats srv' or 'systeminfo', but requires admin for some commands
        try:
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    return f"System uptime (since): {line.split('since')[1].strip()}"
        except Exception:
            return "Could not determine uptime on Windows."
    elif system in ("Linux", "Darwin"):
        # Unix-like systems: use 'uptime' command
        try:
            output = subprocess.check_output("uptime -p", shell=True, text=True)
            return f"System uptime: {output.strip()}"
        except Exception:
            return "Could not determine uptime on Unix-like OS."
    else:
        return "Unsupported operating system."

if __name__ == "__main__":
    print(get_uptime())
