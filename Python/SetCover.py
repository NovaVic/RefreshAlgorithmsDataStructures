# The problem is from Grokking Algorithms book.
#I solved the problem in my own way.
#Problem statement:
#Assume there are n number of states and m number of stations
# A station broadcasts music to one or more states
#we have to find set of stations such that every state is covered 

#Basically we are trying to pick radio stations which would cover all states.

#States to broadcast music to

states_needed = set(["mt","wa", "or", "id", "nv", "ut", "ca", "az"])

#list of stations versus state(s) covered by the stations.
stations = {}
stations["one"] = set(["id","nv","ut"])
stations["two"] = set(["wa", "id", "mt"])
stations["three"] = set(["or","nv", "ca"])
stations["four"] = set(["nv","ut"])
stations["five"] = set(["ca", "az"])



#preserving original list of stations
def deep_copy_stations(stations):
    stations_deep_copy = {}
    for station, states  in stations.items():
        stations_deep_copy[station] = states

    return stations_deep_copy


#Figuring out number of stations covering states in a country is basically the classic 
#set cover problem from the Algorithm books. 
    
def set_cover(stations, states_needed):
    #debugging
    #print(states_needed)
    #print(stations)
    final_stations = set()
    
    if len(states_needed) > 0:
        states_covered = set()

    while True:
        saved_picked_states = set()
        max_len_station = 0
        best_station = None
        for station, states_for_station in stations.items():
            #print(station, states_for_station)
            picked_states = (states_for_station - states_covered)
            print("picked_states",picked_states)
            if  len(picked_states & states_needed) <= 0:
                print("checking next ")
                continue
            num_picked_states = len(picked_states)
         
            if num_picked_states > max_len_station:
                max_len_station = num_picked_states  
                best_station = station  
                saved_picked_states = picked_states

            if best_station == None:
                raise Exception("The stations do not cover all the states")
            states_covered = states_covered | saved_picked_states
            print("states_covered", states_covered)
            states_needed = states_needed - states_covered 
            final_stations = final_stations | {best_station}
            #print(best_station)
            print("final_stations", final_stations)
        try:
            stations.pop(best_station)
        except KeyError:
            raise KeyError
        
        if len(stations) == 0 and len(states_needed) > 0:
           raise Exception("the stations do not cover all states")
        if len(states_needed) <=0:
            print("all states covered")
            break
    return final_stations

	
	
if __name__ == "__main__" :
    stations_deep_copy = deep_copy_stations(stations)
    #print(stations_deep_copy)
	
	#list of stations to cover all states
    final_stations = set_cover(stations_deep_copy, states_needed)
    #debugging
	print(states_needed)	
	
    print(sorted(final_stations, reverse=True))
         
# Theoretical to do
#compute complexity


