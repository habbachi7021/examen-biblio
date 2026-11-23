#Gestion simple d'une bibleotheque
titre=input("titre du livre :")
exemplaires=int(input("Nombres d exemplaires"))
print("livre :",titre)
print("exemplaires :",exemplaires)


#emprunt d'unlivre
exemplaires=exemplaires-1
print("Apres emprunt :",exemplaires,"exemplaire(s) disponible(s)")