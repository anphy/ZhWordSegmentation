from distutils.core import setup

setup(
    name='chseg',
    version='0.012',
    description='chinese word segment',
    author='Kaiqiang Duan',
    url='https://github.com/anphy/ChineseWordSegmentation',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='NLP,Chinese, word segment',
    packages=['chseg'],
    package_dir={'chseg':'chseg'},
)