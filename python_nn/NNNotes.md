
# BackPropagatie
Hier zijn enkele redenen waarom sigmoid benadering van backpropagatie effectief is:

1. Gradiëntinformatie: Door de fouten in de uitvoerlaag terug te propageren naar de verborgen lagen, kunnen de gewichten van de verborgen lagen worden aangepast op basis van de gradiëntinformatie van de kostenfunctie. Dit stelt het neurale netwerk in staat om de gewichten te optimaliseren en de fouten te verminderen.

2. Gebruik van afgeleiden: De term `(output_errors * final_outputs * (1.0 - final_outputs))` maakt gebruik van de afgeleide van de sigmoid-activatiefunctie. De afgeleide van de sigmoid-functie is eenvoudig uit te drukken in termen van de sigmoid-functie zelf, waardoor de berekening efficiënt is. Het gebruik van de afgeleiden maakt het mogelijk om de impact van elke gewichtsverbinding op de fouten in de netwerkuitvoer te bepalen.

3. Gewichtsupdates: De gewichtsupdates worden bepaald door het vermenigvuldigen van de delta's met de leersnelheid `self.lr`. De leersnelheid regelt de snelheid van het leren en stelt de mogelijkheid in om grote of kleine stappen te zetten in de gewichtsruimte. Door het gebruik van de leersnelheid kan het netwerk geleidelijk convergeren naar een optimaal gewichtsconfiguratie.

Samengevat is deze benadering van backpropagatie effectief omdat het gebruikmaakt van de gradiëntinformatie, afgeleiden en leersnelheid om de gewichten aan te passen en het netwerk te laten leren van de fouten in de uitvoerlaag. Hierdoor kan het neurale netwerk convergeren naar een betere voorspellende prestatie.

# Feedforward

De feedforward-methode is effectief vanwege de volgende redenen:

1. Efficiënte berekeningen: De feedforward-methode maakt gebruik van matrixvermenigvuldigingen om signalen van de ene laag naar de andere te berekenen. Dit maakt de berekeningen efficiënter in vergelijking met het individueel doorlopen van elk knooppunt. Door gebruik te maken van matrixvermenigvuldigingen kunnen meerdere signalen tegelijkertijd worden verwerkt, waardoor de berekeningen sneller verlopen.

2. Parallelle verwerking: Aangezien de berekeningen van de signalen naar de verborgen laag en van de verborgen laag naar de uitvoerlaag onafhankelijk zijn, kunnen ze parallel worden uitgevoerd. Dit betekent dat moderne hardware, zoals grafische kaarten (GPU's), de berekeningen efficiënter kan verwerken en de prestaties kan verbeteren.

3. Non-lineariteit van activatiefuncties: De feedforward-methode maakt gebruik van een niet-lineaire activatiefunctie, zoals de sigmoid-functie, om de signalen te transformeren. Hierdoor kan het neurale netwerk complexe patronen en relaties in de gegevens leren en modelleren. De niet-lineariteit is essentieel om de representatiekracht van het netwerk te vergroten en het vermogen te bieden om niet-lineaire relaties in de gegevens te leren.

4. Flexibiliteit: De feedforward-methode kan worden toegepast op neurale netwerken met verschillende architecturen en lagen. Het kan worden uitgebreid naar diepere netwerken met meerdere verborgen lagen, waardoor het netwerk een hoger abstractieniveau kan leren en complexere functies kan modelleren. Hierdoor kan het neurale netwerk meer geavanceerde patronen en structuren in de gegevens leren.

Over het algemeen is de feedforward-methode een fundamenteel en essentieel onderdeel van het neurale netwerkproces. Het maakt het mogelijk om signalen door het netwerk te sturen, non-lineariteit toe te voegen en complexe relaties in de gegevens te leren. Dit draagt bij aan de kracht en effectiviteit van neurale netwerken bij taken zoals patroonherkenning, classificatie en voorspelling.


Vergelijking met linear:

Over het algemeen worden lineaire feedforward-methoden minder vaak gebruikt dan feedforward-methoden met niet-lineaire activatiefuncties vanwege hun beperkte capaciteit om complexe patronen te leren.