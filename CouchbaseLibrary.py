'''
Created on 27 Feb 2014

@author: GWallace
'''
#!/usr/bin/env python
from couchbase import Couchbase
from couchbase import FMT_JSON

def setCouchbaseServer(theHost, thePort, theBucket, thePassword):
    print('Hostname: ' + theHost)
    print('Port: ' + thePort)
    print('Bucketname: ' + theBucket)
    global cbClient
    cbClient= Couchbase.connect(host=theHost, port=thePort, bucket=theBucket, password=thePassword, default_format=FMT_JSON)
    
'''
=============================
COUCHBASE METHODS
=============================
------------------------------------------------------------------------------------------------------------------------
The set method will replace a key if it exists or add it if it does not, and will serialize its value to JSON by default. 
There are also individual add and replace methods.  
The return value is a common Result object indicating status and other metadata, including its CAS 
-- a value indicating the Document's current version.
------------------------------------------------------------------------------------------------------------------------
'''
def writeDocumentToCouchbase(key, jsonDoc): 
    result = cbClient.set(key, jsonDoc)
    print result
    return result
    
'''
-----------------------------------------------------------------------------
The get method returns the Result of the object.
You can access the actual value by using the Result's object value property.
------------------------------------------------------------------------------
'''        
def readDocumentFromCouchbase(key): 
    item = cbClient.get(key, no_format=True)
    print(item.value)
    return item.value
    
def readBinaryFromCouchbase(key): 
    item = cbClient.get(key)
    print(item.value)
    return item.value    

'''
---------------------------------------------------------------------------
Change time to live of existing document- if the document doesn't exist 
no error is thrown if quiet is Set to True
---------------------------------------------------------------------------
'''
def extendTimeToLiveOfDocument(key, isQuiet, timeToLive):
    result= cbClient.get(key, quiet=isQuiet, ttl=timeToLive) 
    print result
    
'''
-----------------------------------------------------------------------------
Removes a key from the server. 
If quiet is specified, an exception is not raised if the key does not exist.
------------------------------------------------------------------------------
'''
def deleteDocumentFromCouchbase(key, isQuiet):
    result= cbClient.delete(key, quiet=isQuiet)
    print result