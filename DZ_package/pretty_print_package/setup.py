from setuptools import setup

setup(
    name='pretty_print_package',
    version='0.1',
    description='description',
    url='http://github.com/name/package_name',
    author='Team_9',
    author_email='email@example.com',
    license='MIT',
    packages=['pretty_print_package'],
    install_requires=[
    'requests==2.26.0',
    'get-time-package==0.1'
    ],
    entry_points={
    'console_scripts': [
    'get_time_pp=pretty_print_package.pretty_print:main',
    ]
    }
)
