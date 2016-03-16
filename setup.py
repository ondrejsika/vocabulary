from setuptools import setup, find_packages


setup(
    name='spending',
    version='1',
    description='Stratum server',
    url='https://github.com/ondrejsika/spending',
    author='Ondrej Sika',
    author_email='ondrej@ondrejsika.com',
    packages=find_packages(),
    install_requires=[
        'Django==1.8.11',
        'gunicorn==19.4.5',
        'psycopg2==2.6.1',
    ],
)

