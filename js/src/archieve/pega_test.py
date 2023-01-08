#!/usr/bin python3
from Pegasus.api import *
from pathlib import Path
import logging, os
logging.basicConfig(level=logging.DEBUG)

import sys
path="/home/ubuntu/src"
sys.path.append(path) 


# --- Properties ---------------------------------------------------------------
props = Properties()
props["pegasus.monitord.encoding"] = "json"
#props["pegasus.data.configuration"] = "sharedfs"
props["dagman.maxidle"] = "1000"
props["pegasus.catalog.workflow.amqp.url"] = "amqp://friend:donatedata@msgs.pegasus.isi.edu:5672/prod/workflows"
props.write() # written to ./pegasus.properties 
Properties.ls("condor.request")
# --- Properties ---------------------------------------------------------------
print("Properties")



# --- SiteCatalog ---------------------------------------------------------------
# --- SiteCatalog ---------------------------------------------------------------
# create a SiteCatalog object
sc = SiteCatalog()

# #create a "local" site
# local = Site("local", arch=Arch.X86_64, os_type=OS.LINUX)

# # create and add a shared scratch and local storage directories to the site "local"
# local_shared_scratch_dir = Directory(Directory.SHARED_SCRATCH, path="/home/ubuntu/src/scratch")\
#                             .add_file_servers(FileServer("file://home/ubuntu/src/scratch", Operation.ALL))

# local_local_storage_dir = Directory(Directory.LOCAL_STORAGE, path="/home/ubuntu/src/outputs")\
#                             .add_file_servers(FileServer("file://home/ubuntu/src/outputs", Operation.ALL))

# local.add_directories(local_shared_scratch_dir, local_local_storage_dir)
# local.add_env(PATH=os.environ["PATH"])
# sc.add_sites(local)


# create a "condorpool" site
condorpool = Site(name="condorpool", arch=Arch.X86_64, os_type=OS.LINUX)
condorpool.add_condor_profile(universe="vanilla")
condorpool.add_pegasus_profile(style="condor")
sc.add_sites(condorpool)

# # write the site catalog to the default path "./sites.yml"
sc.write()
# # --- SiteCatalog ---------------------------------------------------------------
print("SiteCatalog")






with open("f.a", "w") as f:
    f.write("This is the contents of the input file for the diamond workflow!")

# --- Replicas -----------------------------------------------------------------
fa = File("f.a").add_metadata(creator="ryan")
rc = ReplicaCatalog()\
    .add_replica("local", fa, Path(".").resolve() / "f.a")\
    .write() # written to ./replicas.yml 
#cat replicas.yml

# --- Transformations ----------------------------------------------------------
preprocess = Transformation(
                "preprocess",
                site="condorpool",
                pfn="/usr/bin/pegasus-keg",
                is_stageable=True,
                arch=Arch.X86_64,
                os_type=OS.LINUX
            )

print(Path(".").resolve() / "src/shared/scripts/test.py")
preprocess = Transformation(
  name="test.py",
  site="condorpool",
  pfn=Path(".").resolve() / "src/shared/scripts/test.py",
  is_stageable=False,
  arch=Arch.X86_64,
  os_type=OS.LINUX
)

# preprocess = Transformation(
#   name="preprocess.py",
#   site="condorpool",
#   pfn=Path(".").resolve() / "src/shared/scripts/preprocess.py",
#   is_stageable=False,
#   arch=Arch.X86_64,
#   os_type=OS.LINUX
# )



tc = TransformationCatalog()\
    .add_transformations(preprocess)\
    .write() # ./written to ./transformations.yml


# --- Workflow -----------------------------------------------------------------
wf = Workflow("blackdiamond")

fb1 = File("f.b1")
fb2 = File("f.b2")
job_preprocess = Job(preprocess)\
                    .add_args("-a", "preprocess", "-T", "3", "-i", fa, "-o", fb1, fb2)\
                    .add_inputs(fa)\
                    .add_outputs(fb1, fb2)

wf.add_jobs(job_preprocess)


try:
    wf.write()
    wf.graph(include_files=True, label="xform-id", output="graph.png")
except PegasusClientError as e:
    print(e)
RUN_DIR = "/home/ubuntu/src/runs"
try:
    wf.plan(dir=RUN_DIR,
     sites=["condorpool"],
     #staging_sites={"condorpool": "stash"},
     #output_sites=["local"],
     cluster=["horizontal"],
     submit=True
 ).wait()
except PegasusClientError as e:
    print(e)
    
try:
    wf.analyze()
except PegasusClientError as e:
    print(e)