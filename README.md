# Assetto Corsa car power modifier

## Description

Modifies selected cars' power via changing the 'power.lut' file in car data folder

## Getting Started

### Installing

* Simply clone or download the py file directly 

### Executing program

* Make sure your car data is not encrypted(A 'data' folder rather than a data.acd file)
* Execute the program by running:
```
python AC_power_modifier.py \
  --path <AC /content/cars/ path> \
  --carname <name of the car folder> \
  --initial_power <current power output of the car> \
  --target_power <your desired power of the car>
```
The defalut path is set at D:/Steam/steamapps/common/assettocorsa/content/cars/.
