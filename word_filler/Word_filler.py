import json
from docx import Document


def replace_placeholders_in_paragraph(paragraph, data):
    if not paragraph.runs:
        return
    else:
        for dicoo in data.values():#dico correspodant à "parties"
            for key, value in dicoo.items():#"bailleur" et dictionnaire corrspondzant
                if key in paragraph.text:
                    if bool not in value.keys():
                        paragraph.text = paragraph.text.replace(key, " ".join(str(v) for v in value.values()))
                        
                  #  elif value[bool] ==True:
                   #     dicoo[key+"oui"]=dicoo[key]
                        
                        
                        
                    #elif paragraph.text == "{{oui}}" or paragraph.text == "{{non}}":
                     #   if True in value.values():
                      #      paragraph.text = paragraph.text.replace(key, "oui")
                       # else:
                        #    paragraph.text = paragraph.text.replace(key, "non")
                    
                    
def process_document(doc, data):
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    replace_placeholders_in_paragraph(paragraph, data)

def main():
    with open("data.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    doc = Document("Fiche_audit_modele.docx")
    
    # Ajout des placeholders avec accolades
    for dictionnaire in data.values():
        for key in list(dictionnaire.keys()):  # Utilisation de list() pour éviter des problèmes lors de la modification
            dictionnaire[f"{{{{{key}}}}}"] = dictionnaire.pop(key)
    
    process_document(doc, data)
    doc.save("fiche_audit_remplie.docx")

if __name__ == "__main__":
    main()
