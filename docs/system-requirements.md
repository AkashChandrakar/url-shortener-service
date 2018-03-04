# System requirements (what system does)

---

### functional requirements
* The system shall shorten the url provide by user and return sucess/failure message to user.
* The system shall store the shorten url and the original url in some persistent datastore for latter retrival.
* The system shall redirect the shorten url provided by user to original url if it exists otherwise send a error message to user.
* The system shall remove the shorten url after it expires(every url expires after specific period). 


### non functional requirements
* latency / response time
* throughpout
* availability / SLA
* scalibility
* extensiblity
* fail over
* throtlling
* fault tolerance / monitoring alarms
* testability
* security