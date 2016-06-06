# robotframework-elasticsearch

ElasticSearch library for Robot Framework

## Presentation

This library provides basic keywords to interact with Elastic Search in a Robot Framework test suite. 
It allows one to query, count, create or delete an index.

## Install

```bash
pip install robotframework-elasticsearch
```

Or, clone the repository and launch this command from the root directory:

```bash
python setup.py install
```

## Example of Use

```robotframework
*** Settings ***
Library     ElasticSearchLib

*** Testcases ***
Number of docs must be equal to 85431
    ${count} =          es count    localhost   9200    my_index
    Should Be Equal     ${count}    85431
```

## Documentation

Read the Robot Framework formatted doc for more information about how to use the keywords:
* [Robot Framework Documentation for ElasticSearchLib](http://htmlpreview.github.io/?https://github.com/pagesjaunes/robotframework-elasticsearch/blob/master/doc/ElasticSearchLib.html)
