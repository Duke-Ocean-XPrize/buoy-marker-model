# Buoy Acquisition Markers
> Close range drone buoy acquisition system


Drone buoy aquisition model. 

## How to Run with OpenCV

To run with openCV use this image: https://www.dropbox.com/s/loaaepfcw0dh9lz/PiBackup.img?dl=0

OpenCV should be pre-installed

Run:

```sh
cd ~/Desktop/buoy-marker-model
source ~/.profile
workon cv
```

This should drop you into an env with openCV

To test that the install is working

```sh
python
>> import cv2
```

You should now be ready to install requirements and run arcuo_tracker

## Installation

OS X & Linux:

```sh
python install -r requirements.txt
python server.py
python arcuo_tracker.py
```




## Usage example

Run python arcuo_tracker.py. Starts OpenCV. Find the fiducial markers. Pass data to server via Serial

## Development setup

```sh
python install -r requirements.txt
python server.py
python arcuo_tracker.py
```

## Release History

* 0.0.1
    * Work in progress

## Meta

Matthew Kenney – [@baykenney](https://twitter.com/baykenney) – mk365@duke.edu

[https://github.com/Duke-Ocean-XPrize/buoy-marker-model](https://github.com/Duke-Ocean-XPrize/buoy-marker-model)

## Contributing

1. Fork it (<https://github.com/Duke-Ocean-XPrize/buoy-marker-model/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request



 
 
 
 
