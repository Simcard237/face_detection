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
         
         print("je suis l encodage a entregistrer",face_recognition.face_encodings(image)[0])
         return face_recognition.face_encodings(image)[0]
    

    def _load_database_file(self,filepath):
       with open(filepath,"rb") as file:
            files=pickle.Unpickler(file)
            return files.load() 
       
        
    

    # ---------- Start Meta Function
    # _data_converter is the function that allow the image data saving
    #  - side: is a parameter that inform if we will save or load data
    
    def _data_convert(self,databasefilepath,case:str,imgpath:str):
        try:
           data=self._load_database_file(databasefilepath)
        except:data={}
        if case=="saving":
                data.update({f"{len(data)}":self._face_encoding(imgpath)})
                with open(databasefilepath,"wb") as file:
                    files=pickle.Pickler(file)
                    files.dump(data)
                return 1
        elif case=="loading":
           return data    
            
                 



    # this function save the face of the user
    # Output file is a csv file that represent the database
    # inputimggpath is the image path
    def face_saving(self,inputimggpath:str,outputfilepath:str):
       return self._data_convert(outputfilepath,"saving",inputimggpath)
   
    def load_images_saved(self,databasefilepath):
         data=self._data_convert(databasefilepath,"loading","")
         return list(data.values())
    
    
    def unknown_image_encodings(self,imagepath):
        image=self._load_image(imagepath)
        return face_recognition.face_locations(image), face_recognition.face_encodings(image,face_recognition.face_locations(image))
    
    def identification(self,databasefilepath,uknowimagepath):
         img,img1=self.unknown_image_encodings(uknowimagepath)
         for (haut,droite,bas,gauche), encodagevisage in zip(img,img1):
              corresp=face_recognition.compare_faces(self.load_images_saved(databasefilepath),encodagevisage)
              if True in corresp:      
               return corresp            


recognition=Facedetection()
recognition.face_saving("./images/frame_4.jpg","./bd.data")
print(recognition.identification("./bd.data","./images/frame_1.jpg"))

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
 
   
