import os
import shutil
from pathlib import Path
from flaskapp import config

get_base_file = lambda x: config.BASE_DIR.joinpath(x)
def file_rewrite(file, old, new):
    with open(file, 'r+') as f:
        data = f.read()
        data = data.replace("{%s}" % old, new)
        f.seek(0)
        f.write(data)

def get_random_secret_key(key_length=24):
    return os.urandom(key_length).hex()

def run(name, target_dir=None):
    if target_dir is None:
        target_dir = Path.cwd()
    project_dir = target_dir.joinpath(name) 

    if project_dir.exists():
        print("Already directory exists: '{:s}'".format(str(project_dir.resolve())))
        shutil.rmtree(project_dir) # debug
        return

    project_dir.mkdir()
    try:
        for base_file in config.BASE_DIR.glob('*'):
            src = str(base_file)
            dst = str(project_dir.joinpath(base_file.name))
            if base_file.is_dir():
                shutil.copytree(src, dst)
                continue
            else:
                shutil.copy(src, dst)
                if base_file == get_base_file('app.py'):
                    file_rewrite(dst, "SECRET_KEY", get_random_secret_key())


        print("Successed to make project dir: '{:s}'".format(str(project_dir.resolve())))
    except Exception as e:
        shutil.rmtree(project_dir)
        print(str(e))
    
