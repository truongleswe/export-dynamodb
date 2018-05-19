from distutils.core import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='export-dynamodb',
    packages=['exportdynamodb', 'exportdynamodb.entrypoints'],
    version='2.1.0',
    description='A cli to export Amazon DynamoDb',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Truong Le',
    author_email='travistrle@gmail.com',
    url='https://github.com/travistrle/export-dynamodb.git',
    license='GPLv3',
    download_url='https://github.com/travistrle/export-dynamodb/archive/2.1.0.tar.gz',
    keywords=['aws', 'dynamodb', 'export'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'Topic :: Database',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.6',
    install_requires=[
        'click==6.7',
        'boto3==1.7.19'
    ],
    entry_points={
        'console_scripts': [
            'export-dynamodb = exportdynamodb.__main__:main'
        ]
    }
)
