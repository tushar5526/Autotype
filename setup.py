import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Autotype",
    version="1.0.0",
    description="Autotype on websites that have copy-paste disabled like Moodle, HackerEarth contest etc.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tushar5526/Autotype",
    author="Tushar Gupta",
    author_email="tushar.gupta1026@gmail.com",
    license="Creative Commons Zero v1.0 Universal",
    classifiers=[
        # "License :: OSI Approved :: CC0 1.0 Universal",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["Autotype"],
    include_package_data=True,
    install_requires=[
        "click==8.1.3",
        "colorama==0.4.5",
        "customtkinter==4.6.3",
        "darkdetect==0.7.1",
        "importlib-metadata==5.0.0",
        "Pillow==9.1.1",
        "pynput==1.7.3",
        "python-xlib==0.32",
        "six==1.16.0",
        "tk==0.1.0",
        "typer==0.4.2",
        "typing_extensions==4.4.0",
        "zipp==3.10.0",
        "pyobjc==7.3; sys_platform=='darwin'"
    ],
    entry_points={
        "console_scripts": [
            "Autotype=Autotype.__main__:main",
        ]
    },
)
