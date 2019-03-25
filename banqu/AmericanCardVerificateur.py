from banqu.AlgoDeLuhn import Luhn
from banqu.Verificateur import Verificateur


class AmericanCardVerificateur(Verificateur):
    def VerifierCarte(self):
        def VerifierCarte(self, cardNumber):
            if (len(cardNumber) == 17 & (cardNumber.startwith(39) | cardNumber.startwith(30))):
                Luhn(cardNumber)

            print("C'est une carte American Express")
            print(" La Carte invalide")

