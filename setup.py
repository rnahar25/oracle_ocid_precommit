from setuptools import setup


setup(
    name = 'ocid_precommit',
    description = 'check for ocids in precommit hook',
    scripts = ['ocid_precommit'],
    install_requires=[
        'regex',
        'argparse'
    ],
)
