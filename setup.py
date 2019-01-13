#coding=utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='simsm',
    description="Linhas de ônibus do SIM-SM no seu terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.9.15',
    url='https://github.com/jviriato/sim-sm/',
    author='José Victor Viriato',
    license='MIT',
    entry_points={
               'console_scripts': ['simsm=simsm.simsm:main'],
    },
    author_email='josevviriato@gmail.com',
    install_requires=['terminaltables', 'colorama', 'requests'],
    packages=setuptools.find_packages(),   
    keywords=['CLI', 'bus', 'python'],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)
