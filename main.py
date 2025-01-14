import pyfiglet

def ascii_art_generator():
    text = input("Entrez le texte que vous souhaitez convertir en art ASCII : ")
    
    ascii_art = pyfiglet.figlet_format(text)
    
    print("\nVoici votre art ASCII :\n")
    print(ascii_art)

if __name__ == "__main__":
    ascii_art_generator()
