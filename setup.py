from setuptools import setup, find_packages

setup(
    name='click-daily-tools',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        email=personal_email.cli_email:cli
    ''',
)
