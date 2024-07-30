from setuptools import setup, find_packages

setup(
    name='mi_paquete',
    version='0.1',
    packages=find_packages(),
    description='Un paquete para modelar clientes en una página de compras',
    author='Ariadna Valencia',
    author_email='ariadna.valencia1999@gmail.com',
    url='https://github.com/AriadnaValencia/PreEntrega2-Valencia.git', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
