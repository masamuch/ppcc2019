import setuptools

setuptools.setup(
    name="ppcc2019",
    version='0.0.1',
    description='Jupyter notebook for deep learning tutorial at ppcc 2019.',
    author='Masahiko Saito',
    author_email='masamuch@yahoo.co.jp',
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'keras',
        'matplotlib',
        'tensorflow<2.0.0a0',
        'sklearn',
        'pydot',
        'jupyter',
        'graphviz',
    ],
)
