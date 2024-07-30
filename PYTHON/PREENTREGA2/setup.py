from setuptools import setup, find_packages

setup(
    name='mi_paquete',
    version='0.1',
    packages=find_packages(),
    description='Un paquete para modelar clientes en una página de compras',
    author='Ariadna',
    author_email='ariadna@gmail.com',
    url='https://github.com/tuusuario/mi_paquete',  # URL del repositorio si lo tienes
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
