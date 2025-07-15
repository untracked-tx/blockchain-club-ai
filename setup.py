#!/usr/bin/env python3
"""
Setup script for CU Denver Blockchain Club AI Assistant
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="blockchain-club-ai",
    version="1.0.0",
    author="CU Denver Blockchain Club",
    author_email="Liam.Murphy@ucdenver.edu",
    description="AI-powered documentation chatbot for the CU Denver Blockchain Club's on-chain membership system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/untracked-tx/blockchain-club-ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "blockchain-club-ai=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["user-guide/*.md", "*.md", "*.txt"],
    },
)
