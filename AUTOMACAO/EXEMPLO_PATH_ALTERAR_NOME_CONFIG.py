#Comentário lab aula API Cisco
#Exemplo de como usar o PATH para modificar uma configuração, ver função 'def change_hostname():'

#! /usr/bin/env python

import requests
import json

# Check for module dependencies:
not_installed_modules = []

try:
    from requests.auth import HTTPBasicAuth
except ImportError:
    not_installed_modules.append("requests")
try:
    import yaml
except ImportError:
    not_installed_modules.append("PyYAML")


if not_installed_modules:
    print("Please install following Python modules:")

    for module in not_installed_modules:
        print("  - {module}").format(module=module)

    sys.exit(1)



requests.packages.urllib3.disable_warnings()


HTTP_HEADERS = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

HTTP_AUTH = HTTPBasicAuth("cisco", "cisco")


def get_inventory():

    inventory_file = "inventory.yml"
    with open(inventory_file) as fh:
        inventory = yaml.safe_load(fh)

    return inventory




def get_serial_data(host):

    url = (
        "https://{host}/restconf/data/Cisco-IOS-XE-native:native"
        "/license/udi/sn".format(host=host)
    )
    response = requests.get(url, headers=HTTP_HEADERS, auth=HTTP_AUTH, verify=False)
    result = json.loads(response.text)
    serial_data = result["Cisco-IOS-XE-native:sn"]
    return serial_data


def get_version_data(host):

    url = "https://{host}/restconf/data/Cisco-IOS-XE-native:native" "/version".format(
        host=host
    )
    response = requests.get(url, headers=HTTP_HEADERS, auth=HTTP_AUTH, verify=False)
    result = json.loads(response.text)
    version_data = result["Cisco-IOS-XE-native:version"]
    return version_data


def get_hostname(host):
    url = "https://{host}/restconf/data/Cisco-IOS-XE-native:native" "/hostname".format(
        host=host
    )
    response = requests.get(url, headers=HTTP_HEADERS, auth=HTTP_AUTH, verify=False)
    result = json.loads(response.text)
    hostname = result.get("Cisco-IOS-XE-native:hostname")

    return hostname


def structure_data():

    devices = {}
    net_inventory = get_inventory()
    for host in net_inventory:
        devices[host] = {}
        devices[host]["os_version"] = get_version_data(host)
        devices[host]["serial_number"] = get_serial_data(host)
        devices[host]["hostname"] = get_hostname(host)

    return devices

def change_hostname():

    hostname = input("Enter new hostname for R1: ")
    url = 'https://{host}/restconf/data/Cisco-IOS-XE-native:native' \
          '/hostname'.format(host="R1")
    hostname_payload = {"Cisco-IOS-XE-native:hostname": hostname}
    patch_response = requests.patch(url, auth=HTTP_AUTH, headers=HTTP_HEADERS, data=json.dumps(hostname_payload), verify=False)
    #Help in troubleshoot:
    if patch_response.status_code == 204:
        print("\nAPI Call was Successfully Executed...")
        print("\nType: PATCH")
        print("\nURL: {}".format(url))
        print("\nBODY:")
        print(json.dumps(hostname_payload, indent=4, sort_keys=True))
    else:
        print("Executed API Call Failed...")
        print("\nReturned Status Code: {}".format(patch_response.status_code))
        print("\nReason for Failure: {}".format(patch_response.reason))
        print("\nReturned Data: {}".format(patch_response.text))
        sys.exit(1)


def main():

    change = input( "Do you want to make a change to the hostname? [y/n]: ")
    if change.lower() == 'y':  
        change_hostname() 
    
    heading = "|{:^10} | {:^10} | {:^12} | {:^15}|".format(
        "Device", "Hostname", "OS Version", "Serial Number"
    )
    print(len(heading) * "-")
    print(heading)
    print(len(heading) * "-")
    for hostname, details in structure_data().items():

        print(
            "|{:^10} | {:^10} | {:^12} | {:^15}|".format(
                hostname,
                details["hostname"],
                details["os_version"],
                details["serial_number"],
            )
        )
        print(len(heading) * "-")




if __name__ == "__main__":
    main()
