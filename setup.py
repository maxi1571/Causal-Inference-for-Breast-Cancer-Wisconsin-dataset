"""setup script."""
#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirement_file:
    requirements_list = requirement_file.readlines()
    requirements_list = [lib.replace('\n', '') for lib in requirements_list]

requirements = requirements_list

test_requirements = []

setup(
    author="Michael Tekle Woji",
    author_email="michaeltekle1571@gmail.com",
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
<<<<<<< HEAD
    description="Causal Inference using casualnex libary",
=======
    description="Causal Inference using brest cancer dataset",
>>>>>>> 37ba6b4e78d9131bc302bf58c3c2528de0e74e52
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='scripts, casuality',
    name='Causal-Inference-for-Breast-Cancer-Wisconsin-dataset',
    packages=find_packages(include=['scripts', 'scripts.*']),
    test_suite='Tests',
    tests_require=test_requirements,
    url='https://github.com/maxi1571/Causal-Inference-for-Breast-Cancer-Wisconsin-dataset/',
    version='0.1.0',
    zip_safe=False,
)
