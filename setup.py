from setuptools import setup, find_packages

setup(
    name="golden-vortex",
    version="3.7.4",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.1.0",
        "numpy>=1.26.0",
        "matplotlib>=3.8.0",
    ],
)
