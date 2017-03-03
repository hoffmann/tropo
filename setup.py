from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


install_requires = []

def setup_package():
    setup(
        name='tropo',
        description='Azure Resource Template Generator',
        long_description=long_description,
        url='https://github.com/hoffmann/tropo',
        license='BSD',
        classifiers=[
          'Programming Language :: Python',
        ],
        keywords='',
        packages=find_packages(exclude=['docs', 'tests*']),
        setup_requires=['setuptools_scm'],
        use_scm_version=True,
        zip_safe=False,
        include_package_data=True,
        author='Peter Hoffmann',
        install_requires=install_requires,
        author_email='ph@peter-hoffmann.com'
    )

if __name__ == "__main__":
    setup_package()
