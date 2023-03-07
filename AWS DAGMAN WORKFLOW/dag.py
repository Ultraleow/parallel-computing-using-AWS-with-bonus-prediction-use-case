# import htcondor
# from pathlib import Path
# import shutil
# from datetime import datetime, timedelta

# now = datetime.now() + timedelta(hours=8)
# dt_string = now.strftime("%H%M%S_%f_%Y%m%d")
# dag_dir = '/home/ubuntu/src/runs/user_{}'.format(dt_string)
# print("Starting now:",now)
# print("all file in", dag_dir)

# preprocess_script_path = "/home/ubuntu/src/shared/scripts/preprocess.py"
# prediction_script_path = "/home/ubuntu/src/shared/scripts/prediction.py"
# email_script_path = "/home/ubuntu/src/shared/scripts/send_email.py"
# save_db_script_path = "/home/ubuntu/src/shared/scripts/save_db.py"

# # config_path = "/home/ubuntu/src/shared/scripts/config.py"
# data_path = "/home/ubuntu/src/shared/scripts/raw.csv"
# email="ultraleow@gmail.com"


# preprocess_job = htcondor.Submit({
#     "executable": "preprocess.py",  # the program to run on the execute node
#     "output": "preprocess.out",       # anything the job prints to standard output will end up in this file
#     "error": "preprocess.err",        # anything the job prints to standard error will end up in this file
#     "arguments": "{};{}".format(dag_dir,"raw.csv"),
#     #"transfer_input_files": "/home/ubuntu/src/shared/data_received/raw.csv",    # we also need HTCondor to move the file to the execute node
#     #"should_transfer_files": "yes",             # force HTCondor to transfer files even though we're running entirely inside a container (and it normally wouldn't need to)
#     "log": "preprocess.log",
#     "stream_output" : "True", # this file will contain a record of what happened to the job
#     "request_cpus": "1",            # how many CPU cores we want
#     "request_memory": "128MB",      # how much memory we want
#     "request_disk": "128MB",        # how much disk space we want
# })
# print(preprocess_job)


# prediction_job = htcondor.Submit({
#     "executable": "prediction.py",  # the program to run on the execute node
#     "output": "prediction.out",       # anything the job prints to standard output will end up in this file
#     "arguments":dag_dir,
#     "error": "prediction.err",        # anything the job prints to standard error will end up in this file
#     "log": "prediction.log",
#     "stream_output" : "True", # this file will contain a record of what happened to the job
#     "request_cpus": "1",            # how many CPU cores we want
#     "request_memory": "128MB",      # how much memory we want
#     "request_disk": "128MB",        # how much disk space we want
# })
# print(prediction_job)

# email_job = htcondor.Submit({
#     "executable": "send_email.py",  # the program to run on the execute node
#     "output": "email.out",       # anything the job prints to standard output will end up in this file
#     "arguments":"{};{}".format(dag_dir,email),
#     "error": "email.err",        # anything the job prints to standard error will end up in this file
#     "log": "email.log",
#     "stream_output" : "True", # this file will contain a record of what happened to the job
#     "request_cpus": "1",            # how many CPU cores we want
#     "request_memory": "128MB",      # how much memory we want
#     "request_disk": "128MB",        # how much disk space we want
# })
# print(email_job)


# save_db_job = htcondor.Submit({
#     "executable": "save_db.py",  # the program to run on the execute node
#     "output": "save_db.out",       # anything the job prints to standard output will end up in this file
#     "arguments":"{}".format(dag_dir),
#     "error": "save_db.err",        # anything the job prints to standard error will end up in this file
#     "log": "save_db.log",
#     "stream_output" : "True", # this file will contain a record of what happened to the job
#     "request_cpus": "1",            # how many CPU cores we want
#     "request_memory": "128MB",      # how much memory we want
#     "request_disk": "128MB",        # how much disk space we want
# })
# print(save_db_job)





# from htcondor import dags
# dag = dags.DAG()

# tile_layer = dag.layer(
#     name = 'tile',
#     submit_description = preprocess_job,
# )

# montage_layer = tile_layer.child_layer(
#     name = 'montage',
#     submit_description = prediction_job,
# )

# hah_layer = montage_layer.child_layer(
#     name = 'send_email',
#     submit_description = email_job,
# )

# hah_layer_2 = montage_layer.child_layer(
#     name = 'save_db',
#     submit_description = save_db_job,
# )

# print(dag.describe())
# # blow away any old files
# shutil.rmtree(dag_dir, ignore_errors = True)

# # make the magic happen!
# dag_file = dags.write_dag(dag, dag_dir)



# # the submit files are expecting goatbrot to be next to them, so copy it into the dag directory
# shutil.copy2(preprocess_script_path, dag_dir)
# shutil.copy2(prediction_script_path, dag_dir)
# shutil.copy2(email_script_path, dag_dir)
# shutil.copy2(data_path, dag_dir)
# shutil.copy2(save_db_script_path, dag_dir)
# # shutil.copy2(config_path, dag_dir)


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
def csv_prediction_workflow(path_to_csv,email_to,api=False):
    import htcondor
    from pathlib import Path
    import shutil
    import pandas as pd
    import os
    from datetime import datetime, timedelta
    
    now = datetime.now() + timedelta(hours=8)
    dt_string = now.strftime("%H%M%S_%f_%Y%m%d")
    dag_dir = '/home/ubuntu/src/runs/user_{}'.format(dt_string)
    print("Starting now:",now)
    print("all file in", dag_dir)
    
    preprocess_script_path = "/home/ubuntu/src/shared/scripts/preprocess.py"
    prediction_script_path = "/home/ubuntu/src/shared/scripts/prediction.py"
    email_script_path = "/home/ubuntu/src/shared/scripts/send_email.py"
    save_db_script_path = "/home/ubuntu/src/shared/scripts/save_db.py"
    
    data_path = path_to_csv
    email = email_to
    # data_path = "/home/ubuntu/src/shared/scripts/raw.csv"
    # email="ultraleow@gmail.com"
    
    
    preprocess_job = htcondor.Submit({
        "executable": "preprocess.py",  # the program to run on the execute node
        "output": "preprocess.out",       # anything the job prints to standard output will end up in this file
        "error": "preprocess.err",        # anything the job prints to standard error will end up in this file
        "arguments": "{};{}".format(dag_dir,"raw.csv"),
        #"transfer_input_files": "/home/ubuntu/src/shared/data_received/raw.csv",    # we also need HTCondor to move the file to the execute node
        #"should_transfer_files": "yes",             # force HTCondor to transfer files even though we're running entirely inside a container (and it normally wouldn't need to)
        "log": "preprocess.log",
        "stream_output" : "True", # this file will contain a record of what happened to the job
        "request_cpus": "1",            # how many CPU cores we want
        "request_memory": "128MB",      # how much memory we want
        "request_disk": "128MB",        # how much disk space we want
    })
    print(preprocess_job)
    
    
    prediction_job = htcondor.Submit({
        "executable": "prediction.py",  # the program to run on the execute node
        "output": "prediction.out",       # anything the job prints to standard output will end up in this file
        "arguments":dag_dir,
        "error": "prediction.err",        # anything the job prints to standard error will end up in this file
        "log": "prediction.log",
        "stream_output" : "True", # this file will contain a record of what happened to the job
        "request_cpus": "1",            # how many CPU cores we want
        "request_memory": "128MB",      # how much memory we want
        "request_disk": "128MB",        # how much disk space we want
    })
    print(prediction_job)
    
    email_job = htcondor.Submit({
        "executable": "send_email.py",  # the program to run on the execute node
        "output": "email.out",       # anything the job prints to standard output will end up in this file
        "arguments":"{};{}".format(dag_dir,email),
        "error": "email.err",        # anything the job prints to standard error will end up in this file
        "log": "email.log",
        "stream_output" : "True", # this file will contain a record of what happened to the job
        "request_cpus": "1",            # how many CPU cores we want
        "request_memory": "128MB",      # how much memory we want
        "request_disk": "128MB",        # how much disk space we want
    })
    print(email_job)
    
    
    save_db_job = htcondor.Submit({
        "executable": "save_db.py",  # the program to run on the execute node
        "output": "save_db.out",       # anything the job prints to standard output will end up in this file
        "arguments":"{}".format(dag_dir),
        "error": "save_db.err",        # anything the job prints to standard error will end up in this file
        "log": "save_db.log",
        "stream_output" : "True", # this file will contain a record of what happened to the job
        "request_cpus": "1",            # how many CPU cores we want
        "request_memory": "128MB",      # how much memory we want
        "request_disk": "128MB",        # how much disk space we want
    })
    print(save_db_job)
    
    
    
    
    
    from htcondor import dags
    dag = dags.DAG()
    
    tile_layer = dag.layer(
        name = 'data_preprocessing',
        submit_description = preprocess_job,
    )
    
    montage_layer = tile_layer.child_layer(
        name = 'prediction',
        submit_description = prediction_job,
    )
    
    hah_layer = montage_layer.child_layer(
        name = 'send_email',
        submit_description = email_job,
    )
    
    hah_layer_2 = montage_layer.child_layer(
        name = 'save_db',
        submit_description = save_db_job,
    )
    
    print(dag.describe())
    # blow away any old files
    shutil.rmtree(dag_dir, ignore_errors = True)
    
    # make the magic happen!
    dag_file = dags.write_dag(dag, dag_dir)
    
    
    
    # the submit files are expecting goatbrot to be next to them, so copy it into the dag directory
    shutil.copy2(preprocess_script_path, dag_dir)
    shutil.copy2(prediction_script_path, dag_dir)
    shutil.copy2(email_script_path, dag_dir)
    
    
    if api:
        df = pd.read_csv(data_path)
        export_path =  os.path.join(dag_dir,"raw.csv")
        df.to_csv(export_path, index=False)
    else:
        shutil.copy2(data_path, dag_dir)
    
    os.rename(data_path,os.path.join(dag_dir,"raw.csv"))

    shutil.copy2(save_db_script_path, dag_dir)
    # shutil.copy2(config_path, dag_dir)
    
    
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
    csv_prediction_workflow("/home/ubuntu/src/shared/scripts/raw.csv","ultraleow@gmail.com")     