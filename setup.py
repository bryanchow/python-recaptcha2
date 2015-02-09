import os
from setuptools import setup, find_packages


version = "0.1"

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "recaptcha2",
    version = version,
    description = (
        "A minimalist Python client for the Google reCAPTCHA 2.0 API"
    ),
    long_description = read("README.rst"),
    classifiers = [],
    keywords = "",
    author = "Bryan Chow",
    author_email = "",
    url = "https://github.com/bryanchow/python-recaptcha2",
    download_url = (
        "https://github.com/bryanchow/python-recaptcha2/tarball/master"
    ),
    license = "WTFPL",
    packages = find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'furl',
        'requests',
    ],
)
