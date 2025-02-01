prompt_start = f"""

Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
Extraire les informations suivantes du contenu fourni et retourner une  et une seule liste correspondant aux champs demandés avec une explication associée :
"""

prompt_end = f"""
Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
Ecrit ta réponse en JSON valide.
Renvoie ta réponse entre les balises <output> et </output> et assure toi que cela forme un JSON valide.
"""
# Lors de la création de la réponse, assure-toi d'échapper les guillemets dans les valeurs de chaîne pour que la sortie soit un JSON valide
#Réfléchis à chaque étape de ton processus de réflexion et note tes pensées dans des balises XML <scratchpad>

# retourne le tableau JSON valide avec les détails extraits dans des balises XML <output>, en incluant uniquement le JSON valide
# Retourne ta réponse dans un tableau JSON valide, en utilisant le format de sortie fourni, sans citer json
# <example_format>
# {{"Bailleur": "(nom du bailleur)", "Preneur": "(nom du preneur)", "Cession": "(cession)"}}
# </example_format>

# Le nom du bailleur (en lettre capitale, de manière succincte, avec les numéros de la société)
# Le nom du preneur dans le bail (en lettre capitale, de manière succincte, avec les numéro de la société)
# S'il y a cession du droit au bail par le preneur d'origine (oui ou non)
# S'il y a exclusivité (oui ou non)
# S'il y a une clause de non concurrence (oui ou non, et si oui laquelle, être succinct)


system_prompt = {
    "PARTIES" : [
        """
        Tu est un processeur d'analyse de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extraire les informations suivantes du contenu fourni, de manière à extraire les parties pernantes:
            -le nom du bailleur (avec nom, Ville, numéro RCS)
            -le nom du  figurant dans le bail (avec nom, Ville, numéro RCS)
            -s'il y a cession des droit au bail par le preneur d'origine (oui ou non)
            
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        """,
        
        """
        Tu est un processeur d'analyse de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations nécessaire du document fourni pour pouvoir compléter le JSON suivant :
        
        {
            "Bailleur": {
                "nom": (le nom du bailleur),
                "lieu de l'imatriculation RCS" : (lieu),
                "numéro SIREN": (numéro),
                "explication": (explication de/des réponse(s))
                },
            "Preneur": {
                "nom": (le nom du preneur),
                "lieu de l'imatriculation RCS" : (lieu),
                "numéro SIREN": (numéro),
                "explication": (explication de/des réponse(s))
                }
            "Cession": {
                "bool": (true ou false),
                "explication": (explication de/des réponse(s))
                }
        }
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        Ta réponse doit uniquement être un JSON valide. Attribue la valeur null aux champs qui ne sont pas renseignés dans le texte.
        """,
    ],
    "DUREE": [
        """
        Tu est un processeur d'analyse de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations suivantes du contenu fourni, répond en expliquant pourquoi ta réponse correspond aux données fournies:
        
        - Date de signature du contrat fournit présente en fin de document sous la forme mm/dd/yyyy
        - La loi pinel (loi n°2014-626 du 18 juin 2014) est-elle applicable (oui ou non) (elle s'applique si la signature du contrat a lieu après la date de la loi)
        - Date de prise d'effet du bail
        - Durée du bail
        - La date du terme contractuel du bail
        - Si la période est ferme (oui ou non)
        - Date de la prochaine faculté de sortie
        - Préavis minimum à respecter
        - Si il y a une clause spécifique relative à la durée du Bail renouvelé (oui ou non)
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        """,
        """
        Tu est un processeur d'analyse de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations nécessaire du document fourni pour pouvoir compléter le JSON suivant :
        
        {
            "Date_signature_contrat": {
                "date": (date),
                "explication": (explication de/des réponse(s))
                },
            "Application_loi_pinel": {
                "value": (true ou false),
                "explication": (explication de/des réponse(s))
                }
            "Date_effet_bail": {
                "date": (date),
                "explication": (explication de/des réponse(s))
                }
            "Duree_bail": {
                "duree": (duree),
                "explication": (explication de/des réponse(s))
                }
            "Date_terme_contractuel": {
                "date": (date),
                "explication": (explication de/des réponse(s))
                }
            "Periode_ferme": {
                "bool": (true ou false),
                "explication": (explication de/des réponse(s))
                }
            "Date_faculte_sortie": {
                "date": (date),
                "explication": (explication de/des réponse(s))
                }
            "Preavis_minimum": {
                "duree": (duree),
                "explication": (explication de/des réponse(s))
                }
            "Clause_duree_bail_renouvele": {
                "bool": (true ou false),
                "explication": (explication de/des réponse(s))
                }
        }
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        Ta réponse doit uniquement être un JSON valide. Attribue la valeur null aux champs qui ne sont pas renseignés dans le texte.
        """
    
    ],

    "MESURES D'ACCOMPAGNEMENT":[
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations suivantes du contenu fourni, répond en expliquant pourquoi ta réponse correspond aux données fournies:
        
        - Franchise et/ou réduction de loyer en cours (oui ou non), si oui donner l'ensemble des conditions sous la forme d'une sous liste 
        - Participation financière du Bailleur aux travaux d'aménagement du Preneur (oui ou non), si oui donner le montant et les conditions
        - Y a-t-il d'autres mesures d'accompagement dans le contrat (oui ou non)
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        """,
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations nécessaire du document fourni pour pouvoir compléter le JSON suivant :
        
        {
            "Franchise_Reduction": {
                "bool": (true ou false),
                "conditions": (conditions, fait une liste textuelle),
                "explication": (explication de/des réponse(s))
                },
            "Participation_financiere": {
                "bool": (true ou false),
                "montant": (montant),
                "conditions": (conditions),
                "explication": (explication de/des réponse(s))
                }
            "Mesure_accompagnement": {
                "bool": (true ou false),
                "explication": (explication de/des réponse(s))
                }
        }
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        Ta réponse doit uniquement être un JSON valide. Attribue la valeur null aux champs qui ne sont pas renseignés dans le texte.
        """
    ],
    "GARANTIES":[
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations suivantes du contenu fourni, répond en expliquant pourquoi ta réponse correspond aux données fournies:
        
        - Dépôt de garantie (oui ou non), si oui donner le montant de la garantie
        - Y a-t-il d'autre garanties que le dépôt de garantie (oui ou non), si oui donner les détails
        - Original de la garantie en possession du Bailleur (oui ou non), si oui donner la nature de la garantie, le garant, le montant, la date d'expiration
        - La garantie est-elle transférable au nouveau bailleur (oui ou non)
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        """,
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations nécessaire du document fourni pour pouvoir compléter le JSON suivant :
        
        {
            Depot_garantie: {
                bool: (true ou false),
                montant: (montant),
                explication: (explication de/des réponse(s))
                },
            Autres_garanties: {
                bool: (true ou false),
                explication: (explication de/des réponse(s))
                }
            Original_garantie: {
                bool: (true ou false),
                nature: (nature),
                garant: (garant),
                montant: (montant),
                expiration: (date),
                transferabilite: (transfert),
                explication: (explication de/des réponse(s))
                }            
        }
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        Ta réponse doit uniquement être un JSON valide. Attribue la valeur null aux champs qui ne sont pas renseignés dans le texte.
        """
    ],
    
    
    "HONORAIRES, IMPOTS, TAXES ET ASSURANCE DU BAILLEUR": [ 
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations suivantes du contenu fourni, répond en expliquant pourquoi ta réponse correspond aux données fournies:
            
        
        - Dans le cadre des parties privatives, le bailleur aura-t-il des impôts futurs ? (oui ou non)
        - Dans le cadre des parties privatives, le bailleur aura-t-il une taxe foncière ? (oui ou non)
        - Dans le cadre des parties privatives, le bailleur aura-t-il une Taxe d'enlèvement des ordures ménagères (TEOM) ? (oui ou non)
        - Dans le cadre des parties privatives, le bailleur aura-t-il une taxe sur les locaux à usage de commerce ? (oui ou non) 
        
        - Dans le cadre des parties privatives, le preneur aura-t-il des impôts futurs ? (oui ou non)
        - Dans le cadre des parties privatives, le preneur aura-t-il une taxe foncière ? (oui ou non)
        - Dans le cadre des parties privatives, le preneur aura-t-il une Taxe d'enlèvement des ordures ménagères (TEOM) ? (oui ou non)
        - Dans le cadre des parties privatives, le preneur aura-t-il une taxe sur les locaux à usage de commerce ? (oui ou non)
        
        - Dans le cadre des parties communes, le bailleur aura t-il des impôts futurs ? (oui ou non)
        - Dans le cadre des parties communes, le bailleur aura t-il une taxe foncière ? (oui ou non)
        - Dans le cadre des parties communes, le bailleur aura t-il une Taxe d'enlèvement des ordures ménagères (TEOM) ? (oui ou non)
        - Dans le cadre des parties communes, le bailleur aura t-il une taxe sur les locaux à usage de commerce ? (oui ou non)
        
        - Dans le cadre des parties communes, le preneur aura t-il des impôts futurs ? (oui ou non)
        - Dans le cadre des parties communes, le preneur aura t-il une taxe foncière ? (oui ou non)
        - Dans le cadre des parties communes, le preneur aura t-il une Taxe d'enlèvement des ordures ménagères (TEOM) ? (oui ou non)
        - Dans le cadre des parties communes, le preneur aura t-il une taxe sur les locaux à usage de commerce ? (oui ou non)
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.        
        """,
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations nécessaire du document fourni pour pouvoir compléter le JSON suivant :
        
        {
            "Parties_privees": {
                "Bailleur": {
                    "Impots_futurs": (true ou false),
                    "Taxe_fonciere": (true ou false),
                    "TEOM": (true ou false),
                    "Taxe_commerce": (true ou false),
                    "explication" : (explication de/des réponse(s))
                },
                "Preneur": {
                    "Impots_futurs": (true ou false),
                    "Taxe_fonciere": (true ou false),
                    "TEOM": (true ou false),
                    "Taxe_commerce": (true ou false),
                    "explication" : (explication de/des réponse(s))
                }
            },
            "Parties_communes": {
                "Bailleur": {
                    "Impots_futurs": (true ou false),
                    "Taxe_fonciere": (true ou false),
                    "TEOM": (true ou false),
                    "Taxe_commerce": (true ou false),
                    "explication" : (explication de/des réponse(s))
                },
                "Preneur": {
                    "Impots_futurs": (true ou false),
                    "Taxe_fonciere": (true ou false),
                    "TEOM": (true ou false),
                    "Taxe_commerce": (true ou false),
                    "explication" : (explication de/des réponse(s))
                }
            }
        }
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        Ta réponse doit uniquement être un JSON valide. Attribue la valeur null aux champs qui ne sont pas renseignés dans le texte.
        """
    ],
    "HONORAIRES, IMPOTS, TAXES ET ASSURANCE DU BAILLEUR (2)": [
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations suivantes du contenu fourni, répond en expliquant pourquoi ta réponse correspond aux données fournies:
        
        - Le bailleur est-il facturé des frais de gestion technique des travaux (oui ou non), si oui décris les conditions
        - Le baillleur est-il facturé des frais de gestion locative (hors de la gestion des loyers) (oui ou non), si oui décris les conditions,
        - Le bailleur est-il facturé des frais de gestion des loyers (oui ou non), si oui décris les conditions
        - Le bailleur est-il facturé des frais de gestion du syndic de copropriété/ASL/AFUL/autre (oui ou non), si oui décris les conditions
        
        - Le preneur est-il facturé des frais de gestion technique des travaux (oui ou non), si oui décris les conditions
        - Le preneur est-il facturé des frais de gestion locative (hors de la gestion des loyers) (oui ou non), si oui décris les conditions,
        - Le preneur est-il facturé des frais de gestion des loyers (oui ou non), si oui décris les conditions
        - Le preneur est-il facturé des frais de gestion du syndic de copropriété/ASL/AFUL/autre (oui ou non), si oui décris les conditions
        
        - Qui paie les primes d’assurance du BAILLEUR (le bailleur ou le preneur)
        
        - Est-ce qu'il y a des frais de marketing (oui ou non), si oui décris les conditions
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        """,
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations nécessaire du document fourni pour pouvoir compléter le JSON suivant :
        
        {
            "Honoraires": {
                "Bailleur": {
                    "Gestion_technique": {
                        "bool": (true ou false),
                        "conditions": (conditions),
                        "explication": (explication de/des réponse(s))
                    },
                    "Gestion_locative": {
                        "bool": (true ou false),
                        "conditions": (conditions),
                        "explication": (explication de/des réponse(s))
                    },
                    "Gestion_loyers": {
                        "bool": (true ou false),
                        "conditions": (conditions),
                        "explication": (explication de/des réponse(s))
                    },
                    "Gestion_syndic": {
                        "bool": (true ou false),
                        "conditions": (conditions),
                        "explication": (explication de/des réponse(s))
                    }
                },
                "Preneur": {
                    "Gestion_technique": {
                        "bool": (true ou false),
                        "conditions": (conditions),
                        "explication": (explication de/des réponse(s))
                    },
                    "Gestion_locative": {
                        "bool": (true ou false),
                        "conditions": (conditions),
                        "explication": (explication de/des réponse(s))
                    },
                    "Gestion_loyers": {
                        "bool": (true ou false),
                        "conditions": (conditions),
                        "explication": (explication de/des réponse(s))
                    },
                    "Gestion_syndic": {
                        "bool": (true ou false),
                        "conditions": (conditions),
                        "explication": (explication de/des réponse(s))
                    }
                }
            Paiement_assurance: {
                "payeur": (bailleur ou preneur),
                "explication": (explication de/des réponse(s))
                }
            }
            Fonds_marketing: {
                "bool": (true ou false),
                "conditions": (conditions),
                "explication": (explication de/des réponse(s))
            }
        }

        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        Ta réponse doit uniquement être un JSON valide. Attribue la valeur null aux champs qui ne sont pas renseignés dans le texte.
        """
    ],
    "TRAVAUX - REPARATIONS - REMPLACEMENTS": [
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations suivantes du contenu fourni, répond en expliquant pourquoi ta réponse correspond aux données fournies:
        
        - Pour les parties privatives, les frais des grosses réparations sont à la charge (du bailleur ou du preneur)
        - Pour les parties privatives, les frais de mise en conformité et des injonctions administratives sont à la charge (du bailleur ou du preneur)
        - Pour les parties privatives, les frais des problèmes de vétusté et de force majeure sont à la charge (du bailleur ou du preneur)
        - Pour les parties privatives, les frais de remplacement des éléments d'équipement sont à la charge (du bailleur ou du preneur)
        
        - Pour les parties communes, les frais des grosses réparations sont à la charge (du bailleur ou du preneur)
        - Pour les parties communes, les frais de mise en conformité et des injonctions administratives sont à la charge (du bailleur ou du preneur)
        - Pour les parties communes, les frais des problèmes de vétusté et de force majeure sont à la charge (du bailleur ou du preneur)
        - Pour les parties communes, les frais de remplacement des éléments d'équipement sont à la charge (du bailleur ou du preneur)
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        """,
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations nécessaire du document fourni pour pouvoir compléter le JSON suivant :
        
        {
            "Parties_privees": {
                "Bailleur": {
                    "Grosses_reparations": (true ou false),
                    "Mise_conformite": (true ou false),
                    "Vetuste": (true ou false),
                    "Remplacement": (true ou false),
                    "explication" : (explication de/des réponse(s))
                },
                "Preneur": {
                    "Grosses_reparations": (true ou false),
                    "Mise_conformite": (true ou false),
                    "Vetuste": (true ou false),
                    "Remplacement": (true ou false),
                    "explication" : (explication de/des réponse(s))
                }
            },
            "Parties_communes": {
                "Bailleur": {
                    "Grosses_reparations": (true ou false),
                    "Mise_conformite": (true ou false),
                    "Vetuste": (true ou false),
                    "Remplacement": (true ou false),
                    "explication" : (explication de/des réponse(s))
                },
                "Preneur": {
                    "Grosses_reparations": (true ou false),
                    "Mise_conformite": (true ou false),
                    "Vetuste": (true ou false),
                    "Remplacement": (true ou false),
                    "explication" : (explication de/des réponse(s))
                }
            }
        }
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        Ta réponse doit uniquement être un JSON valide. Attribue la valeur null aux champs qui ne sont pas renseignés dans le texte.        
        """
    ],
    "DESTRUCTION": [
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations suivantes du contenu fourni, répond en expliquant pourquoi ta réponse correspond aux données fournies:
        
        - Est-ce qu'il y a une précision spécifique en cas de destruction des locaux loués (oui ou non), si oui décris les conditions
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        """,
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations nécessaire du document fourni pour pouvoir compléter le JSON suivant :
        
        {
            "Derogation_article_1722": {
                "bool": (true ou false),
                "conditions": (conditions),
                "explication": (explication de/des réponse(s))
            }
        }
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        Ta réponse doit uniquement être un JSON valide. Attribue la valeur null aux champs qui ne sont pas renseignés dans le texte.
        """
    ],
    "AUTORISATIONS DE TRAVAUX": [
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations suivantes du contenu fourni, répond en expliquant pourquoi ta réponse correspond aux données fournies:
        
        - Le bailleur a-t-il la possibilité de réaliser des travaux dans les locaux loués (oui ou non), si oui décris les conditions
        - Le bailleur a-t-il la possibilité de réaliser des travaux dans les locaux loués pendant une longue période sans indémnisation (oui ou non), si oui décris les conditions
        
        - Le preneur a-t-il la permission de réaliser des travaux sans l'accord préalable du bailleur (oui ou non), si oui décris les conditions
        - Le preneur a-t-il la permission de poser des plaques ou des enseignes sans l'accord préalable du bailleur (oui ou non), si oui décris les conditions
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        """,
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations nécessaire du document fourni pour pouvoir compléter le JSON suivant :
        
        {
            "Bailleur": {
                "Travaux": {
                    "bool": (true ou false),
                    "conditions": (conditions),
                    "explication": (explication de/des réponse(s))
                },
                "Travaux_longue_duree": {
                    "bool": (true ou false),
                    "conditions": (conditions),
                    "explication": (explication de/des réponse(s))
                }
            },
            "Preneur": {
                "Travaux": {
                    "bool": (true ou false),
                    "conditions": (conditions),
                    "explication": (explication de/des réponse(s))
                },
                "Plaques_enseignes": {
                    "bool": (true ou false),
                    "conditions": (conditions),
                    "explication": (explication de/des réponse(s))
                }
            }
        }
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        Ta réponse doit uniquement être un JSON valide. Attribue la valeur null aux champs qui ne sont pas renseignés dans le texte.
        """
    ],
    "RESTITUTION DES LOCAUX LOUES": [
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations suivantes du contenu fourni, répond en expliquant pourquoi ta réponse correspond aux données fournies:
        
        - Quel est l'état de restitustion des locaux loués (neuf, parfais, bon, état d'usage)
        - Est-ce qu'il y a une clause d'accession (oui ou non), si oui est-elle (en fin de bail, en fin de jouissance ou autre)
        - Est-ce que le bailleur a la possibilité a la possibilité de demander la remise en état des locaux loués (oui ou non)
        - Est-ce qu'il y a un indémnité d'immobilisation (oui ou non), si oui décris les conditions
        - Est-ce qu'il y a un état des lieux d'entrée fourni en Data Room (oui ou non)
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        """,        
        """
        Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
        Extrait les informations nécessaire du document fourni pour pouvoir compléter le JSON suivant :
        
        {
            "Restituton": {
                "etat": (etat),
                "explication": (explication de/des réponse(s))
                },
            "Clause_accession": {
                "bool": (true ou false),
                "moment": (moment du bénéfice),
                "explication": (explication de/des réponse(s))
                },
            "Remise_etat": {
                "bool": (true ou false),
                "explication": (explication de/des réponse(s))
                },
            "Indemnite_immobilisation": {
                "bool": (true ou false),
                "conditions": (conditions),
                "explication": (explication de/des réponse(s))
                },
            "Etat_lieux_entree": {
                "bool": (true ou false),
                "explication": (explication de/des réponse(s))
                }
        }
        
        Lors de ton processus de réflexion, assure toi de ne pas imaginer de données et ne te base que sur les informations fournies dans le texte pour remplir les champs demandés.
        Ta réponse doit uniquement être un JSON valide. Attribue la valeur null aux champs qui ne sont pas renseignés dans le texte.
        """
    ]
    # "SOUS-LOCATION / LOCATION-GERANCE / DOMICILIATION / CESSION": [
    #     """
    #     Tu est un processeur de données et un avocat. Tu recevras le texte d'un bail commercial en rapport avec l'imobilier.
    #     Extrait les informations suivantes du contenu fourni, répond en expliquant pourquoi ta réponse correspond aux données fournies:
        
        
    #     """,
    #     """
    #     """
    # ]
}

# def complete_system_prompt():
#     for key in system_prompt.keys():
#         system_prompt[key] = prompt_start + system_prompt[key]+ prompt_end
        
# complete_system_prompt()
