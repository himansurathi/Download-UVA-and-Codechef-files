# Download-UVA-files
Download all the problems of UVA Judge from its online set

There is a collection of all problems in pdf format available in this link:

https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=1

The problems of Uva online judge are structured in various folders and where numbered sequentially. 
The main aim of this small python script is to successfully 
download all the problem files in pdf format in our computer hard drive.

Motivation

I was quite interested in competitive programming and wanted to solve as many 
problems of UVA to enhance my coding skills and become a  better programmer. 
So a thought crossed my mind that why not download all the problems available in UVA 
in pdf format so that I would be able to at least think and read problems even in off-line 
mode.
	Recently I had learnt python and realised that it has various libraries for helping 
me achieve the same

Version 1

Requirements 

Python 2.7.4 must be installed in the machine to run this script.
Optional- Python should be added in your path or it should be set 
as environment variable 

Running the script 

One can simply run python <name of file>.py in a command window to start downloading each of the pdf files.
Moreover after completion of download you will be notified and you can start solving the 
UVA problems. 

The following are the features:

1. The pdf files will be downloaded in slots of folders like 1-100 files in a single folder, 2- 100 in another problem and so on....
2. Use of urlib2 of python to open each of the pdf files individually so that we can read them.	
3. Informing about each successful download of individual pdf file, each directory download is completed as well as when the total download is also completed.
4. Generic URL of all pdf files: http://uva.onlinejudge.org/external/<jth folder>/<ith file>.pdf 

Testing Environment 

It was tested on Windows 8.1 as well as Linux (Ubuntu 14.04) operating system with python 2.7.4
installed in the machine.