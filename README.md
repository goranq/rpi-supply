# rpi-supply

## Description
Crawler/Parser for [rpilocator|https://rpilocator.com]. It can be used for
setting up alerts based on availability of specific SKU.
The script will request (GET) `https://rpilocator.com?instock` and parse the
response. It will show all available SKUs and color code ones that user
specifies.
Created for learning purposes.

### Usage
Specify important SKUs in `SKUs` variable. 
Run the script by invoking
```bash
python3 rpi-supply.py
```
or make file `rpi-supply.py` executable and run it with
```bash
./rpi-supply.py
```