import os
import pickle


path=os.getcwd().replace("\\","/")+"/static/assets/data/db.data"

with open("D:/projetditros/Erness/vue/env/Scripts/project1/static/assets/data/db.data","rb") as file:
    fils=pickle.Unpickler(file)
    print(len(fils.load()))