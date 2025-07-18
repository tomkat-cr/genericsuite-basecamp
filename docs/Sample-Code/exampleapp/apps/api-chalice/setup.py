import os
from setuptools import setup

requires = (
    "attrs==21.2.0",
    "boto3==1.24.55",
    "botocore==1.27.55",
    "certifi==2018.11.29",
    "cffi==1.15.0",
    "click==8.0.3",
    "cryptography==35.0.0",
    "dnspython==2.6.0rc1",
    # "Flask==2.0.2",
    # "Flask-Cors==3.0.10",
    # "gunicorn==20.1.0",
    "iniconfig==1.1.1",
    "itsdangerous==2.0.1",
    "Jinja2==3.0.2",
    "jmespath==1.0.1",
    "MarkupSafe==2.0.1",
    "packaging==21.0",
    "pluggy==1.0.0",
    "py==1.10.0",
    # "pycairo==1.20.1",
    "pycparser==2.20",
    "PyJWT==2.3.0",
    "pymongo==4.0.1",
    "pyparsing==3.0.0",
    "python-dateutil==2.8.2",
    "PyYAML==6.0",
    "s3transfer==0.6.0",
    "six==1.16.0",
    "toml==0.10.2",
    "urllib3==1.26.11",
    "Werkzeug==2.0.2",
    "wheel==0.41.3",
    "chalice==1.27.3",
    "marshmallow==3.19.0",
)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ExampleApp Backend",
    # version = "1.0.0",
    version=read('version.txt'),
    author="Example App Author",
    author_email="exampleappauthor@example.com",
    description=("ExampleApp Backend"),
    license="Private",
    keywords="",
    url="http://packages.python.org/chalicelib",
    packages=[
        'chalicelib',
    ],
    # namespace_packages=['chalicelib'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    # long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha", "Topic :: Utilities",
        "License :: OSI Approved :: BSD License"
    ],
)
