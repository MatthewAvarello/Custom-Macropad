# Matthew's Lovely Macropad
My macropad is a 9 key macropad with a rotary encoder and an OLED screen! It uses KMK Firmware
## PCB
### Schematic:
The 9 keys are positioned in a 3x3 matrix, saving 3 gpio pins for other use

![Schematic](images/Screenshot%202026-03-31%20211731.png)
### PCB:
![PCB](images/Screenshot%202026-03-31%20211716.png)
## CAD:
Two part Case is held by two m3 screws and heatset inserts
![CAD](images/Screenshot%202026-03-31%20211629.png)
![CAD](images/Screenshot%202026-03-31%20211648.png)
![CAD](images/Screenshot%202026-04-04%20121243.png)
## Firmware:
* Uses KMK Firmware to power the PCB
* Keys act as a numberpad, unless 9 is held, in which the numbers turn into their respective function keys.
* Rotary encoder outputs arrows, button is unbound.
* OLED screen shows whether you are in Normal or function key mode
## BOM
* 9x Cherry MX Switches
* 9x DSA Keycaps
* 2x M3x5x4 HeatSet Inserts
* 2x M3x16mm Screws
* 9x Through the hole 1N4148 Diodes
* 1x 0.91" 128x32 OLED Screen
* 1x EC11E Rotary Encoder
* 1x XIAO RP2040
* 1x The Case (3d Printed Top and Bottom)
* 1x Soldering Iron (Unforunately do not have one)
## Room for Improvement
Looking back I would have changed the following if I had more time.

* Extended the top case print so that the case used 4 screws instead of 2. This would have probably helped structural stability
* Made the keybinds on the firmware more interesting and useful for every day use
* Made the wiring on the PCB more orderly instead of a jumbled mess 💀

## Random Other Notes
CAD was definetely the hardest part for me, arguably took around 80% of the total time I spent on the project. However, it was a great learning experience!

