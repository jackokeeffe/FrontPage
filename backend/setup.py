from setuptools import setup, find_packages

setup(
    name = "FrontPage",
    version = "1.0",
    description = "A minimal tech news aggregator",
    packages = find_packages(),
    install_requires = ['flask', 'flask_cors', 'bs4', 'gunicorn']
)
