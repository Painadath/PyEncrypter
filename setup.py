from distutils.core import setup

setup(name='PyEncrypter',
      version='2021.02.14',
      description='Convert Numbers',
      author='Painadath ',
      scripts=['bin/PyEncrypter'],
      data_files=[
        ('share/pixmaps', ['data/PE.png']),
        ('share/applications', ['data/PE.desktop'])
        ],
 )
