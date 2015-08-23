# Script to download UVA Files

import urllib2 # needed for functions,classed for opening urls.
import os
import shutil
 
class FileDownloader(object): # class to handle downloads of file 
 
    def __init__(self): # properties of file
        self.url = None  #stores the url of the file 
        self.progress = None #stroes the progress status 
        self.status = None # {0:"Downloading", 1:"Completed", 2:"Paused", 3:"Error"}
        self.fileName = None #stores the name of the file 
        self.u = None
        self.fileSize = None # stores the size of file
        self.szDownloaded = 0 # stores the size of file downoaded
        self.isPaused = False #stores the status of file if paused or not
        self.directory=0  #stores the directory of the file     
      
    def startDownload(self, url, start=None):
        try:        
            self.isPaused = False #update the pause status
            self.url = url # update the url of file 
            self.fileName = url.split("/")[-1] # segregate the file name from URl 
            if start is not None:
                req = urllib2.Request(url)
                req.headers["Range"] = "bytes=%s-%s" %(start, self.fileSize) #Percentage of file downloaded
                self.u = urllib2.urlopen(req)
            else:
                self.u = urllib2.urlopen(url)
     
            f = open(self.fileName, "ab") # read the file 
            self.fileSize = int(self.u.info().getheaders("Content-Length")[0]) #store the file size 
     
            self.szDownloaded = 0
            if start is not None:
                self.szDownloaded = start
            block_sz = 8192 #read 8192 bytes of file
            while True:
                buff = self.u.read(block_sz) #read the whole file using blocks of 8192 bytes
                if not buff:
                    self.status = 1
                    break
                self.szDownloaded += len(buff) # update the size of file downloaded
                f.write(buff)
                self.status = 0 # update the status of the file 
                download_status=self.szDownloaded * 100.00 / self.fileSize # Simple mathematics
                print "%.2f done" %(download_status),
                download_status = int((download_status + download_status +1)/4) * chr(8) #shows donload progress bar 
                print download_status # show download 
                if self.isPaused is True: #check if the file has been paused
                    err=2                    
                    break
            err=0
            f.close()
        except urllib2.HTTPError,e:#error handling 
            if e.code == 404:  # Error when page not found 
                print "Page not found!"
            elif e.code == 403: # Error when acccess is denied 
                print "Access denied!"
            else:
                print "Check Your internet connection!!", err.code # error if internet is not coming
            err=1
        except urllib2.URLError,e:
            print "No internet Connection", e.reason
            err=1
        return err
    
    def pauseDownload(self):
        self.isPaused = True  #to pause the donload of file 
        #save a file with the download status, then I'll be able to resume it
 
    def resumeDownload(self):
        self.isPaused = False #to resume the download of the file 
        self.startDownload(self.url, self.szDownloaded)
 
def main():
     current_path=os.getcwd() # To get the current directory 
     foldlow=1
     foldhigh=18 # There were 18 folders in UVA online Judge
     j=foldlow
     error=[]
     paused=[]
     for j in range(foldlow,foldhigh):
         p=j*100
         folder_path=str(p)+"-"+str(p+100)
         new_path=current_path+folder_path
         if os.path.isdir(new_path):
              shutil.rmtree(new_path) # delete an existing folder with same name
         os.mkdir(new_path) #create similar folders in the hard drive
         os.chdir(new_path)    
         for i in range(p,p+2):
             url="http://uva.onlinejudge.org/external/"+str(j)+"/"+str(i)+".pdf"
             f = FileDownloader()
             e=f.startDownload(url) # to read each of the pdf files and copy the same
             if e==1:
                 pair=(j,i)
                 error.append(pair) # report error if the file was not able to download
             elif e==2:
                 pair=(j,i)
                 paused.append(pair)  # report error if the file was paused 
         print "\n\n\n@@@@@@@@@@@@@@ Directory "+str(j)+" Download @@@@@@@@@@@@@@@@"  # Inform when each directory is downoaded
     if len(error)==0 and len(paused)==0:
         print "\n\n\n################## Completed Download Successfully !!!!!!!!! ##########################" # Inform when download is completed
     if len(error)>0:
         print "\n\n\n Could Not successfully Download the following features\n\n\n"
         for counter in error:
             print "The file %d present in %d directory Could not be downloaded Sccessfully" %(counter[1],counter[0]) #report error for all files c=which could not be downloaded
#download_url="http://uva.onlinejudge.org/external/2/221.pdf"
     if len(paused)>0:
         print "\n\n\n Paused Downloads are \n\n\n" #paused downloads
         for counter in paused:
             print "The file %d present in %d directory is paused" %(counter[1],counter[0]) #report the downloads that have been paused

if __name__ == "__main__":
    main()
