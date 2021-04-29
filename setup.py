import setuptools

setuptools.setup(
    name='fastmetrics',
    version='1.0.0',
    author='Guillaume Demaude',
    author_email='guillaume.demaude@gmail.com',
    description='Faster image quality metrics than scipy',
    platforms='Posix; MacOS X; Windows',
    packages=setuptools.find_packages(where='./fastmetrics'),
    package_dir={
        '': 'fastnmetrics'
    },
    include_package_data=True,
    install_requires=(
        'numexpr',
        'scikit-image'
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)