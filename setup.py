from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="BetterTkinter",
    version="2.0.0",
    license="MIT",
    author="BetterTkinter Team",
    author_email="contact@bettertkinter.dev",
    description="The ultimate modern UI toolkit for Python - beautiful, customizable widgets with advanced features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Velyzo/BetterTkinter",
    packages=find_packages(include=["bettertkinter", "bettertkinter.*"]),
    download_url='https://github.com/Velyzo/BetterTkinter/archive/refs/tags/v2.0.0.tar.gz',
    install_requires=[
        "Pillow>=8.0.0",  # For advanced image handling
    ],
    extras_require={
        "dev": ["pytest>=6.0", "black", "flake8"],
        "full": ["Pillow>=8.0.0", "colorsys"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Software Development :: Widget Sets",
        "Environment :: X11 Applications",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
    ],
    keywords="tkinter gui ui custom-widgets modern design beautiful python desktop",
    python_requires=">=3.7",
    project_urls={
        "Bug Tracker": "https://github.com/Velyzo/BetterTkinter/issues",
        "Documentation": "https://Velyzo.github.io/BetterTkinterDocs/",
        "Source Code": "https://github.com/Velyzo/BetterTkinter",
        "Changelog": "https://github.com/Velyzo/BetterTkinter/blob/main/CHANGELOG.md",
        "Demo": "https://github.com/Velyzo/BetterTkinter/blob/main/bettertkinter/BTkDemo.py",
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "btk-demo=bettertkinter.BTkDemo:main",
        ],
    },
    dependency_links=[
        "https://github.com/Eldritchy/BetterTkinter/packages"
    ],
)
