import sys
sys.path.append('..')
from flaskapp import create_project

if __name__ == '__main__':
    create_project.run('tests')
