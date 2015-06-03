import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('{{ PROJECT_NAME  }}/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='{{ PROJECT_NAME }}',
    version=version,
    url='',
    license='{{ license  }}',
    author='{{ author }}',
    author_email='{{ email }}',
    description='{{ description }}',
    long_description=open('README.md').read(),
    packages=['{{ PROJECT_NAME }}'],
    include_package_data=True,
    install_requires=[
    ]
)

