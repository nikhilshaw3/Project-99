import os
import shutil
import time

path=input("Enter path of the folder .")
days=0
seconds=time.time()-(days*24*60*60)


if (os.path.exists(path)):
    for root,dirs,files in os.walk(path,topdown=True):
        for name in files:
            path=os.path.join(root,name)
            ctime=os.stat(path).st_ctime
            
            
            

            if (seconds>=ctime):
                os.remove(path)
                print("\n Deleted the path" + path + "successfully")

                

        for name in dirs:
            path = os.path.join(root, name)
            ctime = os.stat(path).st_ctime

            

            if (seconds >= ctime):
                shutil.rmtree(path)
                print("\n Deleted the path " + path + " successfully")


else:
    print("\n Path not found")
