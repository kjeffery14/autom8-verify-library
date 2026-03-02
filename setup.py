from setuptools import setup, find_packages

setup(
    name = 'autom8',
    packages = find_packages(),
    # Date of release used for version - please be sure to use YYYY.MM.DD.seq#, MM and DD should be two digits e.g. 2017.02.05.0
    # seq# will be zero unless there are multiple release on a given day - then increment by one for additional release for that date
    version = '2026.3.2.0',
    description = 'Functions for IBM Verify REST APIs',
    author='Kevin Jeffery',
    author_email='kevin@microknight.com',
    license='Apache License 2.0',
    url='',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Build Tools'
    ],
    zip_safe = False,
    install_requires = [
        'requests'
    ]
)
