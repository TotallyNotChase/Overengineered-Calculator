# A very sophisticated simple calculator

This is just a fun little program I made for [r/programmerhumor's Overengineering hackathon](https://www.programmerhumor.org/Hackathon)

It's writted in CPython and uses the following libraries:
  1. Tkinter
  2. Math
  3. Playsound
  4. Path from Pathlib

## Installation:-  

It's compatible with Windows 10, I'm not sure if it'll support other OS(s). But for windows 10 it should just run as long as python and the required modules are installed.
## FEATURES!
  1. Calculate (duh)!

      **EXCEPT!** It actually uses *manual postfix conversion and evaluation* instead of just using eval(), because why not! Watch your time waste itself while the program prints the postfix expression in the terminal and then finally evaluates it, also using postfix evaluation (manually)! ⁿᵒᵗ ᵃᵖᵖˡᶦᶜᵃᵇˡᵉ ᶠᵒʳ ˡᵒᵍ ᵃⁿᵈ ᵃⁿᵗᶦˡᵒᵍ

  2. Did some International Math Association just add a brand new identity/number in the list of `e, pi, i etc`?. Do you feel like some numerical expression just keeps chasing you in whichever math you do?

       Well! Don't fret, with the *add macro* function you can assign your **OWN** numbers, for times when you just can't be bothered to type 22/7 or 7/13!

  3. Bored of the same stupid numbers and need some eyebleach? We got you covered with *kitten* and *puppy* pictures, because adding **useless** stuff and **burning** my own time really adds the **ash** to this **Trash**

  4. Oh and you can also do *Quadratic Equations* with it. Not that anyone cares.

**BONUS FEATURE!** This calculator comes with *text-to-speech* pre installed! For times when you *really* wanna annoy the crap out of the user!

## Usage:-

  1. The calculator itself should be pretty straightforward. You press buttons, it works. The *postfix expressions and evaluations* are printed on the **terminal** so be sure to keep an eye out for that one.

  2. To add macros, type in some **numerical expression**, this can only consist of numbers and basic operators, then either press *enter* while in the **entry screen** or click on the **Add Macro** button. You can only add 5 buttons though.

  3. To see pictures, click buttons. That's it.

  4. To do Quadratic equations, click on the **Quadratic Equation** button and then enter a, b, c `(i.e ax^2 + bx + c = 0)` *in that order* seperated by *space* and then either hit *enter* or click on the **Solve!** button. The roots will appear in the *output screen* (bottom).

## Bugs?

The calculator functions *mostly* like a normal calculator, I've not done much bug testing because I kinda procrastinated on the event and only started on the 3rd week.

**Couple of things to note however** :
  1. When you use the *log* or *antilog*, you cannot back out as the *calculation* is done as soon as you press them, so using backspace will result in (apparently) strange outputs.

  2. Both *log* and *antilog* are currently only supported **ONCE** per calculation. More than one of them will result in a ```Invalid Input```

  3. *antilog* uses the base 10 version.
