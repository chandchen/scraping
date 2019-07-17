from setuptools import setup, find_packages

setup(
    name="scraping",
    version="1.0",
    url='https://forge.channelfix.com/chand.chen/ebay-ministry',
    license='BSD',
    description="Scrapy Django Apps.",
    author='Chand Chen',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'setuptools',
        'psycopg2==2.8.2',
        'python-scrapyd-api==2.1.2'
    ],
)
