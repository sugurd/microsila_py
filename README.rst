========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        | |codecov|
    * - package
      - | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/microsila_py/badge/?style=flat
    :target: https://readthedocs.org/projects/microsila_py
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/sugurd/microsila_py.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/sugurd/microsila_py

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/sugurd/microsila_py?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/sugurd/microsila_py

.. |codecov| image:: https://codecov.io/github/sugurd/microsila_py/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/sugurd/microsila_py

.. |commits-since| image:: https://img.shields.io/github/commits-since/sugurd/microsila_py/v0.1.2.svg
    :alt: Commits since latest release
    :target: https://github.com/sugurd/microsila_py/compare/v0.1.2...master



.. end-badges

A python backend for microsila MCU library

* Free software: MIT license

Installation
============

::

    pip install microsila_py

You can also install the in-development version with::

    pip install https://github.com/sugurd/microsila_py/archive/master.zip


Documentation
=============


https://microsila_py.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

