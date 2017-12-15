from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', to='rst', format='md')
except (IOError, ImportError, RuntimeError):
    long_description = ''

setup(
    name="pandoc-attributes",
    version='0.1.7',
    description="An Attribute class to be used with pandocfilters",
    long_description=long_description,
    py_modules=['pandocattributes'],
    author="Aaron O'Leary",
    author_email='dev@aaren.me',
    license='BSD 2-Clause',
    url='http://github.com/aaren/pandoc-attributes',
    install_requires=['pandocfilters', ],
)
