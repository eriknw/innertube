import versioneer
from setuptools import setup, find_packages


with open("README.md") as f:
    long_description = f.read()

setup(
    name="innertube",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Clever pipelining with dask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Erik Welch",
    author_email="erik.n.welch@gmail.com",
    url="https://github.com/eriknw/innertube",
    packages=find_packages(),
    license="BSD",
    python_requires=">=3.6",
    setup_requires=[],
    install_requires=["innerscope", "dask"],
    tests_require=["pytest"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
