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
     error=[]
     paused=[]
     month=["JAN14","FEB14","MARCH14","APRIL14","MAY14","JUNE14","JULY14","AUG14","SEPT14","OCT14","NOV14"]
     #All long challenges of codechef
     month2=["JAN14"]
     for j in month2:
         folder_path=j;
         new_path=current_path+" "+folder_path # finding path of contest
         if os.path.isdir(folder_path):
              shutil.rmtree(folder_path) # delete an existing folder with same name
         os.mkdir(folder_path) #create similar folders in the hard drive
         os.chdir(folder_path)    
         f = FileDownloader()
         url="http://www.codechef.com/"+j+"/" # Codechef contest URL
         e=f.startDownload(url,"Contest "+j+" problems") # to read each of the pdf files and copy the same
         folder_path="problems" #finding the path of problems in a particular contest
         new_path=new_path+folder_path
         if os.path.isdir(new_path):
              shutil.rmtree(new_path) # delete an existing folder with same name
         os.mkdir(new_path) #create similar folders in the hard drive
         os.chdir(new_path)
         print j+" is starting to download\n\n\n"
         url="http://www.codechef.com/"+j+"/" #downloading indivisual problems from each contest
         source_html= urllib2.urlopen(url).readlines()
         req_str='<td ><a href'
         k=0
         for i in source_html:
             if req_str in i:
                 q=i.rfind("/");
                 if q==-1: #report error if file not available 
                     print "Error downoading "+i
                 else:
                     problem_code[k]=i[q+1:-3]
                     k+=1;
                     print "\n Extracting problem "+problem_code # extract problem code for file name 
         for w in problem_code:
             url=url+w+"/"
             f = FileDownloader() #run file Downlaode to manage file downloads indiviually
             e=f.startDownload(url,w)
             if e==1:
                 pair=(j,i) # report error if the file was not able to download
                 error.append(pair)
             elif e==2:
                 pair=(j,i) # report error if the file was paused 
                 paused.append(pair)   
             print "\n\n\n@@@@@@@@@@@@@@ All problems of "+ j +" Download @@@@@@@@@@@@@@@@"  # Inform when each problem is downoaded
     if len(error)==0 and len(paused)==0:
         print "\n\n\n################## Completed Download Successfully !!!!!!!!! ##########################"  # Inform when each contest is downoaded
     if len(error)>0:
         print "\n\n\n Could Not successfully Download the following features\n\n\n"  # report if a file could not be successfully downloaded
         for counter in error:
             print "The file %d present in %d directory Could not be downloaded Sccessfully" %(counter[1],counter[0])
     if len(paused)>0:
         print "\n\n\n Paused Downloads are \n\n\n"
         for counter in paused: # report files which are paused
             print "The file %d present in %d directory is paused" %(counter[1],counter[0])
if __name__ == "__main__":
    main()
