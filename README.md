# XC: Image Segmentation Task

## Part One: Image Generation

<br>

## Structure tree
```
.         
├── annotations                     
|   └── one-label
|       └── ...       
├── images           
|   └── ...     
├── masks          
|   └── ...         
├── pairs
│   └── ...
├── sets                        
|   ├── train
    │   └── ...                            
|   └── train-voc              
|       ├── JPEGImages           
|       ├── SegmentationClass        
|       ├── SegmentationClassPNG                  
|       └── SegmentationClassVisualization        
├── 2voc.py           
├── config.py         
├── images.py       
├── masks.py              
├── README.md           
└── requirements.txt   
```

<br>

## Setup

```
git clone https://github.com/edobytes/xcimg.git
```

```
cd xcimg
```

```
conda create -n xcimg -y python=3.9 && conda activate xcimg

pip install -r requirements.txt 
```

<br> 

## Usage

Edit the global parameters in `config.py` as desired, then run `images.py`:

```
python images.py
```

A set of 100 `jpg` generated images is provided, for reference.

## **IMPORTANT**

### Now manually annotate your image set with [labelme](https://github.com/wkentaro/labelme).

One-label annotations of the included generated images are provided, for reference.

<br>

### Generate Masks

Two options are provided.

### Option A

```
python masks.py
```

This will generate black & white masks and save these in `./masks`, as well as genarating juxtaposed images of the original and the mask (saved in `./pairs`)

Again, for convenience, the aforementioned directories contain the generated masks & pairs resulting from having used the 100 images in `./images`

### Option B

### Convert to VOC format

Given the popularity of the format/task, it is possible to obtain the masks with the structure need by VOC related models.

Copy the contents of `./annotations` and `./images` to `sets/train`, and create a `sets/labels.txt` file, with the following content:

```
__ignore__
_background_
rectangle
```

Note: this is already provided.

Run the following command to convert `labelme`'s annotations format to a `voc` dataset:

```
python 2voc.py sets/train sets/train-voc --labels sets/labels.txt
```
