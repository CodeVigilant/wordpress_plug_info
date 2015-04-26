# wordpress_plug_info
Wordpress Plugin Information extractor

## Sample output

```
$ python wordpress_plugin_info.py --name wp-filemanager --header
Plugin_name,Status,Timestamp,Last_mod_date,Version_NO,Download_count,Compatible_version,minimum_required,author_names,download_url
"wp-filemanager","Published","2015-04-25 21:54:58.021044","2013-5-17","1.4.0","143797"," 3.5.2"," 3.2 or higher","anantshri:J","https://downloads.wordpress.org/plugin/wp-filemanager.1.4.0.zip"
```

## Command Line options

```
usage: wordpress_plugin_info.py [-h] --name TARGET [--api] [--header]

Program to obtain information about Wordpress plugin

optional arguments:
  -h, --help     show this help message and exit
  --name TARGET  Provide Plugin name
  --api          Use Wordpress API
  --header       Print header

Credit (C) Anant Shrivastava http://anantshri.info
```
