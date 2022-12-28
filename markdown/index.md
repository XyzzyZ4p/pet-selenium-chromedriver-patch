<!-- UndetectedChromePatcher documentation master file, created by
sphinx-quickstart on Tue Dec 27 23:22:46 2022.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# Selenium-Chromedriver Patch

Selenium chrome-webdriver patch covering it from detecting.

# Indices and tables


* [Index](genindex.md)


* [Module Index](py-modindex.md)


* [Search Page](search.md)

# Introduction

`Selenium chrome-webdriver patch` is an patch covering selenium webdriver from detecting, inspired by project of
ultrafunkamsterdam (see [here](https://github.com/ultrafunkamsterdam/undetected-chromedriver)).

# Usage

```default
usage: python3 -m selenium_chromedriver_patch [-h] [-s] driverpath

positional arguments:
  driverpath  Path to selenium chrome webdriver

options:
  -h, --help  show this help message and exit
  -s          Silent mode
```

## patcher

The core module of selenium_chromedriver_patch


### selenium_chromedriver_patch.patcher.gen_random_cdc()
Generate random encoded cdc value.


* **Returns**

    Random encoded cdc value



* **Return type**

    str



### selenium_chromedriver_patch.patcher.is_binary_patched(executable_path: str | bytes | os.PathLike[str] | os.PathLike[bytes] | int)
Check if executable is patched.


* **Parameters**

    **executable_path** (*str** | **bytes** | **PathLike**[**str**] **| **PathLike**[**bytes**] **| **int*) – The chromedriver location



* **Returns**

    False if not patched, else True



* **Return type**

    bool



### selenium_chromedriver_patch.patcher.patch(executable_path: str | bytes | os.PathLike[str] | os.PathLike[bytes] | int)
Patches the ChromeDriver binary


* **Parameters**

    **executable_path** (*str** | **bytes** | **PathLike**[**str**] **| **PathLike**[**bytes**] **| **int*) – The chromedriver location



* **Returns**

    False on failure, True on success



* **Return type**

    bool
