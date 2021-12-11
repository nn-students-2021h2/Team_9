from setuptools import setup, find_namespace_packages

setup(
    name='pretty_print_package',
    version='0.1',
    packages=find_namespace_packages(include=['get_time_packages_project.*']),
    install_requires=['requests==2.26.0'],
    entry_points={
        'console_scripts': [
            ('get_time=get_time_packages_project.pretty_print_package.'
            'pretty_print_module:main'),
            ('get_time_pp=get_time_packages_project.pretty_print_package.'
             'pretty_print_module:main')
        ]
    }
)
