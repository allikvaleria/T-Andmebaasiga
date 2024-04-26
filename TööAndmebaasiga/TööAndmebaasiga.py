#import json
#from tkinter.ttk import Separator

#json_data='{"nimi":"Valeria Allik","vanus": 17, "prillid" :true}'
#data=json.loads(json_data)

#print(data)
#print(data["nimi"])
#for id_,dat in enumerate(data):
#    print(id_,"-",dat)

#for key, value in data.items():
#    print(key,":",value)


#data2={
#    "nimi":"Daria",
#    "vamus":17,
#    "abielus":True,
#    "lapsed":("Inna","Mati"),
#    "koduloomad":None,
#    "autod":
#    [
#        {"muudel":"BMW","varv":"punane","joud":500,"number":"123ABC"},
#        {"muudel":"Ford","varv":"must","joud":300,"number":"321CBA"}
#        ]
#    }
#print(json.dumps(data2))
#print(json.dumps(data2,indent=2,separators=(".","="),sort_keys=True))
#with open("data_file.json","w") as write_file:
#    json.dump(data2,write_file)

#print("Andmed failist:")
#with open("data_file.json","r") as w_file:
#    data2=json.load(w_file)

#print(data2)