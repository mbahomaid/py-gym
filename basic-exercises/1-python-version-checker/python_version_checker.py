import sys

def check_python_version():
    # Get the Python version information
    version = sys.version_info
    print(f"You are using Python {version.major}.{version.minor}.{version.micro}")

if __name__ == "__main__":
    check_python_version()