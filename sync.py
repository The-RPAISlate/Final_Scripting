from Main import Main
import json

if __name__ == "__main__" :  
    with open('dict.json') as json_file:
        data = json.load(json_file)
        obj = Main(data)
        obj.WriteNotes()
        obj.WriteLecture()
        obj.WriteTextBook()