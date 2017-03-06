# leafitAPI
Rest API for the Leafit Application

***Before anything else, Flask is required to run this api so I would advise you install that before attempting to run.*** 

Since I am running this locally the IP address of the server is subject to change. To run the api you just run api.py from the terminal like so. The api will not be accessible if your server name ends up as 127.0.0.1. I have a test that searches for the IP address built in but if it doesn't find one it will prompt you to input one. You can find these with ifconfig (unix and mac) or ipconfig (windows). 

    cd (pathto)/leafitAPI 
    
    leafitAPI user$ python3 api.py
     * Running on http://xxx.xxx.x.x:5000/ (Press CTRL+C to quit)
     * Restarting with stat

     * Debugger is active!
     * Debugger pin code: 234-359-317


You can access each plants info at 
http:// xxx.xxx.x.x:5000/(id), where id is a specific int given to every plant. This is accessible from any browser on the same network and in this specific case, a mobile app.
#api.py
This is where the api is built and the other two files are run from. I have yet to put some authentication into it.

#planttojson.py
planttojson.py doesn't actually create any json files. That was however its original intent. There was going to be a folder of json files that api.py would access but instead api.py just calls the dictionaries of info for each plant which evades any file conversion or creation.

#plantsort.py
The parsing of plantGuide.txt is done here. It separates the text into dictionaries based on a numerical key. The dictionary is then sorted into Plant objects which are eventually converted into a json-like format for the api to broadcast.

#plantGuide.txt
sourced from http://pages.uoregon.edu/ecostudy/elp/hendricks/pdf_files/PlantGuide.pdf.