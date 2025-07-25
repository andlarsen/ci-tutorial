import os
import subprocess

def create_virtualenv():
    if not os.path.exists('venv'):
        subprocess.run(['python', '-m', 'venv', 'venv'])
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")
        
def install_dependencies():
    if os.path.exists('venv'):
        print("Upgrading pip and installing dependencies...")
        subprocess.run(['python3', '-m', 'pip', 'install', '--upgrade', 'pip'])
        subprocess.run(['venv/bin/pip', 'install', '-r', 'requirements.txt'])
        print("Dependencies installed.")
    else:
        print("Virtual environment does not exist. Please create it first.")

def install_project():
    if os.path.exists('pyproject.toml'):
        print("Installing project...")
        subprocess.run(['pip', 'install', '-e', '.'])
        print("Project installed.")
    else:
        print("pyproject.toml not found. Please ensure it exists in the current directory.")

def main():
    create_virtualenv()
    install_dependencies()
    install_project()
    print("Setup complete.")

if __name__ == "__main__":
    main()