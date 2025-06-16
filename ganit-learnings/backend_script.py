import os
import subprocess
import sys
import time
import platform

# Configuration
REPO_URL = "" 
PROJECT_DIR = "" 
DEV_BRANCH = "dev"         
USERS_FIXTURE_FILE = "./fixtures/user.json"
CATEGORIES_FIXTURE_FILE = "./fixtures/categories.json"
PCAFORM_FIXTURE_FILE = "./fixtures/pcaform.json"
POSTGRES_CONTAINER_NAME = "my_postgres_db"
DOCKER_NETWORK_NAME = "my_docker_network"

def run_command(command_list, shell=False, check=True):
    """Run a terminal command and exit on failure."""
    result = subprocess.run(command_list, shell=shell)
    if check and result.returncode != 0:
        print(f"❌ Error running: {' '.join(command_list)}")
        sys.exit(1)

def clone_repo():
    if not os.path.exists(PROJECT_DIR):
        print(f"\n Cloning repository from {REPO_URL}...")
        run_command(["git", "clone", REPO_URL])
        os.chdir(PROJECT_DIR)
        run_command(["git", "checkout", DEV_BRANCH])

    else:
        print("\n✅ Repository already cloned. Pulling latest changes...")
        os.chdir(PROJECT_DIR)
        run_command(["git", "checkout", DEV_BRANCH])
        run_command(["git", "pull", "origin", DEV_BRANCH])
        return
    

def python_setup():
    print("\n Setting up Python environment...")
    run_command([sys.executable, "-m", "venv", "venv"])

    if platform.system() == "Windows":
        pip_exec = os.path.join("venv", "Scripts", "pip")
        python_exec = os.path.join("venv", "Scripts", "python")
    else:
        pip_exec = os.path.join("venv", "bin", "pip")
        python_exec = os.path.join("venv", "bin", "python")

    print("\n Installing Python dependencies...")
    run_command([pip_exec, "install", "-r", "requirements.txt"])

    print("\n Creating .env file...")
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            pass
    print("Please paste your environment variables into the .env file manually.")

    fill_env = input("\nHave you filled in the environment variables in the .env file? (y/n): ").strip().lower()
    if fill_env != 'y':
        print("⚠️ Please fill the .env file and rerun the script.")
        sys.exit(0)

    print("\n Running Django migrations...")

    print("Running makemigrations...")
    run_command([python_exec, "manage.py", "makemigrations"])

    print("Running migrate...")
    run_command([python_exec, "manage.py", "migrate"])

    print("\nRunning collectstatic...")
    run_command([python_exec, "manage.py", "collectstatic", "--noinput"])

    return python_exec

def load_env_vars():
    env_vars = {}
    with open('.env') as f:
        for line in f:
            if line.strip() and not line.strip().startswith('#'):
                key, value = line.strip().split('=', 1)
                env_vars[key] = value
    return env_vars

def docker_network_setup():
    print(f"\n Checking Docker network: {DOCKER_NETWORK_NAME} ...")
    result = subprocess.run(["docker", "network", "ls", "--filter", f"name={DOCKER_NETWORK_NAME}", "--format", "{{.Name}}"], capture_output=True, text=True)
    networks = result.stdout.strip().splitlines()

    if DOCKER_NETWORK_NAME not in networks:
        print(" Creating Docker network...")
        run_command(["docker", "network", "create", DOCKER_NETWORK_NAME])
    else:
        print("✅ Docker network already exists.")

def docker_postgres_setup(env_vars):
    print("\n Starting PostgreSQL Docker container using .env variables...")
    # run command to check if the container is already running
    result = subprocess.run(["docker", "ps", "-q", "-f", f"name={POSTGRES_CONTAINER_NAME}"], capture_output=True, text=True)
    if result.stdout.strip():
        print(f"⚠️ Container '{POSTGRES_CONTAINER_NAME}' is already running. Stopping it first...")
        run_command(["docker", "stop", POSTGRES_CONTAINER_NAME])
        run_command(["docker", "rm", POSTGRES_CONTAINER_NAME])

    run_command([
        "docker", "run", "-d",
        "--name", POSTGRES_CONTAINER_NAME,
        "--network", DOCKER_NETWORK_NAME,
        "-e", f"POSTGRES_USER={env_vars.get('DB_POSTGRES_USERNAME', 'ganit')}",
        "-e", f"POSTGRES_PASSWORD={env_vars.get('DB_POSTGRES_PASSWORD', 'admin')}",
        "-e", f"POSTGRES_DB={env_vars.get('DB_POSTGRES_DBNAME', 'mypcadb')}",
        "-p", f"{env_vars.get('DB_POSTGRES_PORT','5432')}:5432",
        "postgres"
    ])

    print("⏳ Waiting for PostgreSQL to start...")
    time.sleep(10)  # Can be replaced with health checks

def load_fixtures(python_exec):
    if not os.path.exists(USERS_FIXTURE_FILE) and not os.path.exists(CATEGORIES_FIXTURE_FILE) and not os.path.exists(PCAFORM_FIXTURE_FILE):
        print(f"⚠️ Fixture file '{USERS_FIXTURE_FILE}' not found. Skipping loading data.")
        return
    
    if not os.path.exists(USERS_FIXTURE_FILE):
        print(f"⚠️ Fixture file '{USERS_FIXTURE_FILE}' not found. Skipping loading data.")
    else:
        print(f"\n Loading data from fixture: {USERS_FIXTURE_FILE} ...")
        run_command([python_exec, "manage.py", "loaddata", USERS_FIXTURE_FILE])
        print("Users Fixture loaded successfully!")

    if not os.path.exists(CATEGORIES_FIXTURE_FILE):
        print(f"⚠️ Fixture file '{CATEGORIES_FIXTURE_FILE}' not found. Skipping loading data.")
    else:
        print(f"\n Loading data from fixture: {CATEGORIES_FIXTURE_FILE} ...")
        run_command([python_exec, "manage.py", "loaddata", CATEGORIES_FIXTURE_FILE])
        print("Categories Fixture loaded successfully!")

    if not os.path.exists(PCAFORM_FIXTURE_FILE):
        print(f"Fixture file '{PCAFORM_FIXTURE_FILE}' not found. Skipping loading data.")

    else:
        print(f"\n Loading data from fixture: {PCAFORM_FIXTURE_FILE} ...")
        run_command([python_exec, "manage.py", "loaddata", PCAFORM_FIXTURE_FILE])
        print(" Pcaform Fixture loaded successfully!")

def download_fixtures_from_s3(env_vars):
    AWS_PROFILE = env_vars.get('AWS__AWS_PROFILE', 'default')
    AWS_FIXTURE_BUCKET = env_vars.get('AWS__FIXTURE_BUCKET')
    os.makedirs("fixtures", exist_ok=True)
    print("\n Downloading fixtures from S3...")
    run_command(["aws", "s3", "cp", f"s3://{AWS_FIXTURE_BUCKET}", "fixtures","--recursive", "--profile", AWS_PROFILE])
    print("✅ Fixtures downloaded successfully!")


def start_server(python_exec):

    print("\n Starting Django server at http://127.0.0.1:8000 ...")
    run_command([python_exec, "manage.py", "runserver"])

if __name__ == "__main__":
    # clone_repo()
    python_exec = python_setup()
    env_vars = load_env_vars()
    docker_network_setup()
    docker_postgres_setup(env_vars)
    download_fixtures_from_s3(env_vars)
    load_fixtures(python_exec)
    start_server(python_exec)
