import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ExampleApp Backend",
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
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha", "Topic :: Utilities",
        "License :: OSI Approved :: BSD License"
    ],
)
