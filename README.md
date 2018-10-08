# mosaic

This utility can be used to generate [photo-mosaic](http://en.wikipedia.org/wiki/Photographic_mosaic) images, to use it you must have Python installed, along with the [Pillow](http://pillow.readthedocs.org/en/latest/) imaging library.

As well as an image to use for the photo-mosaic ([most common image formats are supported](http://pillow.readthedocs.org/en/latest/handbook/image-file-formats.html)), you will need a large collection of different images to be used as tiles. The tile images can be any shape or size (the utility will automatically crop and resize them) but for good results you will need a lot of them - a few hundred at least. One convenient way of generating large numbers of tile images is to [extract screenshots from video files](https://trac.ffmpeg.org/wiki/Create%20a%20thumbnail%20image%20every%20X%20seconds%20of%20the%20video) using [ffmpeg](https://www.ffmpeg.org/).

**Prerequisites**
<pre>pip install scikit-image numpy</pre>

**Usage**
```python
create_mosaic(
    subject="/path/to/source/image", 
    target="/path/to/output/image", 
    tile_paths=["/path/to/tile_1" , ... "/path/to/tile_n"],
    tile_ratio=1920/800, # Crop tiles to be height/width ratio
    tile_width=300, 
    enlargement=20, # Mosiac will be this times larger than original
    reuse=False, # Should tiles be used multiple times?
    color_mode='L',  # RGB (color) L (greyscale)
) 
```
The images below show an example of how the mosaic tiles are matched to the details of the original image:

![Mosaic Image](http://codebox.org.uk/graphics/mosaic/mosaic_small.jpg)  
<span class="smallText">Original</span>

[![Mosaic Image Detail](http://codebox.org.uk/graphics/mosaic/mosaic_detail.jpg)](http://codebox.org.uk/graphics/mosaic/mosaic_large.jpg)  
<span class="smallText">Mosaic Detail (click through for [full mosaic](http://codebox.org.uk/graphics/mosaic/mosaic_large.jpg) ~15MB)</span>

Producing large, highly detailed mosaics takes much time! We are comparing every tile pixel against every mosaic sector to produce a best match. Other libraries simplify this by only comparing against a single pixel from the original sector, or to compare against the sector's histogram.

Changed from original project (https://github.com/codebox/mosaic):  
*   ability to not reuse tiles 
*   increased quality of match by comparing against whole tile images 
*   increased quality of mosaic by starting with the center instead of top left
*   ability to input color mode

Tested with:
*   Python 3.6.5
*   numpy==1.14.4
*   Pillow==5.1.0
*   scikit-image==0.14.1

