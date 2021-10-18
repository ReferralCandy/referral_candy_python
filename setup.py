from setuptools import setup

NAME='referral_candy'
DESCRIPTION='ReferralCandy Python API Client'

setup(name=NAME,
      version='0.2.0',
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
