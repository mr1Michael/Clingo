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

"""Cats in Spring
On a beautiful Spring day in the park, there were three female cats - Ruby, Spot and, Dakota - walking together 
and gossiping about their humans. Up ahead, there were three male cats - Alfredo, Bock, and Cheddar - walking 
together bragging about their conquests. When the two groups met, there were three cupids flying through the air. 
Next thing you knew, there were three couples walking away in separate directions. The couples began talking and 
soon found that they had amazing things in common. Well, long story short, we all know what happens to cats that 
fall in love in the springtime, oh my what a racket! From this information and the following clues, can you 
determine each females' male companion, her favorite activity and how many kittens - 1, 2, or 3 - she had in her l
itter?

- Alfredo chose the female who liked to chase a ball, but she was not Dakota.
- Bock's companion liked to chase the laser light.
- Ruby loved to cuddle up to her male for a long afternoon nap in the sun.
- Dakota had two more kittens than Alfredo's companion.

Write a Clingo program that returns a stable model for the puzzle above. Add an English sentence for each rule 
of the program as an explanatory comment. If necessary, add more comments about your program and describe your 
steps towards a solution."""
