from setuptools import setup

setup(
    name='solidity-auto-compiler',
    version='0.1',
    description='Compile your .sol file when modified automatically by giving file path',
    url='http://github.com/mustafa-demirci/solidity-auto-compiler',
    author='Mustafa Demirci',
    author_email='your-email@example.com',  # Eğer paylaşmak istiyorsanız
    license='GNU',
    install_requires=[  # Bağımlılıklarınızı burada belirtin
        'py-solc-x',
        'watchdog'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
