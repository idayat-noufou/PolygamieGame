define O = Character ("Ovo", color ="#5d3a1a" )
define K = Character ("Kassim")
define Z = Character ("Zahra")
define A = Character ("Amina")
define B = Character ("Balkis")
label start:
    
    O "Salut, je suis Ovo, je suis ton narrateur, celui qui va t’accompagner tout au long de cette belle aventure familiale. 

Içi, tu découvriras le quotidien de 4 personnes qui formeront éventuellement une famille."
    show kassim at truecenter 
    O "Kassim Kouyaté, un jeune homme de 25 salarié dans la finance."
    show za v maison with dissolve
    O "Zahra Affi, une jeune mère au foyer de 28 ans."
    hide kassim
    show za v maison at Position(xalign=0.25, yalign=1.0) with dissolve
    show am v maison at Position(xalign=0.75, yalign=1.0) with dissolve
    O "Amina Soro sa petite fille de 3 ans."
    hide za v maison
    hide am v maison 
    show ba v maison
    O "Et Balkis Bah, une jeune pédiatre de 25 ans débutant son internat."
    hide ba v maison 
    O "Tu seras l’ange ou le démon de l’un de nos personnages Kassim, Zahra, ou Balkis et les choix que tu feras impacterons directement l’harmonie de la famille et les liens entre les personnages.
D’abord, découvre leurs liens :"

    O "Zahra et Kassim sont marié depuis un peu moins d’un an déjà. Même si ils vivent dans l’entente et la bonne humeur, ce couple manquent un peu d’amour romantique.

Balkis et Kassim sont camarades de lycée. Ils ont toujours eu un faible l’un pour l’autre mais ils se sont perdu de vue après le bac."

    
