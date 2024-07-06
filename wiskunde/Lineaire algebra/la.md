
**Lineaire algebra** 

Inverse 𝑨^−𝟏 matrix berekenen van matrix A:

Stap 1) Bepaal de determinant (D)

Stap 2) Bepaal AT

Stap 3) Bepaal de determinant van alle 2x2 matrices

Stap 4) Bepaal de adjunct matrix

Stap 5) Deel het resultaat van stap 4 door de determinant (stap 1)

Stap 6) Controleer of geldt dat A · A−1 = I



1. Getransponeerde matrix:
De getransponeerde matrix van een matrix is de matrix waarbij de rijen van de oorspronkelijke matrix worden omgezet in kolommen en vice versa. Met andere woorden, de getransponeerde matrix draait de oorspronkelijke matrix om over zijn hoofddiagonaal. Het symbool voor de getransponeerde matrix is een T bovenaan de matrix. Bijvoorbeeld, als we een matrix A hebben met elementen a[i][j], dan wordt de getransponeerde matrix aangeduid als A^T, waarbij a[j][i] gelijk is aan a[i][j] in de oorspronkelijke matrix.

2. Inverse matrix:
De inverse matrix van een vierkante matrix A wordt aangeduid als A^(-1) en heeft de eigenschap dat het vermenigvuldigen van A met zijn inverse de identiteitsmatrix oplevert. De identiteitsmatrix is een speciale matrix waarbij de diagonale elementen 1 zijn en alle andere elementen 0. Voor een matrix A om een inverse te hebben, moet het determinant van A verschillend zijn van nul. De inverse matrix stelt ons in staat om de oorspronkelijke matrix "ongedaan te maken" wanneer deze wordt vermenigvuldigd met de inverse.

3. Determinant van een matrix:
De determinant van een vierkante matrix is een scalaire waarde die uniek is voor die matrix. Het wordt meestal aangeduid als det(A) of |A|. De determinant heeft verschillende toepassingen en eigenschappen, zoals het bepalen van de oplosbaarheid van lineaire vergelijkingen, het berekenen van de oppervlakte van een parallellogram in 2D of het volume van een parallellepipedum in 3D. De determinant kan ook worden gebruikt om te bepalen of een matrix een inverse heeft (als de determinant ongelijk is aan nul) en om lineaire afhankelijkheid van vectoren te analyseren.

4. Identiteitsmatrix:
Een identiteitsmatrix, meestal aangeduid als I, is een vierkante matrix waarbij alle diagonale elementen gelijk zijn aan 1 en alle andere elementen gelijk zijn aan 0. Het heeft de eigenschap dat de vermenigvuldiging van een matrix A met de identiteitsmatrix I resulteert in de matrix A zelf. Met andere woorden, AI = IA = A voor een geschikte matrix A. De identiteitsmatrix fungeert als het neutrale element voor matrixvermenigvuldiging, vergelijkbaar met het getal 1 in de gewone vermenigvuldiging van getallen.

De waarde van de determinant van een matrix kan belangrijke informatie verschaffen over de eigenschappen van de matrix. Hier zijn enkele scenario's:

1. Determinant kleiner dan 0:
Als de determinant van een matrix kleiner is dan 0, betekent dit dat de matrix een negatieve determinant heeft. Dit kan aangeven dat de matrix een spiegeling of inversie veroorzaakt in de ruimte waarin de vectoren worden afgebeeld. Het geeft aan dat de oriëntatie van de vectoren in de matrix wordt omgekeerd.

2. Determinant gelijk aan 0:
Wanneer de determinant van een matrix gelijk is aan 0, wordt dit aangeduid als een singuliere matrix of een matrix met lineaire afhankelijkheid tussen de rijen of kolommen. Dit betekent dat de rijen of kolommen van de matrix lineair afhankelijk zijn van elkaar, waardoor de matrix niet-inverteerbaar is. Een determinant van 0 kan ook aangeven dat de matrix geen volledige rang heeft.

3. Determinant gelijk aan of > 1:
Als de determinant van een matrix gelijk is aan 1, betekent dit dat de matrix een speciale eigenschap heeft. Bijvoorbeeld, in lineaire transformaties kan een matrix met determinant 1 een zogenaamde eenheidsdeterminant hebben, wat betekent dat het de grootte van de vectoren behoudt en geen schaling of draaiing introduceert.
