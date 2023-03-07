import htcondor  # for submitting jobs, querying HTCondor daemons, etc.
import classad   # for interacting with ClassAds, HTCondor's internal data format

hostname_job = htcondor.Submit({
    "executable": "/home/ubuntu/src/shared/scripts/t2.py",  # the program to run on the execute node
    "output": "hostname$(CLUSTER).out.txt",       # anything the job prints to standard output will end up in this file
    "arguments":"1,2,3,4",
    "error": "hostname$(CLUSTER).err.txt",        # anything the job prints to standard error will end up in this file
    "log": "hostname$(CLUSTER).log.txt",
    "stream_output" : "True", # this file will contain a record of what happened to the job
    "request_cpus": "1",            # how many CPU cores we want
    "request_memory": "128MB",      # how much memory we want
    "request_disk": "128MB",        # how much disk space we want
})

print(hostname_job)

schedd = htcondor.Schedd()                   # get the Python representation of the scheduler
submit_result = schedd.submit(hostname_job)  # submit the job
print(submit_result.cluster())  


# sleep_job = htcondor.Submit({
#     "executable": "/bin/sleep",
#     "arguments": "10s",               # sleep for 10 seconds
#     "output": "sleep-$(ProcId).out",  # output and error for each job, using the $(ProcId) macro
#     "error": "sleep-$(ProcId).err",
#     "log": "sleep.log",               # we still send all of the HTCondor logs for every job to the same file (not split up!)
#     "request_cpus": "1",
#     "request_memory": "128MB",
#     "request_disk": "128MB",
# })

# # print(sleep_job)
# schedd = htcondor.Schedd()
# submit_result = schedd.submit(sleep_job, count=10)  # submit 10 jobs

# id = submit_result.cluster()

# hi = schedd.query(
#     constraint=f"ClusterId == {submit_result.cluster()}",
#     projection=["ClusterId", "ProcId", "Out"],
# )

# print(hi)
