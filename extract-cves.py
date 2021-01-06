#!/usr/bin/env python
import json

def extract_vulnerable():
    with open('./bjc-all-ips.json') as f:
        bjc_all = json.load(f)

        # Extract all of the vulnerable IPs and write to json file
        vulnerable_matches = []
        for match in bjc_all:
            # Only record the matches with vulnerabilities
            if "vulns" in match:
                vulnerable_matches.append(match)
        with open('./vulnerable-ips.json', 'w') as f_new:
            json.dump(vulnerable_matches, f_new, indent=4)
            print("Found ", len(vulnerable_matches), " IPs with CVEs")
            print("Total Matches: ", len(bjc_all))
        
        return vulnerable_matches

def print_software_and_version(vulnerable_matches):
    # product: version
    software_and_version_count = {}
    for entry in vulnerable_matches:
        software = entry['product']
        version = entry['version']
        combined_str = software + '-' + version

        if (combined_str in software_and_version_count):
            software_and_version_count[combined_str] += 1
        else:
            software_and_version_count[combined_str] = 1
    
    print(software_and_version_count)

def filter_vulnerable(vulnerable_matches):
    """
    We're only interested in a small subset of the data of each vulnerable entry.
    Thus, lets only extract the ones we need for readability.
    """

    # Filter out the higher level keys
    filtered_entries = []
    for entry in vulnerable_matches:
        filtered_entry = {}
        filtered_entry["ip_str"] = entry["ip_str"]
        filtered_entry["product"] = entry["product"]
        # filtered_entry["version"] = entry["version"]
        filtered_entry["domains"] = entry["domains"]
        filtered_entry["hostnames"] = entry["hostnames"]

        # entry['vulns'] is itself a dictionary. We don't need need all of its data
        # cve_entries = {}
        # for cve in entry['vulns']:
        #     cve_entries[cve] = {}

        #     cve_entries[cve]['cvss'] = entry['vulns'][cve]['cvss']
        #     cve_entries[cve]['summary'] = entry['vulns'][cve]['summary']
        # filtered_entry['vulns'] = cve_entries

        filtered_entries.append(filtered_entry)
    print(len(filtered_entries))
    with open('prettified-cves.json', 'w') as f:
        json.dump(filtered_entries, f, indent=4)


vulnerable_matches = extract_vulnerable()
# print_software_and_version(vulnerable_matches)
filter_vulnerable(vulnerable_matches)


    





