from setuptools import setup
from referral_candy import __version__

NAME='referral_candy'
DESCRIPTION='ReferralCandy Python API Client'

setup(name=NAME,
      version=__version__,
      description=DESCRIPTION,
      long_description=DESCRIPTION,
      author='ReferralCandy',
      author_email='hello@referralcandy.com',
      url='https://github.com/ReferralCandy/referral_candy_python',
      packages=['referral_candy'],
      license='MIT License',
      install_requires=[
          'requests',
      ],
      )
