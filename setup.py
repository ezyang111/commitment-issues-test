from setuptools import setup

setup(
    name='cissues',
    version='0.1',
    py_modules=['cissues'],  # Without the .py extension
    entry_points={
        'console_scripts': [
            'cissues=cissues:main',  # Maps 'cissues' command to the main function in your script
        ],
    },
)
