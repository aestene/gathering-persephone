from setuptools import setup, find_packages

setup(
    name="persephone",
    packages=find_packages(include=["apis*", "yrclient*"]),
)