1. Bereken de fout in de laatste laag:
   - `self.dz2 = self.a2 - y`, waarbij `self.a2` de activaties van de laatste laag zijn en `y` de werkelijke waarden zijn. Dit berekent het verschil tussen de voorspelde activaties en de werkelijke waarden.

2. Bereken de partiële afgeleiden van de gewichten en biases in de laatste laag:
   - `self.dW2 = (1 / m) * np.dot(self.a1.T, self.dz2)`, waarbij `m` het aantal voorbeelden in de trainingsdata is. Dit berekent de gemiddelde verandering van de gewichten in de laatste laag ten opzichte van de fout in de uitvoerlaag.
   - `self.db2 = (1 / m) * np.sum(self.dz2, axis=0, keepdims=True)`. Dit berekent de gemiddelde verandering van de biases in de laatste laag ten opzichte van de fout in de uitvoerlaag.

3. Bereken de fout in de verborgen laag:
   - `self.dz1 = np.dot(self.dz2, self.W2.T) * (self.a1 > 0)`, waarbij `self.a1` de activaties van de verborgen laag zijn. Dit berekent de fout in de verborgen laag door het gewogen verschil tussen de fout in de uitvoerlaag en de activaties van de verborgen laag te nemen. De `(self.a1 > 0)`-term wordt gebruikt om de ReLU-activatiefunctie af te leiden.

4. Bereken de partiële afgeleiden van de gewichten en biases in de verborgen laag:
   - `self.dW1 = (1 / m) * np.dot(X.T, self.dz1)`, waarbij `X` de invoerkenmerken zijn. Dit berekent de gemiddelde verandering van de gewichten in de verborgen laag ten opzichte van de fout in de verborgen laag.
   - `self.db1 = (1 / m) * np.sum(self.dz1, axis=0, keepdims=True)`. Dit berekent de gemiddelde verandering van de biases in de verborgen laag ten opzichte van de fout in de verborgen laag.

5. Pas de gewichten en biases aan door het product van de partiële afgeleiden en de leersnelheid van het netwerk:
   - `self.W2 -= learning_rate * self.dW2`. Dit past de gewichten van de laatste laag aan door de partiële afgeleiden te vermenigvuldigen met de leersnelheid en van de huidige gewichten af te trekken.
   - `self.b2 -= learning_rate * self.db2`. Dit past de biases van de laatste laag op een vergelijkbare manier aan.
   - `self.W1 -= learning_rate * self.dW1`. Dit past de gewichten van de verborgen laag aan.
   - `self.b1 -= learning_rate * self.db1`. Dit past de biases van de verborgen laag aan.

Deze stappen volgen de principes van achterwaartse propagatie om de gewichten en biases van het neurale netwerk aan te passen op basis van de fout tussen de voorspelde waarden en de werkelijke waarden.