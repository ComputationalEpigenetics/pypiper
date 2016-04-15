#!/usr/bin/python2.7
"""Getting Started: A simple sample pipeline built using pypiper."""

# This is a runnable example. You can run it to see what the output
# looks like.

# First, make sure you can import the pypiper package

import os
import pypiper

# Create a PipelineManager instance (don't forget to name it!)
# This starts the pipeline.

mypiper = pypiper.PipelineManager(name="BASIC",
	outfolder="pipeline_output/")

# Now just build shell command strings, and use the run function
# to execute them in order. run needs 2 things: a command, and the
# target file you are creating.

# First, generate some random data

# specify target file:
tgt = "pipeline_output/test.out"

# build the command
cmd = "shuf -i 1-500000000 -n 10000000 > " + tgt

# and run with run(). You must use shell=True here because of 
# redirection (>), which is a shell process, and therefore can't be run
# as a python subprocess.
mypiper.run(cmd, target=tgt, shell=True)

# Now copy the data into a new file.
# first specify target file and build command:
tgt = "pipeline_output/copied.out"
cmd = "cp pipeline_output/test.out " + tgt
mypiper.run(cmd, target=tgt)
# No pipes or redirects, so this does not require shell function.
# (this should be the most common use case).


# You can also string multiple commands together, which will execute
# in order as a group to create the final target.
cmd1 = "sleep 5"
cmd2 = "touch pipeline_output/touched.out"
mypiper.run([cmd1, cmd2], target="pipeline_output/touched.out")

# A command without a target will run every time.
# Find the biggest line
#cmd = "awk 'n < $0 {n=$0} END{print n}' pipeline_output/test.out"
#mypiper.run(cmd, "lock.max", shell=True)

# Use checkprint() to get the results of a command, and then use
# report_result() to print and log key-value pairs in the stats file:
last_entry = mypiper.checkprint("tail -n 1 pipeline_output/copied.out",
	shell=True)
mypiper.report_result("last_entry", last_entry)


# Now, stop the pipeline to complete gracefully.
mypiper.stop_pipeline()

# Observe your outputs in the pipeline_output folder 
# to see what you've created.
