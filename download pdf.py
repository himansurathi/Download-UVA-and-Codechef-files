import urllib2
import os
import shutil
def main():
     current_path=os.getcwd() # To get the current directory 
     foldlow=1
     foldhigh=18 # There were 18 folders in UVA online Judge
     j=foldlow
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
             download_file("http://uva.onlinejudge.org/external/"+str(j)+"/"+str(i)+".pdf",i) # to read each of the pdf files and copy the same
         print "\n\n@@@@@@@@@@@@@@ Directory "+str(j)+" Download @@@@@@@@@@@@@@@@" # Inform when each directory is downoaded
     print "\n\n\n################## Completed Download !!!!!!!!! ##########################" # Inform when download is completed

def download_file(download_url,i):
    response = urllib2.urlopen(download_url) # call the URL necessary
    file = open("Problem"+str(i)+".pdf", 'w') # open the file in pdf format
    file.write(response.read()) # write the pdf file in your hard drive with same name as your file name 
    file.close()
    print("Completed "+str(i)+"th file download") # complete the ith file download and inform about the same

if __name__ == "__main__":
    main()
    
 
