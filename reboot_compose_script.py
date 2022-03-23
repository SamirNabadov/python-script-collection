#!/usr/bin/python3

# for application

import os

path = '/root/projects/'

build_dir = os.listdir(path)
projects_list = []


for folder in build_dir:
    if not folder.endswith('.tmp') and folder.startswith('rbis.'):
        projects_dir = path + folder
        projects_list.append(projects_dir)
        
print(projects_list)
for project in projects_list:
    os.chdir(project)
    os.system("/usr/bin/docker compose up -d")


# for monitoring

"""
#!/usr/bin/python3

import os

path = '/root/monitoring/'

os.chdir(path)

os.system("/usr/bin/docker compose up -d")

"""

# for elk

"""
#!/usr/bin/python3

import os

path = '/root/elk/'

os.chdir(path)

os.system("/usr/bin/docker compose up -d")

"""
