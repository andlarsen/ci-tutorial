import os
import subprocess

def create_virtualenv():
    if not os.path.exists('venv'):
        subprocess.run(['python', '-m', 'venv', 'venv'])
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")

def activate_virtualenv():
    if os.path.exists('venv'):
        subprocess.run(['.', 'venv', 'bin', 'activate'], shell=True)
        print("Virtual environment activated.")
    else:
        print("Virtual environment does not exist. Please create it first.")

def install_dependencies():
    if os.path.exists('venv'):
        print("Upgrading pip and installing dependencies...")
        subprocess.run(['python3', '-m', 'pip', 'install', '--upgrade', 'pip'])
        subprocess.run(['venv/bin/pip', 'install', '-r', 'requirements.txt'])
        print("Dependencies installed.")
    else:
        print("Virtual environment does not exist. Please create it first.")

def main():
    create_virtualenv()
    activate_virtualenv()
    install_dependencies()

if __name__ == "__main__":
    main()
    print("Setup complete.")