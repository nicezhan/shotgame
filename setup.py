from setuptools import setup, find_packages

setup(
    name='pygame-project',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'game=main:main',
        ],
    },
    install_requires=[
        'pygame==2.5.2',
    ],
)