def csMakeItJazzy(chords):
    output_list = [] 
    for chord in chords:
        if "7" in chord:
            output_list.append(chord)
            continue
        else:
            output_list.append(chord + str(7))
    return output_list






print(csMakeItJazzy(["G", "F", "C"])) # ["G7", "F7", "C7"]
print(csMakeItJazzy(["Dm", "G", "E", "A"])) #  ["Dm7", "G7", "E7", "A7"]
print(csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"])) # ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
print(csMakeItJazzy([])) # []



