'''
@summary: setup script 

@author: Micle Bu <mekery@gmail.com>
@copyright: Copyright &copy; 2012 Micle Bu
@license: BSD New
@version: setup.py 2012-03-31 Micle Bu
'''
from distutils.core import setup
from pdfdig import __version__

setup(
    name='pdfdig',
    version=__version__,
    description='pdf content digger and anlyzer',
    long_description='pdf content digger and anlyzer',
    license='BSD New',
    author='Micle Bu',
    author_email='mekery at gmail dot com',
    url='https://github.com/mekery/pdfdig',
    packages=['pdfdig'],
    scripts=[
        'utility/pdftotext.py',
        'utility/pdfgrep.py',
        'utility/pdftoc.py',
    ],
    keywords=['pdf digger','pdf converter','pdf toc','text analysis','text mining'],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: "BSD New" License',
        'Operating System :: POSIX',
        'Topics :: Text Processing',
    ],
)
