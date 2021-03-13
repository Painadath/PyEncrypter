from setuptools import setup
params = {}
params['scripts'] = ['bin/PyEncrypter']
setup(name='PyEncrypter',
      version='1',
      description='Convert Numbers',
      author='Painadath ',
      packages=['lib'],
      data_files=[
        ('share/pixmaps', ['data/PE.png']),
        ('share/pixmaps', ['data/Button.png']),
        ('share/applications', ['data/PE.desktop'])
        ],
      **params
 )
