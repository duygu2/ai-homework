from logic import *

friends = ["Beren","Cem","Defne","Emre"]
gifts= ["Anahtarlık","Gözlük", "Parfüm", "Saat"]
symbols=[]

knowledge = And()

#symbols added
for friend in friends:
    for gift in gifts:
        symbols.append(Symbol(f"{friend}{gift}"))
        
for friend in friends:
    knowledge.add(Or(
        Symbol(f"{friend}Anahtarlık"),
        Symbol(f"{friend}Gözlük"),
        Symbol(f"{friend}Parfüm"),
        Symbol(f"{friend}Saat")
        ))
#sadece beren'in 3 hediyesi var
knowledge.add(
    And(Symbol("BerenAnahtarlık"),
        Symbol("BerenParfüm"),
         Symbol("BerenSaat")
        )
    )

#Defne'nin sadece bir hediyesi var
knowledge.add(Or(
    Symbol("DefneParfüm"),
    Symbol("DefneSaat")
    ))

#Gözlüğü sadece Emre'ye hediye etmiştir.
knowledge.add(
    And(Symbol("EmreGözlük"),Symbol("EmreParfüm"))
    
    )

#bir arkadaşına sadece ahatarlık ve parfüm hediye etmiştir.
#Toplam 2 anahtarlık hediye etmiştir.-> beren ve Cem
knowledge.add(
    And(
        Symbol("CemAnahtarlık")
        ))

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)