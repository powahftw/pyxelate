## Example

![example](http://i.imgur.com/I9Vibs4.jpg)


```
python pyxelate.py parrot.jpg
```
Here you see both the original and the edited close togheter. Made with [juxtapose-py](https://github.com/powahftw/juxtapose-py)



# pyxelate
Python script that given an image as input and some parameter it create a low-res version by analyzing color frequency on sub-block


### Prerequisites

This script make uses of the Python Imaging Library: PIL. You need to install it before running it

### Usage

You can use it by launching like

```
python pyxelate.py <inputpath> [additional arguments]
```

You can have a look at the addictional parameter with 

```
python pyxelate.py -h
```

```
-d Dimension of the PixelBlock | Default is 15
```

### Other Example 


```
python pyxelate.py cat.jpg -d 25
```

![example](http://i.imgur.com/hMmmkab.jpg)



### Final notes

On small image, to achive better result the script double the dimension, otherwise the image's dimensions shouldn't change

The color frequency part of the script is based on [this](http://blog.zeevgilovitz.com/detecting-dominant-colours-in-python/).
It uses Colour Frequency since in a fraction of an image it's a good guess at what the average color is

The first Example image was created with another script which i created for the occasion [juxtapose-py](https://github.com/powahftw/juxtapose-py)

This script was developed in a short timeframe and as such there might be some occasional problem and some better optimization possibile. I appreciate any type of feedback :) 
