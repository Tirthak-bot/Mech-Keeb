# Mech-Keeb
A Almost Full Sized Mechanical Keyboard, Hot Swappable Switches and coded in KMK Firmware!
<br>

<img  width="286.0" height="400.0" alt="Mech Keeb Zine" src="https://github.com/user-attachments/assets/485a5fb9-195c-4807-827c-9b7315da2d6c" />
<img width="477" height="400" alt="Render Compilation" src="https://github.com/user-attachments/assets/a1a0c49f-2a17-451f-88d9-d2bbba78c092" />

<br>

Making this keyboard because i don't have a *almost full sized decent Keyboard!
<br>
<br>
Using this is pretty straight forward obviously blehh, just connect it to the computer, flash the firmware once and it should just work like a regular keeb moving forward :)

# Schematic
The Schematic was made in KICAD!
<br>

<img width="3300" height="2550" alt="Schematic_page-0001" src="https://github.com/user-attachments/assets/3da5efb1-cf67-42ee-a866-7282277cd896" />

# Layout
The layout was designed on https://www.keyboard-layout-editor.com/, The firmware hasn't yet been edited to match this layout and is currently sitting with placeholders, I will do it once i get the parts irl. Also the Blank keys will be used as arrow keys and macro keys.
<br> 

<img width="1001" height="346" alt="image" src="https://github.com/user-attachments/assets/c3a28d84-f2bf-4f80-90cf-5a6311da8023" />

# PCB
The PCB was designed in KICAD!
<br> 

<img width="1116" height="372" alt="PCB Front" src="https://github.com/user-attachments/assets/12844e3e-e1b4-4697-99ad-c396ef945506" />
<img width="1108" height="365" alt="PCB Front With Components" src="https://github.com/user-attachments/assets/e5777a8a-66ab-4a77-bb52-4eb73e3a128a" />
<img width="1118" height="374" alt="PCB Back" src="https://github.com/user-attachments/assets/c67b7a85-5068-4a9a-a64b-79e29a6e6f55" />
<img width="1118" height="367" alt="PCB Back With Components" src="https://github.com/user-attachments/assets/d50e77d6-c93f-4502-bb17-af00cd736b02" />

# Case
The case was designed in Fusion. PCB to the bottom case and bottom case to top case all is joined by M3 Screws!
<br>

Anyways, here is a ugly ahh blue render of the case bleh :3

<img width="1366" height="573" alt="40209db7-113f-4d1a-9cf5-38ee7798f177" src="https://github.com/user-attachments/assets/70a2d56f-1133-4e57-a0a2-35d54380865a" />

# Firmware
As mentioned above, the firmware is written in python using the KMK Libraries. It will be pushed to the microcontroller using circuit python.

# BOM
|SR.NO|ITEMS|QUANTITY|UNIT PRICE|TOTAL PRICE|URL|
|-----|-----|--------|-----------|-----------|---|
|1|	PCB|	5	|$25|	$125|	https://www.lioncircuits.com/|
|2| 1N4148 1W Zener Diode|	100|	$0.016	|$1.67	|https://robu.in/product/1n4148-1w-zener-diode-pack-of-50/|
|3|	1N5819 1W Diode|	5	|$0.03	|$0.15|	https://robu.in/product/1n5819-1w-diode-pack-of-30/|
|4|	0402 100nf Capacitors SMD|	100|	$0.021|	$2.1	|https://robu.in/product/tcc0402x7r104j500at-cctc-smt-ceramic-capacitors-0402-x7r-104j100nf%C2%B15-0-rated-voltage50v-thickness0-50mm-tape/|
|5|	SK6812 Mini-E	|200|$0.13	|$27	|https://desertcart.in/products/690911592|
|6|	RPI PICO|	1	|$4.1	|$4.1	|https://robu.in/product/raspberry-pi-pico/|
|7|	0.96 inch I2C OLED Display|	1|	$2.12|	$2.12	|https://robu.in/product/0-96-inch-i2c-iic-oled-lcd-module-4pin-with-vcc-gnd-blue/|
|8|	Cherry MX Style Switches|	2 Sets|	$16|	$32|	https://stackskb.com/store/akko-fairy-pro-switch-pack-of-45/|
|9|	EC11 Rotary Encoder|	1	|-|	-|	Self Sourced|
|10|	Hot Swap Sockets	|90	|$0.11|	$9.6|	https://stackskb.com/store/gateron-hotswap-sockets/|
|11|	Keyboard Stabilizers	|1 Set| (4 + 1; 6.25U)|	$17|	$17|	https://stackskb.com/store/durock-clear-screw-in-stabilizers-v2/|
|12|	Keycaps	|1 Set	|$14|	$14|	https://stackskb.com/store/veekos-gradient-keycaps-cherry-profile-135-keys/|
|13|	Assorted M3 Screws|	-|	-|	-|	Self Sourced|
|14|	M3 Heat Inserts	|-|	-	|-	|Self Sourced|
|15|	Filament Spool(For 3D Printing the case)|	1 Roll|	$8	|$11|	https://india.numakers.com/products/pla-metallic#|
|16|	A Set of tweezers|	1 Set|	$2	|$2	|https://robu.in/product/anti-static-tweezers-6pcs-set-vetus-bga-esd/|
||TOTAL:||			$250||	



