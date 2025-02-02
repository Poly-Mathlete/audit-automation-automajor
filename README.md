# audit-automation-automajor
https://github.com/Poly-Mathlete/audit-automation-automajor

Structure de repo (code utile):

# pdf_extract_to_excel :
generate_excel.py

populate_excel_fast(excel_filename, out_path, pdfs_path, max_simult=10) # remplir un excel, il faut fournir le chemin de l'excel template, le chemin de sortie de l'excel généré, les chemins sous forme d'une listes des bails à analyser, max_simult représente le nombre de thread, s'il est trop haut le nombre max de requettes à bedrock et atteint.

populate_excel(excel_filename, out_path, pdfs_path, max_simult=10) # remplir un excel, il faut fournir le chemin de l'excel template, le chemin de sortie de l'excel généré, les chemins sous forme d'une listes des bails à analyser. Cette méthode est longue...
    
# pdf_extract_to_word :
extract_for_word.py

extract_from_pdf(f) # input is a file, output is a dictionnary that will be used to fillin the word document

extract_from_pdf_fast(f, max_worker=10) #faster version
    
# word_filler :
Word_filler.py

fill(data_path) #data_path is the path to a .json f ile containing the informations to fill

# ui

streamlit web ui in app.py file
```
streamlit run app.py
```

```
Commandes utiles :
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
