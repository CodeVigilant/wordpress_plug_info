# wordpress_plug_info
Wordpress Plugin Information extractor

Output is ; seperate CSV style output

Output fields are as follow
1. Plugin Name
2. Plugin website status code
3. Status Message (gives reason in case plugin is closed)
4. Current Version
5. Last update date and Time
6. Total Download as per website
7. Download url for latest version

## Sample output

```
$ python3 wordpress_plugin_info.py --name wp-file-manager
wp-file-manager;200;'Plugin is Alive';'7.1';'2021-02-18 7:13am GMT';'9192091';'https://downloads.wordpress.org/plugin/wp-file-manager.zip'

$ python3 wordpress_plugin_info.py --name wp-filemanager
wp-filemanager;404;'This plugin has been closed and is no longer available for download.'
```

## Command Line options

```
usage: wordpress_plugin_info.py [-h] --name TARGET

Program to obtain information about Wordpress plugin

optional arguments:
  -h, --help     show this help message and exit
  --name TARGET  Provide Plugin name

Credit (C) Anant Shrivastava http://anantshri.info
```
