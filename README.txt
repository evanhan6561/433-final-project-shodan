Evan Han and Anh Le
433 Final Project: Using SHODAN to Analyze Barnes Jewish Hospital

Files:
bjc-all-ips.json
    Contains the banners of all IPs under the organization "BJC Health System" as json

vulnerable-ips.json
    Contains the banners of all IPs with potential CVEs. Vulnerable IPs were extracted
    by checking if the "vulns" attribute was set or not.

prettified-cves.json
    Contains the banners of all vulnerable IPs but only containing the data of relevant 
    attributes

bjc-graball.py
    Using the SHODAN python module, query SHODAN for the banners of every IP under
    the organization "BJC Health System" and write data to bjc-all-ips.json

extract-cves.py
    Filter the json of bjc-all-ips.json to only the vulnerable IPs and write them to 
    vulnerable-ips.json . Process further by extracting only the relevant attributes
    and writing to prettified-cves.json .


Analysis:
    Queried SHODAN on 1/3/2020. 16 out of 196 banners contained potential CVEs. 
    All CVEs were tied to the server software used: either Apache httpd 2.4.34 or
    Microsoft IIS 7.5.


Reproducibility:
    A SHODAN API key is required to use their services. Within bjc-graball.py, put in
    your API key as the value of SHODAN_API_KEY.