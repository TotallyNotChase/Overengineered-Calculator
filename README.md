# A very sophisticated simple calculator

This is just a fun little program I made for [r/programmerhumor's Overengineering hackathon](https://www.programmerhumor.org/Hackathon)

It uses the following libraries:
  1. Tkinter
  2. Math
  3. Playsound

The calculator functions *mostly* like a normal calculator, I've not done much bug testing because I kinda procrastinated on the event and only started on the 3rd week.

Couple of things to note however :
  1. The *factorial* will evaluate all *operators* **BEFORE** it and then calculate it.

        for example, ```3+5!``` actually returns ```8!```
  2. Both *log* and *antilog* are currently only supported **ONCE** per calculation. More than one of them will result in a ```Invalid Input```
