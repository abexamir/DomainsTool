import re
from socket import gethostbyname, gaierror
import argparse
import os
import sys
# from lxml import html
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i",
    "--input-file", dest="input_file", help="path to file containing domains")
    parser.add_argument("-r",
    "--report", type=bool, const=True, nargs='?', help="full report needed or not")
    parser.add_argument("-t",
    "--target", dest="special_host", required=False, help="host to get all domains on")
    parser.add_argument("-v",
    "--verbose", type=bool, const=False, nargs='?', help="Complete report showing which domain is on which host")
    # parser.add_argument("-s",
    # "--simple", type=bool, const=False, nargs='?', help="get output simple line by line")
   
  

    args = parser.parse_args()

    if not args.input_file:
        parser.error("[-] Please specify the path to file containing domains")
    if not os.path.exists(os.path.abspath(args.input_file)):
        parser.error("The file '{}' does not exist!".format(args.input_file))
        sys.exit(1)
    return args

def get_clear_domains(domains):
    httpsDomains = [i for i in domains if (re.match(r"^https", i))]
    httpDomains = [i for i in domains if ((re.match(r"^http", i)) and (i not in httpsDomains))]
    cleanDomains = [i for i in domains if ((i not in httpDomains) and (i not in httpsDomains))]

    cleanHttpsDomains = [i[8:len(i)] for i in httpsDomains]
    cleanHttpDomains = [i[7:len(i)] for i in httpDomains]

    allDomains = []
    for sublist in cleanDomains, cleanHttpDomains, cleanHttpsDomains:
        for item in sublist:
            allDomains.append(item)

    domainsParts = []
    clearDomains = []
    for i in allDomains:
        domainsParts.append(i.partition('/'))
    for i in domainsParts:
        clearDomains.append(i[0])

    return clearDomains

def make_host_domain_pair(clearUrls):
    pair = []
    domains_to_nowhere = []

    for i in range(len(clearUrls)):
        try:
            pair.append([clearUrls[i], gethostbyname(clearUrls[i])])
        except(gaierror):
            domains_to_nowhere.append(clearUrls[i])
            continue
            # print ("domain", pair[i][0], "is on", pair[i][1])

    return pair, domains_to_nowhere

def get_hosts(pair):
    hosts = [row[1] for row in pair]
    sorted_unique_hosts = sorted(set(hosts), key=hosts.count, reverse = True)
    return hosts, sorted_unique_hosts

def get_domains_of_a_host(host):
    domains_of_host = []
    for row in host_domain_pair:
        if row[1] == host:
            domains_of_host.append(row[0])
    return domains_of_host


def banner(text, ch='=', length=78):
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    return banner

options = get_arguments()

print("\n", banner("Domains Tool"))
print("\n\n\t\tA Tool to check all domains given in a text file\n\t\t   and associate them with corresponding host.\n\n\t\t     input file can be the output of sublist3r\n\n\n\t\t\t     Written by Amir Serati\n\n")

inputDomains = [i for i in open(str(options.input_file)).read().splitlines() if len(i) > 2]
domains = get_clear_domains(inputDomains)
host_domain_pair = make_host_domain_pair(domains)[0]
# dead_domains = make_host_domain_pair [1]

all_hosts = get_hosts(host_domain_pair)[0]
unique_hosts = get_hosts(host_domain_pair)[1]

if options.report:
    # print ("\n\t-----------------------\n\t\tSummary\n\t-----------------------\n")
    print(banner("Summary"))
    print ("\tThere are ", len(domains), " domains served on ", len(unique_hosts), " hosts\n" )
    for host in unique_hosts:
        print("\t[+] "+ "host"+ "\t"+ host+ "\t"+ "serves"+ "\t"+ str(all_hosts.count(host))+ "\t"+ "domains.\n")

if options.verbose:
    print(banner("Verbose Report"), "\n")
    for i in range(len(domains)):
        print ("\t\tdomain", host_domain_pair[i][0], "is on", host_domain_pair[i][1])

if options.special_host:
    domains_of_host = get_domains_of_a_host(str(options.special_host))
    print(banner("domains on host {}".format(options.special_host)), "\n")
    # print("\n\t------------------------------\n\tdomains on host {}\n\t------------------------------\n".format(options.special_host))
    for i in  range(len(domains_of_host)):
        print("\t\t\t", i+1, " ", domains_of_host[i])

# for ip in unique_hosts:
#     print (ip)

# for domain in domains:
#     print (domain)
#     try:
#         t = html.parse(domain)
#         print (t.find(".//title").text)
#     except:
#         continue