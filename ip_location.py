#!/usr/bin/python
'''
	IP Location and Mass IP Location
	Date: 12 NOV 2017 - 15:17
	Respect:  YC - HighTech - EOF Club - Brian - d3m0l1d0r - Cater - Strike - rCent
             Kodo - pr0s3x - CrazyDuck - xin0x - mmxm - CriptonKing - d3z3n0v3 - c0de_universal - All Friends
'''

import requests
import json
import argparse as arg
import sys 
import os as sistema
 
sistema.system("cls" if sistema.name == "nt" else "reset")

parser = arg.ArgumentParser()
parser.add_argument("-i", "--ip", action="store", help="Select target IP")
parser.add_argument("-l", "--list", action="store",  help="Select target IP list")
parser.add_argument("-s", "--save", action="store", help="Select where the tested ips will be saved")
param = parser.parse_args()

save_ = param.save
mass_ = param.list
	
menu = """
       *                  ((((        *       *
*            *        *  (((
       *    Coded       (((      *
  *   / \      *   by  *(((           *
   __/___\__  *          (((
    | (O) |    v4p0r *    ((((                  *
* __| :-: |__ ... .. .             *.     ... .
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 # IP Location and Mass IP Location v1
 # Coder: v4p0r
 # Team: Yunkers Crew
 # Skype: drx.priv
 # Twitter: 0x777null
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 # [+] Usage:
 # python ip_location.py --help
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""

banner_single = """
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 # Search IP 
 # I hope this helps you
 # By v4p0r
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""

banner_mass = """
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 # Search IP List 
 # I hope this helps you
 # By v4p0r
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""

if len(sys.argv) == 1:
	print(menu)
	exit()
	
def main():

	try:
		single_api = "http://ip-api.com/json/{}" . format(param.ip)
		req = requests.get(single_api)
		single_info = json.loads(req.text)
	except:
		print('[!] Error in connection')
		exit()
		
	if mass_:
		print(banner_mass)
		ips_ = mass_
		arquivo = open(ips_)
		lines = arquivo.readlines()
		lines = [ip.replace("\n", "") for ip in lines]
		
		for ip in lines:
			try:
				mass_search(ip)
			except:
				print('[-] Invalid IP Adress')
	else: 
		print(banner_single)
		single_search(single_info)

def single_search(single_info):

	try:
		lista_ = []
		print("\n[+] IP: {} \n[+] ORG: {}\n[+] ISP: {}\n[+] AS: {}\n[+] COUNTRY CODE: {}\n[+] COUNTRY: {}\n[+] REGION: {}\n[+] REGION NAME: {}\n[+] CITY: {}\n[+] TIME ZONE: {}\n[+] LATITUDE: {}\n[+] LONGITUDE: {}\n".format(single_info["query"], single_info["org"], single_info["isp"], single_info["as"], single_info["countryCode"], single_info["country"], single_info["region"], single_info["regionName"], single_info["city"], single_info["timezone"], single_info["lat"], single_info["lon"]))
		lista_.append("\n[+] IP: {} \n[+] ORG: {}\n[+] ISP: {}\n[+] AS: {}\n[+] COUNTRY CODE: {}\n[+] COUNTRY: {}\n[+] REGION: {}\n[+] REGION NAME: {}\n[+] CITY: {}\n[+] TIME ZONE: {}\n[+] LATITUDE: {}\n[+] LONGITUDE: {}\n".format(single_info["query"], single_info["org"], single_info["isp"], single_info["as"], single_info["countryCode"], single_info["country"], single_info["region"], single_info["regionName"], single_info["city"], single_info["timezone"], single_info["lat"], single_info["lon"]))
	except:
		print('[-] Invalid IP Adress')
	
	if save_: 
		save_resultados(lista_)
	
def mass_search(ip):

	lista_ = []
	mass_api = "http://ip-api.com/json/" + ip
	mass_req = requests.get(mass_api)
	mass_info = json.loads(mass_req.text)
	print("\n[+] IP: {} \n[+] ORG: {}\n[+] ISP: {}\n[+] AS: {}\n[+] COUNTRY CODE: {}\n[+] COUNTRY: {}\n[+] REGION: {}\n[+] REGION NAME: {}\n[+] CITY: {}\n[+] TIME ZONE: {}\n[+] LATITUDE: {}\n[+] LONGITUDE: {}\n".format(mass_info["query"], mass_info["org"], mass_info["isp"], mass_info["as"], mass_info["countryCode"], mass_info["country"], mass_info["region"], mass_info["regionName"], mass_info["city"], mass_info["timezone"], mass_info["lat"], mass_info["lon"]))
	lista_.append("\n[+] IP: {} \n[+] ORG: {}\n[+] ISP: {}\n[+] AS: {}\n[+] COUNTRY CODE: {}\n[+] COUNTRY: {}\n[+] REGION: {}\n[+] REGION NAME: {}\n[+] CITY: {}\n[+] TIME ZONE: {}\n[+] LATITUDE: {}\n[+] LONGITUDE: {}\n".format(mass_info["query"], mass_info["org"], mass_info["isp"], mass_info["as"], mass_info["countryCode"], mass_info["country"], mass_info["region"], mass_info["regionName"], mass_info["city"], mass_info["timezone"], mass_info["lat"], mass_info["lon"]))
	
	if save_: 
		save_resultados(lista_)


def save_resultados(list_ip):

	print("[*] Save results...")
	print("[*] =========================================== [*]")
	file = open(save_, "a")
	file = [file.write(str(x_ip) + "\n") for x_ip in list_ip]

try:
	main()
except KeyboardInterrupt: 
	exit()
