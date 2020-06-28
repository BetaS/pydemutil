from setuptools import setup, find_packages


setup(
    name='dem-util',
    version='1.0.2',
    url='',
    license='',
    author='Minsu Kim',
    author_email='mskim@sharekim.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'pyproj',
        'shapely',
        'cairocffi',
        'scour'
    ],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ]
)