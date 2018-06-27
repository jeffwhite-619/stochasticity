from distutils.core import setup

setup(
    name='stochasticity',
    version='0.1.0',
    author='Jeff White',
    author_email='thisguy@thejeffwhite.com',
    packages=['coin',],
    url='https://github.com/jeffwhite-619/stochasticity',
    license='LICENCE',
    description='Modules to generate various sorts of randomness, starting with a simple coin flip.',
    long_description=open('README.txt').read(),
    install_requires="random",
)
