
import subprocess
import sys
import gzip

DB_HOST = ""
DB_PORT = ""
DB_USER = ""
DB_PASSWORD = ""
DB_NAME = ""

BACKUP_PATH = '/backup/postgresql_backup'

PACKAGES = ["postgresql"]

def check_package():
    for PACKAGE in PACKAGES:
        rc = subprocess.call(['which', PACKAGE])
        if rc == 0:
            print(f'{PACKAGE} installed!')
        else:
            print(f'{PACKAGE} missing in path!')
            sys.exit(1)

def list_postgres_databases():
    try:
        command = "psql --dbname=postgresql://{}:{}@{}:{}/{} --list".format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        output = process.communicate()[0]
        if int(process.returncode) != 0:
            print('Command failed. Return code : {}'.format(process.returncode))
            sys.exit(1)
        return output
    except Exception as e:
        print(e)
        sys.exit(1)

def backup_postgres_db():
    try:
        command = "pg_dump --dbname=postgresql://{}:{}@{}:{}/{} -f {}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, BACKUP_PATH)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        output = process.communicate()[0]
        if process.returncode != 0:
            print('Command failed. Return code : {}'.format(process.returncode))
            sys.exit(1)
        return output
    except Exception as e:
        print(e)
        sys.exit(1)

def compress_file():
    compressed_file = "{}.gz".format(str(BACKUP_PATH))
    with open(BACKUP_PATH, 'rb') as f_in:
        with gzip.open(compressed_file, 'wb') as f_out:
            for line in f_in:
                f_out.write(line)
    return compressed_file

def main():
    check_package()
    list_postgres_databases()
    backup_postgres_db()
    compress_file()

if __name__== "__main__":
    main()