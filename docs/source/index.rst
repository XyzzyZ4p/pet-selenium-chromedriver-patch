.. UndetectedChromePatcher documentation master file, created by
   sphinx-quickstart on Tue Dec 27 23:22:46 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Selenium-Chromedriver Patch
===========================

Selenium chrome-webdriver patch covering it from detecting.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Introduction
============

``Selenium chrome-webdriver patch`` is an patch covering selenium webdriver from detecting, inspired by project of
ultrafunkamsterdam (see `here <https://github.com/ultrafunkamsterdam/undetected-chromedriver>`_).

Usage
=====

.. code-block::

        usage: python3 -m selenium_chromedriver_patch [-h] [-s] driverpath

        positional arguments:
          driverpath  Path to selenium chrome webdriver

        options:
          -h, --help  show this help message and exit
          -s          Silent mode


.. automodule:: selenium_chromedriver_patch.patcher
    :members:
    :undoc-members:
    :show-inheritance:

.. toctree::
   :maxdepth: 2
   :caption: Contents:
