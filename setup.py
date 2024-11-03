from setuptools import setup, find_packages

setup(
    name="BetterTkinter",
    version="v1.0",
    license='MIT',
    author='D&I',
    author_email="di.projects.help@gmail.com",
    description="An enhanced tkinter package with custom-styled widgets",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/D-I-Projects/bettertkinter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
