from distutils.core import setup
setup(
  name = 'export-dynamodb',
  packages = ['export-dynamodb'],
  version = '1.0.0',
  description = 'A cli to export Amazon DynamoDb',
  author = 'Truong Le',
  author_email = 'travistrle@gmail.com',
  url = 'https://github.com/travistrle/export-dynamodb.git',
  license = 'GPLv3',
  download_url = 'https://github.com/travistrle/export-dynamodb/archive/1.0.0.tar.gz',
  keywords = ['aws', 'dynamodb', 'export'],
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: System Administrators',
    'Topic :: Database',
    'Programming Language :: Python :: 3.6',
  ],
  python_requires='>=3.6',
)