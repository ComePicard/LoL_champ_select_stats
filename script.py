def count_position(position: str, echantillon: str):
    i = 0
    result = 0
    pos_calcul = int(position)+5
    position_bis = str(pos_calcul)
    while i < len(echantillon) :
        if(position=="5"):
            if((i!=len(echantillon)-1 and echantillon[i]=="1" and echantillon[i+1]=="0") or echantillon[i]==position):
                result += 1
        elif(position==1):
            if((echantillon[i]=="1" and echantillon[i+1]!="0") or echantillon[i]==position_bis):
                result += 1
        elif(echantillon[i]==position or echantillon[i]==position_bis):
            result += 1
        i+=1
    return result

def moyenne_position(echantillon: str):
    un = count_position("1",echantillon)
    deux = count_position("2",echantillon)*2
    trois = count_position("3",echantillon)*3
    quatre = count_position("4",echantillon)*4
    cinq = count_position("5",echantillon)*5
    return (un + deux + trois + quatre + cinq) / len(echantillon)
    

with open('./data_lol.txt') as lol_data :
    echantillon = lol_data.read()
    print("Taille de l'échantillon:",len(echantillon),"games")
    print("Nombre de 1st pick:",count_position("1", echantillon), " → ",round(count_position("1", echantillon)/len(echantillon)*100, 2),"%")
    print("Nombre de 2nd pick:",count_position("2", echantillon), " → ",round(count_position("2", echantillon)/len(echantillon)*100, 2),"%")
    print("Nombre de 3rd pick:",count_position("3", echantillon), " → ",round(count_position("3", echantillon)/len(echantillon)*100, 2),"%")
    print("Nombre de 4th pick:",count_position("4", echantillon), " → ",round(count_position("4", echantillon)/len(echantillon)*100, 2),"%")
    print("Nombre de 5th pick:",count_position("5", echantillon), " → ",round(count_position("5", echantillon)/len(echantillon)*100, 2),"%")
    print("Position moyenne dans le lobby:",round(moyenne_position(echantillon), 2))
