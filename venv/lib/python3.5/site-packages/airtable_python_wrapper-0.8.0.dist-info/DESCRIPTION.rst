# Airtable Python Wrapper

[![Build Status](https://travis-ci.org/gtalarico/airtable-python-wrapper.svg?branch=master)](https://travis-ci.org/gtalarico/airtable-python-wrapper)
[![codecov](https://codecov.io/gh/gtalarico/airtable-python-wrapper/branch/master/graph/badge.svg)](https://codecov.io/gh/gtalarico/airtable-python-wrapper)
[![Documentation Status](https://readthedocs.org/projects/airtable-python-wrapper/badge/?version=latest)](http://airtable-python-wrapper.readthedocs.io/en/latest/?badge=latest)

Airtable API Client Wrapper for Python

![project-logo](https://github.com/gtalarico/airtable-python-wrapper/blob/master/docs/source/_static/logo.png)

## Installing

```
pip install airtable-python-wrapper
```

## Documentation

Full documentation here:

http://airtable-python-wrapper.readthedocs.io/

### Usage Example

Below are some of the methods available in the wrapper.

For the full list and documentation visit the [docs](http://airtable-python-wrapper.readthedocs.io/)

You can see the wrapper in action in this [Jupyter Notebook](https://github.com/gtalarico/airtable-python-wrapper/blob/master/Airtable.ipynb).

```
airtable = Airtable('baseKey', 'table_name')

airtable.get_all(view='MyView', maxRecords=20)

airtable.insert({'Name': 'Brian'})

airtable.search('Name', 'Tom')

airtable.update_by_field('Name', 'Tom', {'Phone': '1234-4445'})

airtable.delete_by_field('Name', 'Tom')

```

## License
[MIT](https://opensource.org/licenses/MIT)

## Requires
* requests
* six

#### Requirements [Testing + Docs]
* pytest
* pytest-ordering
* pytest-cov
* coverage
* sphinx
* sphinxcontrib-napoleon


# 0.8.0
* Docs: New Documentation on Parameter filters Docs
* Docs: More documentation and examples.
* Feature: Search now uses filterByFormula
* Added Formula Generator

# 0.7.3
* Removed Unencoded Debug Msg due to IronPython Bug #242

# 0.7.2
* Merge Fix

# 0.7.1-alpha
* Moved version to sep file to fix setup.py error
* Removed urlencode import
* Added Explicit Raise for 422 errors with Decoded Urls

# 0.7.0-dev1
* Feature: Added airtable.get() method to retrieve record
* Fix: sort/field string input to allow sting or list
* Fix: AirtableAuth Docs
* Fix: Keyargs Docs

# 0.6.1-dev1
* Bugfix: Fix Setup to install six.py
* Bugfix: Fix AitableAuth Docs

# 0.6.0-dev1
* Implemented Sort Filter
* Implemented FilterByFormula
* Implemented all param filters as classes
* Added Aliases for Parameters
* Renamed get() to get_iter()

# 0.5.0-dev1

# 0.4.0
* Added replace()
* Added mirror()

# 0.3.0
* Initial Work


