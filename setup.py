from setuptools import setup

setup(
    name = "robotframework-async",
    version = "1.0.1",
    description = "Generic Robot Framework library for asynchronous keyword execution",
    author = "Fredrik Reveny",
    author_email = "chetic@gmail.com",
    url = "https://github.com/Chetic/robotframework-async",
    download_url = "https://github.com/Chetic/robotframework-async",
    keywords = ["async", "robotframework"],
    install_requires = ["robotframework >= 2.8.6"],
    packages = ["AsyncLibrary"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ]
)
