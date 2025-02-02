# audit-automation-automajor
https://github.com/Poly-Mathlete/audit-automation-automajor

Structure de repo (code utile):

pdf_extract_to_excel : \
    generate_excel : \
        populate_excel_fast(excel_filename, out_path, pdfs_path, max_simult=10) # remplir un excel, il faut fournir le chemin de l'excel template, le chemin de sortie de l'excel généré, les chemins sous forme d'une listes des bails à analyser, max_simult représente le nombre de thread, s'il est trop haut le nombre max de requettes à bedrock et atteint.

        populate_excel(excel_filename, out_path, pdfs_path, max_simult=10) # remplir un excel, il faut fournir le chemin de l'excel template, le chemin de sortie de l'excel généré, les chemins sous forme d'une listes des bails à analyser. Cette méthode est longue...


```
Commandes utiles :
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
