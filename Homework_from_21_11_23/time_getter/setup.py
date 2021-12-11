from setuptools import setup, find_namespace_packages

setup(
    name='get_time_package',
    version='0.1',
    packages=find_namespace_packages(include=['get_time_packages_project.*']),
    install_requires=['requests==2.26.0'],
    entry_points={
        'console_scripts': [
            ('get_time=get_time_packages_project.get_time_package.'
            'get_time_module:main'),
        ]
    }
)
