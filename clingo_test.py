import clingo

def main():
    ctl = clingo.Control()
    ctl.add("base", [], """
    
directors(fionafantastic; guygalaxy; hollyhunter; keithking).
titles(dreamsofJuly; harvestsun; jackysteel; miltonvale).
durations(50; 60; 70; 80).
{credits(X,Y,Z): durations(Z), titles(Y)}=1:-directors(X).
:- credits(X,Y,Z), credits(A,B,Z), X!=A, Y!=B.
:- credits(X,Y,Z), credits(A,Y,C), X!=A, Z!=C.
:- credits(X,Y,Z), credits(X,B,C), Y!=B, Z!=C.
:- credits(X,Y,Z), credits(A,Y,Z), X!=A.
:- credits(X,Y,Z), credits(X,B,Z), Y!=B.
:- credits(X,Y,Z), credits(X,Y,C), Z!=C.
:-credits(hollyhunter, miltonvale, _).
:-credits(hollyhunter, dreamsofJuly, _).
D1 = D + 10 :- credits(_, miltonvale, D1), credits(_, harvestsun, D).
D1 = D + 10 :- credits(_, dreamsofJuly, D1), credits(_, miltonvale, D).
D1 = D + 20 :- credits(hollyhunter, _, D1), credits(guygalaxy, _, D).
D = 50 :- credits(keithking, _, D).
#show credits/3.

    """)
    ctl.configuration.solve.models = 0
    ctl.ground([("base", [])])
    ctl.solve(on_model=lambda m: print(m))

if __name__ == "__main__":
    main()

"""Ocala International Film Festival
The Ocala International Film Festival is being held this week and four films will be presented. The films have been 
created by directors and have some duration. Using only the clues that follow, determine the director, running time 
and title of each film, as well as the country in which each was produced.
Directors: Fiona Fantastic, Guy Galaxy, Holly Hunter, Keith King
Titles: Dreams of July, Harvest Sun, Jacky Steel, Milton Vale
Durations: 50, 60, 70, 80 min.

Clues

1. Holly Hunter's film is either Harvest Sun or Jacky Steel .
2. Keith King's film has a running time of 50 minutes.
3. Harvest Sun is 10 minutes shorter than Milton Vale.
4. Milton Vale is 10 minutes shorter than Dreams of July.
5. Guy Galaxy's film is 20 minutes shorter than Holly Hunter's film."""