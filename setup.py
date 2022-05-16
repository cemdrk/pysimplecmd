from setuptools import setup


setup(
    name="pysimplecmd",
    packages=["src"],
    entry_points={
        "console_scripts": [
            "pysimplecmd=src:main",
        ]
    },
)
