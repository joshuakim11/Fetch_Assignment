Hello! This is the solution to my Fetch Take-Home Exercise -- Site Relibability Engineering.
The solution is written in Python, and contains 5 Files:
  1. main.py -- This is where the main script resides, and should be the one that is called to run later.
  2. Endpoint.py -- This is the file that contains the Endpoint class.
  3. Endpoint_Helper.py -- This is a helper file with a few functions that help with endpoint-related functionalities.
  4. YAML_Example.yaml -- This is the file with the YAML example given in the Take-Home Excercise.
  5. example2.yaml -- This is a YAML example with no contents.

To set up and run this program, there are a few prerequisites.
  1. You must have Python3 installed on your machine. To install, please follow this link, download the latest version of python, and follow the required steps: https://www.python.org/downloads/
  2. Open up a new terminal session.
  3. Next, we need to install a few packages for this program to work properly. Specifically: pyyaml, schedule, and requests. This requires pip, Python's package manager.
     1. Ensure pip is installed by running these commands on your command line:
          1. **FOR MAC/UNIX:** python3 -m pip --version
          2. **FOR WINDOWS:** py -m pip --version
     2. If there is no pip package installed, try bootstraping it from your standard package: 
          1. **FOR MAC/UNIX:** python3 -m ensurepip --default-pip
          2. **FOR WINDOWS:** py -m ensurepip --default-pip
     3. Now, use the following commands to install packages on to your machine:
          1. **FOR MAC/UNIX:**
               1. python3 -m pip install pyyaml
               2. python3 -m pip install schedule
               3. python3 -m pip install requests
          3. **FOR WINDOWS:**
               1. py -m pip install pyyaml
               2. py -m pip install schedule
               3. py -m pip install requests
  4. We should be good to run our program now. From this github repository, download all files and unzip them into a directory of your choice.
  5. Navigate to the directory that holds all the unzipped files on your command line.
  6. Run the main.py script by using the following command:
     1. **FOR MAC/UNIX:** python3 main.py
     2. **FOR WINDOWS:** py main.py
  8. The program should run sucessfully!
        


