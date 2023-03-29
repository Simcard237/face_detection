from PIL import Image, ImageDraw
import face_recognition
import numpy as np
import pandas as pd
import pickle

class Facedetection:


    def __init__(self):
       self._image=None
       self._imagedata=None
   

    #load Image 
    def _load_image(self,imagepath):
        return face_recognition.load_image_file(imagepath)
   

    def _face_encoding(self,imagepath:str):
         image=self._load_image(imagepath)
         return face_recognition.face_encodings(image)[0]
    

    def _load_database_file(self,filepath):
       files=""
       with open(filepath,"rb") as file:
            files=pickle.Unpickler(file)
            files=files.load()
       return files
       
        
    

    # ---------- Start Meta Function
    # _data_converter is the function that allow the saving of the image data 
    #  - side: is a parameter that inform if we will save or load data
    
    def _data_convert(self,databasefilepath,case:str,imgpath:str,id):
        data={}
        try:
           with open(databasefilepath,"rb") as file:
                files=pickle.Unpickler(file)
                data=files.load()
        except:pass
        print("je suis data ",data)
        if case=="saving":
                data.update({f"{id}":self._face_encoding(imgpath)})
                print("je suis data 2 ", data)
                print("je suis len data 2 ", len(data))
                
                with open(databasefilepath,"wb") as file:
                    files=pickle.Pickler(file)
                    files.dump(data)
                return 1
        elif case=="loading":
           return data    
            
                 



    # this function save the face of the user
    # Output file is a csv file that represent the database
    # inputimggpath is the image path
    def face_saving(self,inputimggpath:str,outputfilepath:str,id):
       try: 
           if len(self._data_convert(outputfilepath,"loading","",0))!=0:
               
               int("a")
       except:  
        try:  
        
         return self._data_convert(outputfilepath,"saving",inputimggpath,id)
        
        except: return 2
    def load_images_saved(self,databasefilepath):
         data=self._data_convert(databasefilepath,"loading","",0)
         return data
    
    
    def unknown_image_encodings(self,imagepath):
        image=self._load_image(imagepath)
        return face_recognition.face_locations(image), face_recognition.face_encodings(image,face_recognition.face_locations(image))
    
    def identification(self,databasefilepath,uknowimagepath):
         img,img1=self.unknown_image_encodings(uknowimagepath)
         for (haut,droite,bas,gauche), encodagevisage in zip(img,img1):
              li=self.load_images_saved(databasefilepath)
              corresp=face_recognition.compare_faces(list(li.values()),encodagevisage)
              if True in corresp:  
                 
                 indexs=[list(li.values())[corresp.index(i)] for i in corresp if i==True] 
                #  for i in list(li.keys()):
                #      if np.array_equal(indexs[0],li[i]):
                #          position=list(li.values()).index(indexs[0])
                 return [i for i in li.keys() if np.array_equal(indexs[0],li[i])]          
              return 0

#recognition=Facedetection()
#recognition.face_saving("./images/frame_4.jpg","./bd.data")
#print(recognition.identification("..assets/data/bd.data","./images/frame_0.jpg"))

#  image=face_recognition.load_image_file("images.jpeg")
#     encodagevisage=face_recognition.face_encodings(image)[0]
#     encoddagevisage_connu=[
#     encodagevisage]

# nomvisage=["lady gaga"]



# imageinconnu=face_recognition.load_image_file("./imgtest/img.jpeg")

# emp_visage_inconnu=face_recognition.face_locations(imageinconnu)
# encodagevisage_inconnu=face_recognition.face_encodings(imageinconnu,emp_visage_inconnu
# )




# for (haut,droite,bas,gauche), encodagevisage in zip(emp_visage_inconnu,encodagevisage_inconnu):
#     corresp=face_recognition.compare_faces(encoddagevisage_connu,encodagevisage)
#     nom="Inconnu"
#     distances_visage=face_recognition.face_distance(encodagevisage_connu,encodagevisage)
#     meilleur_indice=np.argmin(distances_visage)
 
   
