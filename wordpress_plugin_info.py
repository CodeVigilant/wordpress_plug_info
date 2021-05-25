#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import sys
import argparse
import datetime
import json
url_to_use="https://wordpress.org/plugins/"
api_url="https://api.wordpress.org/plugins/info/1.0/"


def get_details(plug_name):
	r=requests.get(api_url + plug_name + ".json")
	if r.status_code == 404:
		url_to_check=url_to_use + plug_name + "/"
		r1=requests.get(url_to_check)
		soup = BeautifulSoup(r1.content,'html.parser')
		reason=soup.find(class_='plugin-notice')
		#return reason.text
		response = plug_name + ";404;'" + reason.text + "'"
	else:
		if r.status_code == 200:
			plug_info = json.loads(r.content)
			response = plug_name + ";" + str(r.status_code) + ";'Plugin is Alive';'" + plug_info['version'] + "';'" + plug_info['last_updated'] + "';'" + str(plug_info['downloaded']) + "';'" + plug_info['download_link'] + "'"
		else:
			respose = plug_name + ";" + str(r.status_code)
	return response


def main(argv):
	desc="""Program to obtain information about Wordpress plugin"""
	epilog="""Credit (C) Anant Shrivastava http://anantshri.info"""
	parser = argparse.ArgumentParser(description=desc,epilog=epilog)
	parser.add_argument("--name",help="Provide Plugin name",dest='target',required=True)
	x=parser.parse_args()
	plug_name=x.target
	print(get_details(plug_name))

if __name__ == "__main__":
	main(sys.argv[1:])
