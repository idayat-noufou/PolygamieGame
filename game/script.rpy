define O = Character ("Ovo", color ="#5d3a1a" )
define K = Character ("Kassim")
define Z = Character ("Zahra")
define A = Character ("Amina")
define B = Character ("Balkis")

label start:
    scene city with fade
    show ovo at truecenter
    O "Salut, je suis Ovo !"
    O "ton narrateur, celui qui va t’accompagner tout au long de cette belle aventure familiale." 
    O "Içi, tu découvriras le quotidien de 4 personnes qui formeront éventuellement une famille."
    show ovo at Position(xalign=1.0, yalign=0.5) with dissolve
    O "Mais avant de commencer, laisse moi te présenter les personnages principaux."
    show ka_v_maison at truecenter with dissolve
    O "Kassim Kouyaté, un jeune homme de 25 salarié dans la finance."
    hide ka_v_maison
    show za_v_maison at Position(xalign=0.5, yalign=0.5) with dissolve
    O "Zahra Affi, une jeune mère au foyer de 28 ans."
    show am_v_maison at Position(xalign=0.6, yalign=0.75) with dissolve
    O "Amina Soro sa petite fille de 3 ans."
    hide za_v_maison
    hide am_v_maison
    show ba_v_maison at truecenter with dissolve
    O "Et Balkis Bah, une jeune pédiatre de 25 ans débutant son internat."
    hide ba_v_maison
    O "Tu seras l’ange ou le démon de l’un de nos personnages Kassim, Zahra, ou Balkis "
    O "les choix que tu feras impacterons directement l’harmonie de la famille et les liens entre les personnages."
    O "D’abord, découvre leurs liens :"
    show ka_v_maison at Position(xalign=0.4, yalign=0.5) with dissolve
    show za_v_maison at Position(xalign=0.55, yalign=0.5) with dissolve
    O "Zahra et Kassim sont marié depuis un peu moins d’un an déjà."
    O "Même si ils vivent dans l’entente et la bonne humeur, ce couple manquent un peu d’amour romantique."

    hide za_v_maison
    show ba_v_maison at Position(xalign=0.55, yalign=0.5) with dissolve
    O "Balkis et Kassim sont camarades de lycée."
    O "Ils ont toujours eu un faible l’un pour l’autre mais ils se sont perdu de vue après le bac."
