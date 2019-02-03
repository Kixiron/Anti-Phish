from setuptools import setup
from setuptools.command.install import install

setup (
    name="Anti-Phish",
    version="1.1.3",
    install_requires={
        "argparse",
        "json",
        "string",
        "sys",
        "requests",
        "os",
        "random"
    },
    author="Kixiron",
    author_email="kixiron.contact@gmail.com",
    description="An anti-phishing script written in python",
    license="Apache 2.0",
    url="https://github.com/Kixiron/Anti-Phish"
)
