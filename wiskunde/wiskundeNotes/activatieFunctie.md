De sigmoid-activatiefunctie is een veelgebruikte wiskundige functie binnen AI, met name in neurale netwerken. Het wordt vaak gebruikt als een niet-lineaire activatiefunctie voor het introduceren van niet-lineariteit in het model. 

De sigmoid-functie heeft een S-vormige curve en wordt gekenmerkt door de volgende eigenschappen:

Begrenzing: De sigmoid-functie geeft altijd een waarde tussen 0 en 1. Naarmate z naar oneindig nadert, nadert σ(z) naar 1, en naarmate z naar min oneindig nadert, nadert σ(z) naar 0. Dit maakt het geschikt voor het modelleren van kansen of waarschijnlijkheden.

Niet-lineariteit: De sigmoid-functie introduceert niet-lineariteit in het model. Het kan helpen bij het modelleren van complexe relaties tussen invoer en uitvoer, waardoor het model beter in staat is om niet-lineaire patronen in de gegevens te leren.

Differentieerbaarheid: De sigmoid-functie is differentieerbaar overal in zijn domein. Dit is belangrijk voor het trainen van neurale netwerken met behulp van gradient-based optimalisatie-algoritmen, zoals backpropagation. De afgeleide van de sigmoid-functie kan eenvoudig worden berekend als σ'(z) = σ(z) * (1 - σ(z)).


![activatieFunctie](https://gitlab.fdmci.hva.nl/chintss/minor-logboek-aai-2/-/raw/main/wiskunde/Differentieren/IMG_8133.JPEG)
