import pyaudio
import numpy as np
import random
import os
import time
import threading
from pystyle import Center

maxValue = 2**16
p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=2,rate=44100,
              input=True, frames_per_buffer=1024)


ascii1 = '''

                    ___                                                    ___
 __________________/  /space                      space __________________/  /
| _    _______    /  /space                       space| _    _______    /  /
|(_) .d########b. //)|space _____________________ space|(_) .d########b. //)|
|  .d############//  |space|        _____        |space|  .d############//  |
| .d######""####//b. |space|() ||  [ YUX ]  || ()|space| .d######""####//b. |
| 9######(  )#_//##P |space|()|__|  | = |  |__|()|space| 9######(  )#_//##P |
| 'b######++#/_/##d' |space|() ||   | = |   || ()|space| 'b######++#/_/##d' |
|  "9############P"  |space|   ||   |___|   ||   |space|  "9############P"  |
|  _"9a#######aP"    |space|  _   _____..__   _  |space|  _"9a#######aP"    |
| |_|  `""""''       |space| (_) |_____||__| (_) |space| |_|  `""""''       |
|  ___..___________  |space|_____________________|space|  ___..___________  |
| |___||___________| |space                       space| |___||___________| |
|____________________|space                       space|____________________|

'''

ascii2 = r"""

 @@@@@ /                                      / @@@@@
@@@@@@@ /                                    / @@@@@@@
@@@@@@@ /          @@@@@@@@@@@@@@@           / @@@@@@@
 @@@@@@@@ /      @@@@@@@@@@@@@@@@@@@       / @@@@@@@@
     @@@@@ /    @@@@@@@@@@@@@@@@@@@@@    / @@@@@
       @@@@@ / @@@@@@@@@@@@@@@@@@@@@@@ / @@@@@
         @@ /  @@@@@@@@@@@@@@@@@@@@@@@@@ / @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@  BY  @@@@ YUX  @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@ /  @@@@@@@@@@@@@@@@@  / @@
           @@@@ / @@@@ @ @ @ @ @@@@ / @@@@
          @@@@@ /  @@@ @ @ @ @ @@@  / @@@@@
        @@@@@ /     @@@@@@@@@@@@@     / @@@@@
      @@@@ /         @@@@@@@@@@@         / @@@@
   @@@@@ /             @@@@@@@             / @@@@@
  @@@@@@@ /                               / @@@@@@@
   @@@@@ /                                 / @@@@@


"""


def visualize():
    while True:
        data = np.fromstring(stream.read(1024),dtype=np.int16)
        data = data[1::2]
        peak = np.abs(np.max(data)-np.min(data))/maxValue
        if round(peak, 1) > 0.1:
            print('[#####                  ]')
        if round(peak, 1) > 0.2:
            print('[############           ]')
        if round(peak, 1) > 0.3:
            print('[##################     ]')
        if round(peak, 1) < 0.1:
            print('[                       ]')    


def visualize2():
    while True:
        data = np.fromstring(stream.read(1024),dtype=np.int16)
        data = data[1::2]
        peak = np.abs(np.max(data)-np.min(data))/maxValue
        peak = int(str(round(peak, 1)).split('.')[1])
        print(f"{'-'*peak*3}")


def visualize_radio():
    global ascii1
    while True:
        data = np.fromstring(stream.read(1024),dtype=np.int16)
        data = data[1::2]
        peak = np.abs(np.max(data)-np.min(data))/maxValue
        peak = int(str(round(peak, 1)).split('.')[1])
        asciia = ascii1.replace('space', '-'*peak*3)
        print(Center.Center(asciia))


def visualize_skull():
    global ascii1
    while True:
        data = np.fromstring(stream.read(1024),dtype=np.int16)
        data = data[1::2]
        peak = np.abs(np.max(data)-np.min(data))/maxValue
        peak = int(str(round(peak, 1)).split('.')[1])
        asciia = ascii2.replace('/', '@'*peak*3)
        print(Center.Center(asciia))


for i in range(5):
    x = threading.Thread(target=visualize_skull)
    x.start()