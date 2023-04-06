# PyAnsys Granta MI Server API

[![PyAnsys](https://img.shields.io/badge/Py-Ansys-ffc107.svg?labelColor=black&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC)](https://docs.pyansys.com/)
[![python](https://img.shields.io/pypi/pyversions/ansys-grantami-serverapi-openapi?logo=pypi)](https://pypi.org/project/ansys-grantami-serverapi-openapi/)
[![pypi](https://img.shields.io/pypi/v/ansys-grantami-serverapi-openapi.svg?logo=python&logoColor=white)](https://pypi.org/project/ansys-grantami-serverapi-openapi/)
[![GH-CI](https://github.com/pyansys/grantami-serverapi-openapi/actions/workflows/generate_library.yml/badge.svg)](https://github.com/pyansys/grantami-serverapi-openapi/actions/workflows/generate_library.yml)
[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Project Overview

Autogenerated client library for the Granta MI Server API Services. Direct use
of this package is unsupported. Use [ansys-grantami-recordlists](https://github.com/pyansys/grantami-recordlists)
instead.

Commits should generally only be made to this repository to update the OpenAPI
YAML definition (stored in ``yaml/``). Changes to the Python code will be made
automatically when the YAML is modified.


## Contributing

This repository is not under active development. It is only for storing the code generated from the API
definition. All development is done in the following repositories:

- [ansys-grantami-recordlists](https://github.com/pyansys/grantami-recordlists)


## Releasing

Since the ``ansys-grantami-serverapi-openapi`` package is auto-generated, the release process differs slightly from
the standard [PyAnsys release procedure](https://dev.docs.pyansys.com/guidelines/dev_practices.html#release-procedures).

1. Ensure the ``main`` branch build status is green, which indicates that the most recent run of the ``Build and Test 
   Client Library`` workflow was successful.
2. Create a new branch from the ``main`` branch with the name ``release/MAJOR.MINOR`` (for example, release/0.2).
3. Make the following changes in ``ansys-<product/service>-<library>-openapi/src/setup.cfg``:
    - Set the ``version`` to ``MAJOR.MINOR``.
    - Set the ``Development Status`` classifier to ``Development Status :: 5 - Production/Stable``.
4. Commit this file. Push the branch to GitHub and create a new PR for this release that merges it to ``main``.
   While effort is focused on the release, changes should not be made to either the YAML definition
   or the ``openapi-client-template``.
5. Wait for the PyAnsys developers to functionally test the new release. Testers should locally install this
   branch and use it to run the full suite of tests in the ``main`` branch of the pythonic packages.
6. Tag the release:
   ```console
   git tag v<MAJOR.MINOR.0>
   git push origin --tags
   ```

Once the tag is pushed to GitHub, a workflow will build and publish the release.
