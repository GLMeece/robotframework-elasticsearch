# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch

class ElasticSearchLib(object):
    """
    _A Robot Framework library for querying an elasticsearch server_
    
    It allows one to run a query, count docs, and manage indices (create, delete)

    Requires ``elasticsearch-py``: http://elasticsearch-py.readthedocs.org/en/latest/index.html

    = Table of contents =

    - `Usage`
    - `Keywords`

    = Usage =

    This library has several keywords:
    
    - ``Es Search``
    - ``Es Count``
    - ``Es Delete Index``
    - ``Es Create Index``
    """

    ROBOT_LIBRARY_VERSION = '1.1'

    def es_search(self,p_host,p_port,p_index,p_query):
        """
        === Returns a Query Result from Elastic Search ===
        
        The result is the response from elastic search as a dictionary.

        - ``p_host`` - Elasticsearch server
        - ``p_port`` - Port of the es server
        - ``p_index`` - Name of the index to query
        - ``p_query`` - Query to run

        | ${res} = | Es Search | localhost | 9200 | myIndex |  {"query": {"query_string": {"query": "searched value"}}} |
        """
        
        # Es client
        try:
            param = [{'host':p_host,'port':int(p_port)}]
            es = Elasticsearch(param)
        except Exception:
            raise AssertionError("Connection error on %s:%i",p_host,int(p_port))

        try:
            documents = es.search(body=p_query, index=p_index)
        except Exception:
            raise AssertionError("Search error on %s:%i/%s for query : %s",p_host,int(p_port),p_index,p_query)

        return documents

    def es_count(self,p_host,p_port,p_index,p_query=None):
        """
        === Returns the Number of Documents That Match a Query ===
        
        The result is the response from elastic search. The value is in the "count" field of the response.

        - ``p_host`` - Elasticsearch server
        - ``p_port`` - Port of the es server
        - ``p_index`` - Name of the index to query
        - ``p_query`` - Query to run

        | ${res} = | Es Count | localhost | 9200 | myIndex |  {"query": {"query_string": {"query": "searched value"}}} |

        ``${res}`` contains the number of docs
        """

        # Es client
        try:
            param = [{'host':p_host,'port':int(p_port)}]
            es = Elasticsearch(param)
        except Exception:
            raise AssertionError("Connection error on %s:%i",p_host,int(p_port))

        try:
            result = es.count(index=p_index, body=p_query)
        except Exception:
            raise AssertionError("Count error on %s:%i/%s for query : %s",p_host,int(p_port),p_index,p_query)

        return result['count']

    def es_delete_index(self,p_host,p_port,p_index):
        """
        === Deletes an Index ===

        - ``p_host`` - Elasticsearch server
        - ``p_port`` - Port of the es server
        - ``p_index`` - Name of the index to remove

        | ${res} = | Es Delete Index | localhost | 9200 | myIndex |
        """

        # Es client
        try:
            param = [{'host':p_host,'port':int(p_port)}]
            es = Elasticsearch(param)
        except Exception:
            raise AssertionError("Connection error on %s:%i",p_host,int(p_port))

        try:
            es.indices.delete(index=p_index)
        except Exception:
            raise AssertionError("Can't delete the index %s on %s:%i",p_index,p_host,int(p_port))

    def es_create_index(self,p_host,p_port,p_index,p_mapping=None):
        """
        === Creates an Index ===

        - ``p_host`` - Elasticsearch server
        - ``p_port`` - Port of the es server
        - ``p_index`` - Name of the index to create
        - ``p_mapping`` - (optional) Dictionary containing a custom mapping

        | ${res} = | Es Create Index | localhost | 9200 | myIndex |
        | ${res} = | Es Create Index | localhost | 9200 | myIndex | CustomDictMapping |
        """

        # Es client
        try:
            param = [{'host':p_host,'port':int(p_port)}]
            es = Elasticsearch(param)
        except Exception:
            raise AssertionError("Connection error on %s:%i",p_host,int(p_port))

        try:
            es.indices.create(index=p_index,body=p_mapping)

        except Exception:
            raise AssertionError("Can't create the index %s on %s:%i",p_index,p_host,int(p_port))

    def es_index(self,p_host,p_port,p_index,p_doctype,p_docid,p_document):
        """
        === Indexes a Document by Doctype and Docid ===
        
        Indexes a Document on an elasticsearch index according to a doctype and a docid

        - ``p_host`` - Elasticsearch server
        - ``p_port`` - Port of the es server
        - ``p_index`` - Name of the index to query
        - ``p_doctype`` - Type of the document to index
        - ``p_docid`` - Id of the document to index
        - ``p_document`` - Document to index

        | es index | localhost | 9200 | myIndex | theDocType | id_457891 | {"address": {"street": "myAddress", "city":"Wow city"}} |
        """
        
        # Es client
        try:
            param = [{'host':p_host,'port':int(p_port)}]
            es = Elasticsearch(param)
        except Exception:
            raise AssertionError("Connection error on %s:%i",p_host,int(p_port))

        try:
            es.index(doc_type=p_doctype, id=p_docid, body=p_document, index=p_index)
        except Exception:
            raise AssertionError("Index error on %s:%i/%s for document : %s",p_host,int(p_port),p_index,p_document)
