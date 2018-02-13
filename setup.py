from setuptools import setup

setup(name='nb2html',
      version='0.1.0',
      description='to convert jupyter notebooks to html files',

      url='https://github.com/r-ikota/nbtools',
      py_modules=['nb2html'],
      author='Ryo IKOTA',
      author_email='r.ikota.mt@gmail.com',
      entry_points={
        'console_scripts': [
            'nb2html=nb2html:main',
        ],
      },
      license='BSD',
      keywords='jupyter notebook html'

      )
