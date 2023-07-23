import clingo

def main():
    ctl = clingo.Control()
    ctl.add("base", [], """

femalecat(ruby;spot;dakota).
malecat(alfredo;bock;cheddar).
activity(ball; laser; cuddling).
kits(1..3).
{litter(X, Y): kits(Y)}=1 :- femalecat(X).
{hobby(X, Y): activity(Y)}=1 :- femalecat(X).
{couple(X, Y): malecat(Y)}=1 :- femalecat(X).

:-couple(dakota, alfredo).

:-couple(X, alfredo),couple(X, bock).
:-couple(X, cheddar),couple(X, bock).
:-couple(X, alfredo),couple(X, cheddar).

:-couple(ruby, X),couple(spot, X).
:-couple(ruby, X),couple(dakota, X).
:-couple(dakota, X),couple(spot, X).

:-litter(dakota, X), litter(ruby, X).
:-litter(dakota, X), litter(spot, X).
:-litter(spot, X), litter(ruby, X).

:-hobby(dakota, X), hobby(ruby, X).
:-hobby(dakota, X), hobby(spot, X).
:-hobby(spot, X), hobby(ruby, X).

hobby(X, ball) :- couple(X, alfredo). 
litter(X, 1) :- couple(X, alfredo).
couple(X, bock) :- hobby(X, laser).
hobby(ruby, cuddling).
litter(dakota, 3).

#show couple/2.
#show litter/2.
#show hobby/2.
            

        """)
    ctl.configuration.solve.models = 0
    ctl.ground([("base", [])])
    ctl.solve(on_model=lambda m: print(m))


if __name__ == "__main__":
    main()