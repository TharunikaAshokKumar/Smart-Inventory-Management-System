from setuptools import setup, find_packages

setup(
    name='SmartInventoryManagementSystem',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'pandas',
        'scikit-learn',
    ],
)
