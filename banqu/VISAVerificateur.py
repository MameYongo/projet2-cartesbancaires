from banqu.AlgoDeLuhn import Luhn
from banqu.Verificateur import Verificateur


class VisaVerificateur(Verificateur):
    def VerifierCarte(self, cardNumber):
        if(len(cardNumber)==15 & (cardNumber.startwith(14) | cardNumber.startwith(14))):
            Luhn(cardNumber)


        print("C'est une carte Visa")