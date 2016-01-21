from setuptools import setup, find_packages

setup(
    name='cpuset-py3',
    version='1.0',
    author="Johannes Bechberger",
    url="https://github.com/parttimenerd/cpuset",
    description="Fork of cpuset (https://github.com/lpechacek/cpuset) by Alex Tsariounov that works with python3",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only"
    ],
    entry_points='''
        [console_scripts]
        cset=cpuset.main:main
    ''',
)