import os
import schedule
import signal
import Endpoint_Helper

#variables
filePath = ""
rawEndpoints =""
hostnameDict = {}

#function to help with signal input and quit when ctrl+c is input.
def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C, exiting program...')
    exit(1)

#function to call every 15 seconds.
def looper_script(endpoints,keys):
    for endpoint in endpoints:
        boolean = Endpoint_Helper.endpoint_checker(endpoint) #checks to see if outcome is UP or DOWN.
        hostname = Endpoint_Helper.url_parser(endpoint.url) #finds the hostname of each endpoint.
        if boolean:
            hostnameDict[hostname]["success"] = hostnameDict[hostname]["success"] + 1
            hostnameDict[hostname]["total"] = hostnameDict[hostname]["total"] + 1
        else:
            hostnameDict[hostname]["total"] = hostnameDict[hostname]["total"] + 1
    for key in keys:
        percentage = round(hostnameDict[key]["success"]/hostnameDict[key]["total"] * 100)
        print("%s%s%d%s" % (key," has ",percentage,"% availability percentage"))
    print("----------------------------------------------------")


##Script start point##
if __name__ == "__main__":
    #Read for signal input of ctrl+c to quit if needed.
    signal.signal(signal.SIGINT, signal_handler)
    #keep receiving user input until a valid YAML file is provided
    while filePath == "":
        filePath = input("Please enter the filepath to a configuration with endpoint information: ").strip()
        try:
            if not os.path.isfile(filePath):
                raise Exception("The path you provided is not valid. Try again.") #if input is not a file, raise exception to mention that.
            if not filePath[-5:] == ".yaml" and not filePath[-4:] == ".yml":
                raise Exception("The file you have provided is not a YAML file. Try again.") #if input is not a YAML file, raise exception to mention that.
            rawEndpoints = Endpoint_Helper.load_endpoints(filePath) #if valid input, save endpoints to variable endpoints.
            if not rawEndpoints:
                raise Exception("There are no endpoints in your YAML file. Please try a different file.")
        except Exception as e:
            print(e)
            filePath = "" #if exception, reset filepath to ""
    #store raw endpoints into individual endpoint objects.
    endpoints = Endpoint_Helper.parse_endpoints(rawEndpoints)
    #parse URL hostnames and initialize them into a hashmap.
    for endpoint in endpoints:
        hostname = Endpoint_Helper.url_parser(endpoint.url)
        hostnameDict[hostname] = {"success":0,
                                  "total":0}
    keys = hostnameDict.keys()
    #Loop every 15 seconds until exit command is input.
    schedule.every(15).seconds.do(looper_script,endpoints,keys)
    print("\nStarting test runs.\n")
    looper_script(endpoints, keys) #inital run, then run every 15 seconds.
    while True:
        schedule.run_pending()
