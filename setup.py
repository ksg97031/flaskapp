import sys
import setuptools

if sys.version_info < (3, 4):
    print("Unfortunately, your python version is not supported!\n"
          + "Please upgrade at least to Python 3.4!")
    sys.exit(1)

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flaskapp",
    python_requires='>=3.4',
    version="1.0.5",
    author="ksg97031",
    author_email="ksg97031@gmail.com",
    description="Create flask project simply",
    install_requires=['flask', 'pathlib', 'sqlalchemy', 'flask-sqlalchemy'],
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/ksg97031/flaskapp",
    packages=setuptools.find_packages(),
    scripts=['bin/flaskapp'],
    package_data={
        "flaskapp.base": ["*"],
        "flaskapp.base.templates": ["*"],
        "flaskapp.base.static": ["*"],
        "flaskapp.base.static.js": ["*"],
        "flaskapp.base.static.css": ["*"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
