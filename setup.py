from setuptools import find_packages, setup
setup(
    name='gaurav',
    packages=find_packages(include=['gaurav']),
    version='0.0.0',
    description='My first Python library',
    author='Gaurav Pandey',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)