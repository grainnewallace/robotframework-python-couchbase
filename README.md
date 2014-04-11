robotframework-python-couchbase
===============================

Robot framework Couchbase Library in Python 


Installation instructions for Couchbase Python client libraries:
http://www.couchbase.com/communities/python/getting-started
https://github.com/couchbase/couchbase-python-client 
https://pypi.python.org/pypi/couchbase

Configuration:
Configure the hostname, bucketname and bucket password of Couchbase Server in the scripts/couchbase_variables.txt
*** Variables ***
${hostname}  localhost
${port}      8091
${bucketname}  thebucket
${bucketpassword}  thePassw0rd


Robot Keywords
==============
Write Document To Couchbase               ${Key}   ${JSON}
Read Document From Couchbase              ${Key}   
Extend Time To Live Of Document           ${Key}   ${IsQuiet}  ${TTL}
Extend Time To Live Of Document Quiet     ${Key}   ${IsQuiet}  ${TTL}
Delete Document From Couchbase            ${Key}   ${IsQuiet} 
Delete Document From Couchbase Quiet      ${Key}   ${IsQuiet}  


Robot Variables
===============
${Key}  
${JsonFile}

===============
Robot Commands
===============
pybot scripts
