# A very sophisticated simple calculator

This is just a fun little program I made for [r/programmerhumor's Overengineering hackathon](https://www.programmerhumor.org/Hackathon)

It's writted in CPython and uses the following libraries:
  1. Tkinter
  2. Math
  3. Playsound

**FEATURES!**
  1. Calculate (duh)!
  2. Did some International Math Association just add a brand new identity/number in the list of `e, pi, i etc`?. Do you feel like some numerical expression just keeps chasing you in whichever math you do?

       Well! Don't fret, with the *add macro* function you can assign your **OWN** numbers, for times when you just can't be bothered to type 22/7 or 7/13!

The calculator functions *mostly* like a normal calculator, I've not done much bug testing because I kinda procrastinated on the event and only started on the 3rd week.

Couple of things to note however :
  1. The *factorial* will evaluate all *operators* **BEFORE** `!` and then calculate it.

        for example, ```3+5!``` actually returns ```8!```
  2. Both *log* and *antilog* are currently only supported **ONCE** per calculation. More than one of them will result in a ```Invalid Input```
