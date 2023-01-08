# import htcondor
# from pathlib import Path
# import shutil
# from datetime import datetime, timedelta

# now = datetime.now() + timedelta(hours=8)
# dt_string = now.strftime("%H%M%S_%f_%Y%m%d")
# dag_dir = '/home/ubuntu/src/runs/ML_{}'.format(dt_string)
# print("Starting now:",now)
# print("all file in", dag_dir)


# training_1_script_path = "/home/ubuntu/src/shared/scripts/training_1.py"
# training_2_script_path = "/home/ubuntu/src/shared/scripts/training_2.py"
# training_3_script_path = "/home/ubuntu/src/shared/scripts/training_3.py"


# get_data_and_split_script_path = "/home/ubuntu/src/shared/scripts/get_db_and_split.py"
# training_script_path = "/home/ubuntu/src/shared/scripts/training.py"
# testing_script_path = "/home/ubuntu/src/shared/scripts/testing.py"
# update_model_script_path = "/home/ubuntu/src/shared/scripts/update_model.py"

# get_data_and_split_job = htcondor.Submit({
#     "executable": "get_db_and_split.py",  # the program to run on the execute node
#     "output": "get_db_and_split.out",       # anything the job prints to standard output will end up in this file
#     "error": "get_db_and_split.err",        # anything the job prints to standard error will end up in this file
#     "log": "get_db_and_split.log",
#     "stream_output" : "True", # this file will contain a record of what happened to the job
#     "request_cpus": "1",            # how many CPU cores we want
#     "request_memory": "128MB",      # how much memory we want
#     "request_disk": "128MB",        # how much disk space we want
# })
# print(get_data_and_split_job)

# training_job = htcondor.Submit({
#     "executable": "training.py",  # the program to run on the execute node
#     "output": "training$(CLUSTER).out",       # anything the job prints to standard output will end up in this file
#     "arguments":"{};$(x)".format(dag_dir),
#     "error": "training$(CLUSTER).err",        # anything the job prints to standard error will end up in this file
#     "log": "training$(CLUSTER).log",
#     "stream_output" : "True", # this file will contain a record of what happened to the job
#     "request_cpus": "1",            # how many CPU cores we want
#     "request_memory": "128MB",      # how much memory we want
#     "request_disk": "128MB",        # how much disk space we want
# })
# print(training_job)


# testing_job = htcondor.Submit({
#     "executable": "testing.py",  # the program to run on the execute node
#     "output": "testing$(CLUSTER).out",       # anything the job prints to standard output will end up in this file
#     "arguments":"{};$(x)".format(dag_dir),
#     "error": "testing$(CLUSTER).err",        # anything the job prints to standard error will end up in this file
#     "log": "testing$(CLUSTER).log",
#     "stream_output" : "True", # this file will contain a record of what happened to the job
#     "request_cpus": "1",            # how many CPU cores we want
#     "request_memory": "128MB",      # how much memory we want
#     "request_disk": "128MB",        # how much disk space we want
# })
# print(testing_job)

# update_model_job = htcondor.Submit({
#     "executable": "update_model.py",  # the program to run on the execute node
#     "output": "update_model.out",       # anything the job prints to standard output will end up in this file
#     "arguments":dag_dir,
#     "error": "update_model.err",        # anything the job prints to standard error will end up in this file
#     "log": "update_model.log",
#     "stream_output" : "True", # this file will contain a record of what happened to the job
#     "request_cpus": "1",            # how many CPU cores we want
#     "request_memory": "128MB",      # how much memory we want
#     "request_disk": "128MB",        # how much disk space we want
# })
# print(update_model_job)



# from htcondor import dags
# dag = dags.DAG()

# first_layer = dag.layer(
#     name = 'get_data_and_split',
#     submit_description = get_data_and_split_job,
# )

# training_layer = first_layer.child_layer(
#     name = 'train_it',
#     submit_description = training_job,
#     vars = [{"x":1},{"x":2},{"x":3}]
# )
# testing_layer = training_layer.child_layer(
#     name = 'test_it',
#     submit_description = testing_job,
#     vars = [{"x":1},{"x":2},{"x":3}]
# )

# update_model_layer = testing_layer.child_layer(
#     name = 'should_i_update',
#     submit_description = update_model_job,
# )


# print(dag.describe())
# dag_file = dags.write_dag(dag, dag_dir)

# shutil.copy2(get_data_and_split_script_path, dag_dir)
# shutil.copy2(training_script_path, dag_dir)
# shutil.copy2(testing_script_path, dag_dir)
# shutil.copy2(update_model_script_path, dag_dir)




# print(f'DAG directory: {dag_dir}')
# print(f'DAG description file: {dag_file}')

# dag_submit = htcondor.Submit.from_dag(str(dag_file), {'force': 1})
# print(dag_submit)



# import os
# os.chdir(dag_dir)

# schedd = htcondor.Schedd()
# with schedd.transaction() as txn:
#     cluster_id = dag_submit.queue(txn)

# print(f"DAGMan job cluster is {cluster_id}")

# os.chdir('..')

# dag_job_log = f"{dag_file}.dagman.log"
# print(f"DAG job log file is {dag_job_log}")


# dagman_job_events = htcondor.JobEventLog(str(dag_job_log)).events(None)

# # this event stream only contains the events for the DAGMan job itself, not the jobs it submits
# for event in dagman_job_events:
#     print(event)

#     # stop waiting when we see the terminate event
#     if event.type is htcondor.JobEventType.JOB_TERMINATED and event.cluster == cluster_id:
#         break
    
def auto_train_workflow():
    import htcondor
    from pathlib import Path
    import shutil
    from datetime import datetime, timedelta
    
    now = datetime.now() + timedelta(hours=8)
    dt_string = now.strftime("%H%M%S_%f_%Y%m%d")
    dag_dir = '/home/ubuntu/src/runs/ML_{}'.format(dt_string)
    print("Starting now:",now)
    print("all file in", dag_dir)
    
    
    training_1_script_path = "/home/ubuntu/src/shared/scripts/training_1.py"
    training_2_script_path = "/home/ubuntu/src/shared/scripts/training_2.py"
    training_3_script_path = "/home/ubuntu/src/shared/scripts/training_3.py"
    
    
    get_data_and_split_script_path = "/home/ubuntu/src/shared/scripts/get_db_and_split.py"
    training_script_path = "/home/ubuntu/src/shared/scripts/training.py"
    testing_script_path = "/home/ubuntu/src/shared/scripts/testing.py"
    update_model_script_path = "/home/ubuntu/src/shared/scripts/update_model.py"
    
    get_data_and_split_job = htcondor.Submit({
        "executable": "get_db_and_split.py",  # the program to run on the execute node
        "output": "get_db_and_split.out",       # anything the job prints to standard output will end up in this file
        "error": "get_db_and_split.err",        # anything the job prints to standard error will end up in this file
        "log": "get_db_and_split.log",
        "stream_output" : "True", # this file will contain a record of what happened to the job
        "request_cpus": "1",            # how many CPU cores we want
        "request_memory": "128MB",      # how much memory we want
        "request_disk": "128MB",        # how much disk space we want
    })
    print(get_data_and_split_job)
    
    training_job = htcondor.Submit({
        "executable": "training.py",  # the program to run on the execute node
        "output": "training$(CLUSTER).out",       # anything the job prints to standard output will end up in this file
        "arguments":"{};$(x)".format(dag_dir),
        "error": "training$(CLUSTER).err",        # anything the job prints to standard error will end up in this file
        "log": "training$(CLUSTER).log",
        "stream_output" : "True", # this file will contain a record of what happened to the job
        "request_cpus": "1",            # how many CPU cores we want
        "request_memory": "128MB",      # how much memory we want
        "request_disk": "128MB",        # how much disk space we want
    })
    print(training_job)
    
    
    testing_job = htcondor.Submit({
        "executable": "testing.py",  # the program to run on the execute node
        "output": "testing$(CLUSTER).out",       # anything the job prints to standard output will end up in this file
        "arguments":"{};$(x)".format(dag_dir),
        "error": "testing$(CLUSTER).err",        # anything the job prints to standard error will end up in this file
        "log": "testing$(CLUSTER).log",
        "stream_output" : "True", # this file will contain a record of what happened to the job
        "request_cpus": "1",            # how many CPU cores we want
        "request_memory": "128MB",      # how much memory we want
        "request_disk": "128MB",        # how much disk space we want
    })
    print(testing_job)
    
    update_model_job = htcondor.Submit({
        "executable": "update_model.py",  # the program to run on the execute node
        "output": "update_model.out",       # anything the job prints to standard output will end up in this file
        "arguments":dag_dir,
        "error": "update_model.err",        # anything the job prints to standard error will end up in this file
        "log": "update_model.log",
        "stream_output" : "True", # this file will contain a record of what happened to the job
        "request_cpus": "1",            # how many CPU cores we want
        "request_memory": "128MB",      # how much memory we want
        "request_disk": "128MB",        # how much disk space we want
    })
    print(update_model_job)
    
    
    
    from htcondor import dags
    dag = dags.DAG()
    
    first_layer = dag.layer(
        name = 'get_data_and_split',
        submit_description = get_data_and_split_job,
    )
    
    training_layer = first_layer.child_layer(
        name = 'train_it',
        submit_description = training_job,
        vars = [{"x":1},{"x":2},{"x":3}]
    )
    testing_layer = training_layer.child_layer(
        name = 'test_it',
        submit_description = testing_job,
        vars = [{"x":1},{"x":2},{"x":3}]
    )
    
    update_model_layer = testing_layer.child_layer(
        name = 'should_i_update',
        submit_description = update_model_job,
    )
    
    
    print(dag.describe())
    dag_file = dags.write_dag(dag, dag_dir)
    
    shutil.copy2(get_data_and_split_script_path, dag_dir)
    shutil.copy2(training_script_path, dag_dir)
    shutil.copy2(testing_script_path, dag_dir)
    shutil.copy2(update_model_script_path, dag_dir)
    
    
    
    
    print(f'DAG directory: {dag_dir}')
    print(f'DAG description file: {dag_file}')
    
    dag_submit = htcondor.Submit.from_dag(str(dag_file), {'force': 1})
    print(dag_submit)
    
    
    
    import os
    os.chdir(dag_dir)
    
    schedd = htcondor.Schedd()
    with schedd.transaction() as txn:
        cluster_id = dag_submit.queue(txn)
    
    print(f"DAGMan job cluster is {cluster_id}")
    
    os.chdir('..')
    
    dag_job_log = f"{dag_file}.dagman.log"
    print(f"DAG job log file is {dag_job_log}")
    
    
    dagman_job_events = htcondor.JobEventLog(str(dag_job_log)).events(None)
    
    # this event stream only contains the events for the DAGMan job itself, not the jobs it submits
    for event in dagman_job_events:
        print(event)
    
        # stop waiting when we see the terminate event
        if event.type is htcondor.JobEventType.JOB_TERMINATED and event.cluster == cluster_id:
            break
if __name__ == "__main__":
    auto_train_workflow()