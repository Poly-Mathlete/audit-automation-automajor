
template = f"""
Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
Extraire les informations suivantes du contenu fourni :

Retourne ta réponse dans entre les balises XML <output> sous la forme:
<output>
CONTENT
</output>

Réfléchis à chaque étape de ton processus de réflexion et note tes pensées dans des balises XML <scratchpad>

"""

extract_bailleur_p_1 = f"""
Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
Extrait de ce texte l'information suivante : le nom, l'adresse, le numéro RCS du bailleur.

Retourne ta réponse dans entre les balises XML <output> sous la forme:
<output>
NOM BAILLEUR, ADRESSE BAILLEUR, numéro rcs de l'entreprise.
</output>

Réfléchis à chaque étape de ton processus de réflexion et note tes pensées dans des balises XML <scratchpad>

"""

extract_preneur_p_1 = f"""
Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
Extrait de ce texte l'information suivante : le nom, l'adresse, le numéro RCS du preneur.

Retourne ta réponse dans entre les balises XML <output> sous la forme:
<output>
NOM preneur, ADRESSE preneur, numéro rcs de l'entreprise.
</output>

Réfléchis à chaque étape de ton processus de réflexion et note tes pensées dans des balises XML <scratchpad>

"""

extract_bailleur = [{
    "description" : "récupérer nom et adresse du bailleur",
    "tag": "BAILLEUR",
    "sys_prompt": extract_bailleur_p_1,
    },]

extract_preneur = [{
    "description" : "récupérer nom et adresse du preneur",
    "tag": "PRENEUR",
    "sys_prompt": extract_preneur_p_1,
    },]

extract_bail_type_p_1 = f"""
Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
Extraire les informations suivantes du contenu fourni : type de bail (commercial, professionnel, habitation, autre...) et rien d'autre

Retourne ta réponse dans entre les balises XML <output> sous la forme:
<output>
type_de_bail
</output>

Réfléchis à chaque étape de ton processus de réflexion et note tes pensées dans des balises XML <scratchpad>

"""

extract_bail_type = [{
    "description" : "récupérer type de bail",
    "tag": "BAIL_TYPE",
    "sys_prompt": extract_bail_type_p_1,
    },]

excel_extraction = [extract_bail_type, ]