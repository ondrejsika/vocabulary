from setuptools import setup, find_packages


setup(
    name='vocabulary',
    version='1',
    description='Easy way, how to learn vocabulary',
    url='https://github.com/ondrejsika/vocabulary',
    author='Ondrej Sika',
    author_email='ondrej@ondrejsika.com',
    packages=find_packages(),
    install_requires=[
        'Django==1.8.11',
        'gunicorn==19.4.5',
        'psycopg2==2.6.1',
    ],
)

