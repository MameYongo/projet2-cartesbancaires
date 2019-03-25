from banqu.Banque import Banque
from banqu.Verificateur import Verificateur

if __name__ == "__main__":
    c = input ( "Veuiller saisir votre numero de carte " )
    v=Verificateur()
    m=Banque(v)
    m.verification(c)