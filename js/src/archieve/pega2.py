#!/usr/bin python3
from Pegasus.api import *
from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)

import sys
path="/home/ubuntu/src"
sys.path.append(path) 
wf_dir = str(Path(__file__).parent.resolve())

# --- Properties ---------------------------------------------------------------
props = Properties()
props["pegasus.monitord.encoding"] = "json"                                                                    
props["pegasus.catalog.workflow.amqp.url"] = "amqp://friend:donatedata@msgs.pegasus.isi.edu:5672/prod/workflows"
props["pegasus.mode"] = "tutorial" # speeds up tutorial workflows - remove for production ones
props.write() # written to ./pegasus.properties 
Properties.ls("condor.request")


input_csv_path = str(Path(".").resolve() / "src/shared/data_received/raw.csv")
with open("f.a", "w") as f:
    f.write(input_csv_path)

# --- Replicas -----------------------------------------------------------------
fa = File("f.a")
rc = ReplicaCatalog()\
    .add_replica("local", fa, input_csv_path)\
    .write() # written to ./replicas.yml 
#cat replicas.yml

wf = Workflow("namela")
    # --- Site Catalog -------------------------------------------------------------
exec_site_name="condorpool"
workflow.sc = SiteCatalog()

    # shared_scratch_dir = os.path.join(self.wf_dir, "scratch")
    # local_storage_dir = os.path.join(self.wf_dir, "output")
    
shared_scratch_dir = wf_dir
local_storage_dir = wf_dir

local = Site("local")\
                    .add_directories(
                        Directory(Directory.SHARED_SCRATCH, shared_scratch_dir)
                            .add_file_servers(FileServer("file://" + shared_scratch_dir, Operation.ALL)),
                        
                        Directory(Directory.LOCAL_STORAGE, local_storage_dir)
                            .add_file_servers(FileServer("file://" + local_storage_dir, Operation.ALL))
                    )

exec_site = Site(exec_site_name)\
                        .add_pegasus_profile(style="condor")\
                        .add_condor_profile(universe="vanilla")\
                        .add_profiles(Namespace.PEGASUS, key="data.configuration", value="condorio")

workflow.sc.add_sites(local, exec_site)
        
        
# --- Transformations ----------------------------------------------------------
# preprocess = Transformation(
#                 "preprocess",
#                 site="condorpool",
#                 pfn="/usr/bin/pegasus-keg",
#                 is_stageable=False,

#             )
preprocess = Transformation(
   name="test.py",
   site="local",
   pfn=Path(".").resolve() / "src/shared/scripts/test.py",
   is_stageable=False,
   arch=Arch.X86_64,
   os_type=OS.LINUX
)







findrange = Transformation(
                "findrange",
                site="condorpool",
                pfn="/usr/bin/pegasus-keg",
                is_stageable=False,
                arch=Arch.X86_64,
                os_type=OS.LINUX
            )

analyze = Transformation(
                "analyze",
                site="condorpool",
                pfn="/usr/bin/pegasus-keg",
                is_stageable=False,
                arch=Arch.X86_64,
                os_type=OS.LINUX
            )

tc = TransformationCatalog()\
    .add_transformations(preprocess, findrange, analyze)\
    .write() # ./written to ./transformations.yml


# --- Workflow -----------------------------------------------------------------

fb1 = File("f.b1")
fb2 = File("f.b2")
job_preprocess = Job(preprocess)\
                    .add_args("-a", "preprocess", "-i", fa)\
                    .add_inputs(fa)#\
                    #.add_outputs(fb1, fb2)

fc1 = File("f.c1")
job_findrange_1 = Job(findrange)\
                    .add_args("-a", "findrange", "-T", "3", "-i", fb1, "-o", fc1)\
                    .add_inputs(fb1)\
                    .add_outputs(fc1)

fc2 = File("f.c2")
job_findrange_2 = Job(findrange)\
                    .add_args("-a", "findrange", "-T", "3", "-i", fb2, "-o", fc2)\
                    .add_inputs(fb2)\
                    .add_outputs(fc2)

fd = File("f.d")
job_analyze = Job(analyze)\
                .add_args("-a", "analyze", "-T", "3", "-i", fc1, fc2, "-o", fd)\
                .add_inputs(fc1, fc2)\
                .add_outputs(fd)

wf.add_jobs(job_preprocess)
try:
    wf.write()
    wf.graph(include_files=True, label="xform-id", output="graph.png")
except PegasusClientError as e:
    print(e)
    
    
try:
    wf.plan(submit=True)\
        .wait()
except PegasusClientError as e:
    print(e)
    
# try:
#     wf.analyze()
# except PegasusClientError as e:
#     print(e)