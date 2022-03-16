import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="masakhane",
    version="0.0.3",
    author="Masakhane",
    author_email="abdouaziz@gmail.com",
    description="An effective language-first preprocessing tool for African languages (🔧 Beta version).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/masakhane-io/masakhane-preprocessing",
    project_urls={
        "Bug Tracker": "https://github.com/masakhane-io/masakhane-preprocessing/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)