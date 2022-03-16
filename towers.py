import re
import os

input_filter = re.compile(r'[aA][bB]|[aA][cC]|[bB][aA]|[bB][cC]|[cC][aA]|[cC][bB]')


ring = dict()
ring[0]="||"
ring[1]="0||0"
ring[2]="00||00"
ring[3]="000||000"
ring[4]="0000||0000"
ring[5]="00000||00000"

clear = lambda :os.system("cls")

tower_a = [5,4,3,2,1,0,0]
tower_b = [0,0,0,0,0,0,0]
tower_c = [0,0,0,0,0,0,0]
tower_win = [5,4,3,2,1,0,0]



def game():
    print()
    print("{:>25}".format("Hanoi-Towers"))
    print()
    for element in reversed(range(7)):
        print(f"{ring[tower_a[element]]:^15}{ring[tower_b[element]]:^15}{ring[tower_c[element]]:^15}")
    print()
    print("Bitte Eingabe von->nach z.B.: 'ac'; Ende mit 'q'")
    eingabe = input()

    while eingabe not in ["q","Q"] and (tower_b != tower_win or tower_c != tower_win):
        eingabe_result = input_filter.fullmatch(eingabe)
        if eingabe_result is None:
            print("Bitte gültige Eingabe")
            eingabe =input()
        else:
            (counter_a,counter_b,counter_c) = 0,0,0
            [source, destination] = list(iter(eingabe_result.string))

            bottom_stack_a = len([counter_a for element in tower_a if element != 0])
            bottom_stack_b = len([counter_b for element in tower_b if element != 0])
            bottom_stack_c = len([counter_c for element in tower_c if element != 0])

            tower_dict_pos = dict()
            tower_dict= dict()
            tower_dict["a"] = tower_a
            tower_dict["b"] = tower_b
            tower_dict["c"] = tower_c
            tower_dict_pos["a"] =  bottom_stack_a
            tower_dict_pos["b"] =  bottom_stack_b
            tower_dict_pos["c"] =  bottom_stack_c



            if tower_dict_pos[destination] == 0 and  tower_dict_pos[source] !=0:
                source_val = (tower_dict[source][tower_dict_pos[source] - 1])
                dest_val =tower_dict[destination][ tower_dict_pos[destination]]
                print(source+str(source_val)+"->"+destination+str(dest_val))
                tower_dict[source][tower_dict_pos[source] - 1] = 0
                tower_dict[destination][tower_dict_pos[destination]] = source_val
                clear()
                print("{:>25}".format("Hanoi-Towers"))
                print()
                for element in reversed(range(7)):
                    print(f"{ring[tower_a[element]]:^15}{ring[tower_b[element]]:^15}{ring[tower_c[element]]:^15}")

                if tower_dict[destination] == tower_win:
                        print(" you won!")
                        break

                else:
                    print()
                    print("Bitte Eingabe von->nach z.B.: 'ac'; Ende mit 'q'")
                    eingabe = input()




            elif tower_dict_pos[source] != 0 and (tower_dict[source][ tower_dict_pos[source]-1])\
                    < tower_dict[destination][ tower_dict_pos[destination]-1]:
                source_val = (tower_dict[source][tower_dict_pos[source]-1])
                dest_val = tower_dict[destination][tower_dict_pos[destination]-1]
                print(source+str(source_val)+"->"+destination+str(dest_val))
                tower_dict[source][tower_dict_pos[source] - 1] = 0
                tower_dict[destination][tower_dict_pos[destination]] = source_val
                clear()
                print("{:>25}".format("Hanoi-Towers"))
                print()
                for element in reversed(range(7)):
                    print(f"{ring[tower_a[element]]:^15}{ring[tower_b[element]]:^15}{ring[tower_c[element]]:^15}")

                if tower_dict[destination] == tower_win:
                        print()
                        print("Gewonnen!!")
                        break

                else:
                    print()
                    print("Bitte Eingabe von->nach z.B.: 'ac'; Ende mit 'q'")
                    eingabe = input()



            else:
                source_pos = (tower_dict[source][tower_dict_pos[source]-1])
                dest_pos = tower_dict[destination][tower_dict_pos[destination]-1]
                print(source + str(source_pos) + "->" + destination + str(dest_pos))
                print("Bitte gültigen Wert eingeben!")
                eingabe = input()




if __name__ == "__main__":
    game()