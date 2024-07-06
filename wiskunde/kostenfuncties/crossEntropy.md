waarschijnlijkheden P = [[0, 2], [0, 5], [0, 3]] en de werkelijke 

waarschijnlijkheden Q = [[1, 2], [2, 6], [2, 1]].

De cross-entropie tussen de voorspelde waarschijnlijkheden P en de werkelijke waarschijnlijkheden Q wordt gegeven door de formule:

Cross-entropy = -Σ(Q * log(P))

Laten we de berekening uitvoeren:

Bereken de logaritme van de voorspelde waarschijnlijkheden P:

Log(P) = [[log(0), log(2)], [log(0), log(5)], [log(0), log(3)]]

Let op dat log(0) niet gedefinieerd is. In dit geval kunnen we aannemen dat log(0) = -∞.

Vermenigvuldig de werkelijke waarschijnlijkheden Q met de logaritme van de voorspelde waarschijnlijkheden P:

Q * Log(P) = [[1 * log(0), 2 * log(2)], [2 * log(0), 6 * log(5)], [2 * log(0), 1 * log(3)]]

Aangezien log(0) = -∞, hebben alle termen waarin log(0) voorkomt de waarde -∞. We kunnen deze termen negeren bij de berekening van de som.

Bereken de som van de geldige termen:

Σ(Q * Log(P)) = 2 * log(2) + 6 * log(5) + 1 * log(3)

5.27300127206
Dit is correct er is een afwijking in de voorspelde en werkelijke waarde.

