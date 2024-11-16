from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="BetterTkinter",
    version="1.3.4",
    license="MIT",
    author="Eldritchy",
    author_email="eldritchy.help@gmail.com",
    description="An enhanced tkinter package with custom-styled widgets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eldritchy/bettertkinter",
    packages=find_packages(include=["bettertkinter", "bettertkinter.*"]),
    download_url='https://github.com/Eldritchy/bettertkinter/archive/refs/tags/v1.3.4.tar.gz',
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
        "Bug Tracker": "https://github.com/Eldritchy/bettertkinter/issues",
        "Documentation": "https://eldritchy.github.io/BetterTkinterDocs/",
        "Source Code": "https://github.com/Eldritchy/bettertkinter",
    },
    include_package_data=True,
    dependency_links=[
        "https://github.com/Eldritchy/BetterTkinter/packages"
    ],
)
