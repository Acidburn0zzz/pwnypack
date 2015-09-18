from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys
import os


__version__ = '0.7.0'


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


requires = [
    'six',
    'capstone',
    'paramiko',
]


if sys.version_info[:2] < (2, 7):
    requires.extend([
        'counter',
        'ordereddict',
        'argparse',
    ])


if sys.version_info[:2] < (3, 4):
    requires.append('enum34')


def read_file(filename):
    try:
        with open(os.path.join(os.path.dirname(__file__), filename)) as f:
            return f.read()
    except IOError:
        return ''


setup(
    name='pwnypack',
    packages=['pwny', 'pwnypack'],
    version=__version__,
    description='Official Certified Edible Dinosaurs CTF toolkit.',
    long_description=read_file('README.rst') + '\n' + read_file('changelog.rst'),
    author='Ingmar Steen',
    author_email='iksteen@gmail.com',
    url='https://github.com/edibledinos/pwnypack/',
    download_url='https://github.com/edibledinos/pwnypack/tarball/v%s' % __version__,
    setup_requires=['setuptools>=17.1'],
    install_requires=requires,
    tests_require=['mock', 'coverage', 'pytest-cov', 'pytest'],
    cmdclass = {'test': PyTest},
    entry_points={
        'console_scripts': [
            'pwny=pwnypack.main:main',
        ],
    },
    keywords=['wargame', 'ctf'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
    ],
)
