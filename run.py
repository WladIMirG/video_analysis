from fun import *

## ['run.py' <imagem> <tipo de filtro> <mode> <plano rgb> <imagem filtrada> <pt>

if __name__ == "__main__":
    print(sys.argv)
    if sys.argv[1][-4:]==".png":
        print("Iniciando...")