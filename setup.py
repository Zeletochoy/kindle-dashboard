from setuptools import find_packages, setup


setup(
    name="kindle_dashboard",
    version="0.0.1",
    description="Dashboard oon my old kindle",
    url="https://github.com/Zeletochoy/kindle-dashboard",
    author="Antoine Lecubin",
    author_email="antoinelecubin@msn.com",
    packages=find_packages(),
    license="beerware",
    install_requires=[
        "beautifulsoup4>=4.10.0,<5.0.0",
        "html2image>=2.0.1,<3.0.0",
        "Pillow>=9.0.1,<10.0.0",
        "requests>=2.27.1,<3.0.0",
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
        ],
    },
    entry_points={
        "console_scripts": [
            "kd-server = kindle_dashboard.cli.server:cli",
        ],
    },
)
