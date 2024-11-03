from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="BetterTkinter",
    version="1.1.0",
    license="MIT",
    author="D&I Projects",
    author_email="di.projects.help@gmail.com",
    description="An enhanced tkinter package with custom-styled widgets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/D-I-Projects/bettertkinter",
    packages=find_packages(include=["bettertkinter", "bettertkinter.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: User Interfaces",
    ],
    keywords="tkinter gui custom-widgets python",
    python_requires=">=3.6",
    project_urls={
        "Bug Tracker": "https://github.com/D-I-Projects/bettertkinter/issues",
        "Documentation": "https://github.com/D-I-Projects/bettertkinter#readme",
        "Source Code": "https://github.com/D-I-Projects/bettertkinter",
    },
    include_package_data=True,
)
