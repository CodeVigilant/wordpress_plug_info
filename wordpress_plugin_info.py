#!/usr/bin/python2.7
import requests
from BeautifulSoup import BeautifulSoup
import sys
import argparse
import datetime
url_to_use="http://www.wordpress.org/plugins/"
api_url="http://api.wordpress.org/plugins/info/1.0/"
def to_string(data):
	out = ""
	if type(data) is unicode:
		out = data.encode('utf8')
	elif type(data) is int:
		out = str(data)
	else:
		out=str(data)
	if type(out) is str:
		return out
	else:
		return type(out)
		to_string(out)

def get_api_details(plug_name):
	print "Not yet Implemented"
	#r= requests.get(api_url + plug_name + ".xml")
	#print r.text


def get_details(plug_name):
	r=requests.get(url_to_use + plug_name)
	if r.status_code == 200:
		souper=BeautifulSoup(r.content) 
		comp=""
		req=""
		data_sent=""
		abc=souper.findAll("div",{"class":"plugin-contributor-info"})
		cba = souper.findAll("div",{"class":"plugin-contributor-info no-profile"})
		auth_name=""
		for x in abc:
			auth_name=auth_name + x.find('div').text + ":"
		for x in cba:
			auth_name=auth_name + x.find('div').text + ":"
		auth_name = auth_name[:-1]
		stri=souper.find("div",{"class":"col-3"})
		if stri is not None:
			wpver_req=str(stri.find("p")).splitlines()
			for z in wpver_req:
				if z.find("Require") > -1:
					req=str(z[int(z.find("</strong>"))+9:int(z.find("<br/>"))-5])
				if z.find("Compatible") > -1:
					comp=str(z[int(z.find("</strong>"))+9:int(z.find("<br/>"))-5]).decode("ascii","ignore")
				disabled = str(souper.find('div',{"id":"plugin-title"})).find('disabled')
				if disabled > 0:
					return '"' + plug_name + '","Disabled"'
				download_count=souper.find('meta',{"itemprop":"interactionCount"})['content'].split(':',1)[1]
				date_mod=souper.find('meta',{"itemprop":"dateModified"})['content']
				version_no=souper.find('meta',{"itemprop":"softwareVersion"})
				#['content']
				if version_no is not None:
					version_no = version_no['content']
		down_me=souper.find('a',{"itemprop":"downloadUrl"})
		if down_me is None:
			downme = None
		else:
			downme = down_me['href']
		#['href']
		if downme is None:
			downme=""
			if download_count is None:
					download_count="0"
			if date_mod is None:
				date_mod=""
			if version_no is None:
				version_no=str('0')
		data_sent= '"' + to_string(plug_name) + '","Published","' + to_string(datetime.datetime.now()) + '","' + to_string(date_mod) + '","' + to_string(version_no) + '","' + to_string(download_count) + '","' + to_string(comp) + '","' +  to_string(req) + '","' + to_string(auth_name) + '","' + to_string(downme) + '"'
		return data_sent
	else:
		return '"' + plug_name + '","Not published"'	

def main(argv):
	desc="""Program to obtain information about Wordpress plugin"""
	epilog="""Credit (C) Anant Shrivastava http://anantshri.info"""
	parser = argparse.ArgumentParser(description=desc,epilog=epilog)
	parser.add_argument("--name",help="Provide Plugin name",dest='target',required=True)
	parser.add_argument("--api",help="Use Wordpress API",action="store_true")
	parser.add_argument("--header",help="Print header",action="store_true")
	x=parser.parse_args()
	api=x.api
	plug_name=x.target
	header=x.header
	
	if header:
		print "Plugin_name,Status,Timestamp,Last_mod_date,Version_NO,Download_count,Compatible_version,minimum_required,author_names,download_url"
	if api:
		print get_api_details(plug_name) 
	else:
		print get_details(plug_name)


if __name__ == "__main__":
	main(sys.argv[1:])
