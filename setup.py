from setuptools import setup, find_packages
VERSION = open('powonline/version.txt').read()
setup(
    name="powonline",
    version=VERSION.strip(),
    packages=find_packages(),
    install_requires=[
        'bcrypt',
        'config-resolver >= 4.2, <5.0',
        'flask',
        'flask-restful',
        'flask-sqlalchemy',
        'gouge >= 1.1, <2.0',
        'marshmallow',
        'psycopg2',
        'pyjwt',
        'sqlalchemy',
    ],
    extras_require={
        'dev': [
            'alembic',
            'blessings',
            'gouge',
        ],
        'test': [
            'flask-testing',
            'pytest',
            'pytest-catchlog',
            'pytest-coverage',
            'pytest-xdist',
        ]
    },
    include_package_data=True,
    author="Michel Albert",
    author_email="michel@albert.lu",
    description="Tracker for PowWow 2017",
    license="BSD",
    url="https://exhuma.github.com/powonline",
)
