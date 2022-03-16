import re

input_filter = re.compile(r'[aA][bB]|[aA][cC]|[bB][aA]|[bB][cC]|[cC][aA]|[cC][bB]')


ring = dict()
ring[0]="||"
ring[1]="0||0"
ring[2]="00||00"
ring[3]="000||000"
ring[4]="0000||0000"
ring[5]="00000||00000"

tower_a = [5,4,3,2,0,0,0]
tower_b = [2,1,0,0,0,0,0]
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
#            source = source_dest_list[0]
#            destination = source_dest_list[1]
            bottom_stack_a = len([counter_a for element in tower_a if element != 0])
            bottom_stack_b = len([counter_b for element in tower_b if element != 0])
            bottom_stack_c = len([counter_c for element in tower_c if element != 0])
            print(bottom_stack_a, bottom_stack_b, bottom_stack_c)
            tower_dict_pos = dict()
            tower_dict= dict()
            tower_dict["a"] = tower_a
            tower_dict["b"] = tower_b
            tower_dict["c"] = tower_c
            tower_dict_pos["a"] =  bottom_stack_a -1
            tower_dict_pos["b"] =  bottom_stack_b -1
            tower_dict_pos["c"] =  bottom_stack_c -1
            print(tower_dict[destination][tower_dict_pos[destination]])
            print(tower_dict[source][tower_dict_pos[source]])


            if tower_dict_pos[destination] == -1:
                dest_pos =(destination,tower_dict[destination][ tower_dict_pos[destination]])
                source_pos =(tower_dict[source][tower_dict_pos[source]])
                print(str(source) + str(source_pos) +"->"+ str(destination)+str(dest_pos) )
                print("zero")
                eingabe = input()
 #
            elif (tower_dict[source][ tower_dict_pos[source]]) < tower_dict[destination][ tower_dict_pos[destination]]:
                print(tower_dict[destination][ tower_dict_pos[destination]])
                print(tower_dict[source][tower_dict_pos[source]])
                print("pass")
                eingabe = input()

            else:
                print(tower_dict[destination][ tower_dict_pos[destination]])
                print(tower_dict[source][tower_dict_pos[source]])
                print("not possible")
                eingabe = input()
























if __name__ == "__main__":
    game()