from setuptools import setup

setup(
    name='jsn_exp',
    version='0.1',
    py_modules=['jsn_exp'],
    install_requires=[
        'Click','pygments','colorama'
    ],
    entry_points='''
        [console_scripts]
        jsn=jsn_exp:cli
    ''',
)