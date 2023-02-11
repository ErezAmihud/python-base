from setuptools import setup, find_packages

setup(
    name="name",
    author="Erez Amihud",
    author_email="erezamihud@gmail.com",
    packages=find_packages(),
    extras_require={"dev": ["ruff"]},
)
