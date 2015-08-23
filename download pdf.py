import urllib2                                                # needed for functions,classed for opening urls.
import os
import shutil


def main():
     current_path=os.getcwd() # To get the current directory 
     foldlow=1
     foldhigh=18 # There were 18 folders in UVA online Judge
     j=foldlow
     error=[]
     for j in range(foldlow,foldhigh):
         p=j*100
         folder_path=str(p)+"-"+str(p+100)
         #new_path=folder_path
         new_path=current_path+folder_path
         if os.path.isdir(new_path):
              shutil.rmtree(new_path) # delete an existing folder with same name
         os.mkdir(new_path) #create similar folders in the hard drive
         os.chdir(new_path)    
         for i in range(p,p+100):
             url="http://uva.onlinejudge.org/external/"+str(j)+"/"+str(i)+".pdf"
             e=download_file(url,i)  # to read each of the pdf files and copy the same
             if e==1:
                 pair=(j,i)  # report error if the file was not able to download
                 error.append(pair)
         print "\n\n\n@@@@@@@@@@@@@@ Directory "+str(j)+" Download @@@@@@@@@@@@@@@@"  # Inform when each directory is downoaded
     if len(error)==0:
         print "\n\n\n################## Completed Download Successfully !!!!!!!!! ##########################" # Inform when download is completed
     else:
         print "\n\n\n Could Not successfuly Download the following features\n\n\n"
         for counter in error:
             print "The file %d present in %d directory Could not be downloaded Sccessfully" %(counter[1],counter[0]) #report error for all files c=which could not be downloaded
#download_url="http://uva.onlinejudge.org/external/2/221.pdf"
#i=221
def download_file(download_url,i):
    usock=[]
    try:
         usock = urllib2.urlopen(download_url)                                  #function for opening desired url
         file_name = download_url.split('/')[-1]                                #Example : for given url "www.cs.berkeley.edu/~vazirani/algorithms/chap6.pdf" file_name will store "chap6.pdf"
         f = open(file_name, 'wb')                                              #opening file for write and that too in binary mode.
         file_size = int(usock.info().getheaders("Content-Length")[0])          #getting size in bytes of file(pdf,mp3...)
         print "\nDownloading: %s Bytes: %s " % (file_name, file_size)
         downloaded = 0
         block_size = 8192                                            #bytes to be downloaded in each loop till file pointer does not return eof
         while True:
             buff = usock.read(block_size)
             if not buff:                                             #file pointer reached the eof
                break
             downloaded = downloaded + len(buff)
             f.write(buff)  
             download_status = downloaded * 100.00 / file_size #Simple mathematics
             print "%.2f done" %(download_status),  # shows download bar in command line
             download_status = int((download_status + download_status +1)/4) * chr(8)
             print download_status # show download 
         f.close()
         print("Completed "+str(i)+"th file download\n")
         err=0
    except urllib2.HTTPError,e: #error handling 
        if e.code == 404: # Error when page not found 
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
    

if __name__ == "__main__":
    main()
