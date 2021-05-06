## Imap
Imap is a tool for visualize the hd-map. This project was inspired by Apollo.
```
data     // hd-map dir
main.py  // main process
map.py  // hd-map struct
editor.py  // user interaction
```

## Quick start
#### Install
There are 2 ways to install imap.
1. Install matplotlib and protobuf.
```
pip install -U matplotlib
pip install protobuf
```

2. Or you can install conda first, then install protobuf. Use `conda install protobuf` to install will fail, I haven't found the reason yet. Replace with the following command will work.
```
pip install protobuf
```

## Example
After the installation is complete, you can view the map with the following command.
```
python main.py -m data/borregas_ave.txt
```

The following is the display of the hd-map in `data\borregas_ave.txt`.  
![map_show](doc/img/map_show.jpg)  


## Todo
1. add argparse.ArgumentParser
2. show map in more details (like layers, styles)  // now
3. select lane to convert color