from setuptools import setup

def readme():
    with open('README.md', encoding='utf8') as f:
        README = f.read()
    return README


setup(
    name="olxcrapper",
    version="0.1.7",
    description="Ferramenta de scraping de categorias da OLX BR com suporte a notificação de anúncios novos no GMail.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yagolimalins/olxcrapper",
    author="Yago Lima Lins",
    author_email="yago.lima.lins@protonmail.com",
    license="GPL",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["olxcrapper"],
    include_package_data=True,
    install_requires=["bs4", "lxml", "argparse", "requests"],
    entry_points={
        "console_scripts": [
            "olxcrapper=olxcrapper.olxcrapper:main",
        ]
    },
)
