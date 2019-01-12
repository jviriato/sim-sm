from setuptools import setup

setup(
    name='sim-sm',
    description="Linhas de ônibus do SIM-SM no seu terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.1',
    scripts=['sim-sm'],
    url='https://github.com/jviriato/sim-sm/',
    author='José Victor Viriato',
    license='MIT',
    author_email='josevviriato@gmail.com',
    packages=setuptools.find_packages(),   
    keywords=['CLI', 'bus', 'python']
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)
