#from BanqueCheck.src.bank.Luhalgo import Luhn
#from Verificateur import Verificateur
from banqu.AlgoDeLuhn import Luhn
from banqu.Verificateur import Verificateur


class MasterCardVerificateur(Verificateur):
    def VerifierCarte(self,cardNumber):
        if (len(cardNumber) == 16 & (cardNumber.startwith(41) | cardNumber.startwith(40))):
            Luhn(cardNumber)

        print("C'est une carte Mastercard")
        print("Carte invalide")

