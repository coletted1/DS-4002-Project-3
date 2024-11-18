# DS-4002-Project-3

## Section 1 - Software & Platform

The main software used for this project includes VS Code with Python. We used Python's PyTorch and TensorFlow libraries, an image based system used to build and train models for image based recognition and model optimization. 

Most coding was performed on a Windows machine, with some portions done using a Mac.

## Section 2 - Map of Documentation

### Project Folder Strcutre:

```
DS-4002-Project-3/
│
├── DATA/
│   ├── banana
│   │   ├── fresh
│   │   └── spoiled
│   ├── lemon
│   │   ├── fresh
│   │   └── spoiled
│   ├── lulo
│   │   ├── fresh
│   │   └── spoiled
│   ├── mango
│   │   ├── fresh
│   │   └── spoiled
│   ├── orange
│   │   ├── fresh
│   │   └── spoiled
│   ├── strawberry
│   │   ├── fresh
│   │   └── spoiled
│   ├── tamarillo
│   │   ├── fresh
│   │   └── spoiled
│   └── tomato
│       ├── fresh
│       └── spoiled
│
├── OUTPUT/
│   ├── Analysis/
│   │   ├── 
│   │   └── 
│   └── Exploratory/
│       ├── banana_average_color_histogram.png
│       ├── lemon_average_color_histogram.png
│       ├── lulo_average_color_histogram.png
│       ├── mango_average_color_histogram.png
│       ├── orange_average_color_histogram.png
│       ├── strawberry_average_color_histogram.png
│       ├── tamarillo_average_color_histogram.png
│       └── tomato_average_color_histogram.png
│
├── SCRIPTS/
│   ├── ExploratoryPlot.py
│   └── 
│
├── LICENSE.md
└── README.md
```

- **DATA/**: Contains the various image files used throughout the project, including the images sorted based on fruit type, and on a predetermined freshness level.
- **OUTPUT/**:
  - **Exploratory/**: Contains exploratory plots for each of the fruits based on color intensity from the fresh and spoiled fruits for initial data trends.
    
- **SCRIPTS/**: Python scripts used in the project:
  - **1-ExploratoryPlot.py**: Generates exploratory vizualzations for data insights.

## Section 3 - Instructions for reproducing results

Follow the steps below to reproduce the results of this project: 
### Step 1 : Dataset Collection 
- Download the fruit image data from [mendeley.data](https://data.mendeley.com/datasets/bdd69gyhv8/1). This dataset contains 16,000 images, documentaing 16 different fruits with varying freshness levels.
- Download the images from each of the fruit categories, and then depending on the fruit presented in the image, place the downloaded image files in the DATA/ folder of the project in their own respective file. The images given in the dataset are pre-sorted based on fruit type, and if they were already classified as being fresh or spoiled.
- 

### Step 2 : Pre - Process images 

### Step 3 : Build and Train Model

### Step 4 : Evaluate Model

### Step 5 : Evaluate Results 

---

## References 
[1] P. S. Giovany Cesar, P. A. Orlando Javier, and J.-M. Robinson, “Spoiled and fresh fruit inspection dataset,” Mendeley Data, vol. 1, Nov. 2020, doi: https://doi.org/10.17632/6ps7gtp2wg.1.

[2] admiral 360, “Fruit sorting machine to reduce waste - Ingivision,” Ingivision, Sep. 17, 2024. https://www.ingivision.com/2024/09/17/how-fruit-sorting-machines-help-reduce-waste/ (accessed Nov. 04, 2024).

[3] J. Davis, “Food Waste in the United States,” Ballard Brief, 2022. https://ballardbrief.byu.edu/issue-briefs/food-waste-in-the-united-states
[4]“OpenCV,” opencv.org. https://opencv.org

[5]F. Chollet, “Building powerful image classification models using very little data,” Keras.io, 2016.https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html

[6]G. Boesch, “Pytorch vs Tensorflow: A Head-to-Head Comparison,” viso.ai, Mar. 02, 2021. https://viso.ai/deep-learning/pytorch-vs-tensorflow/

[7]“AI Deploy - Tutorial - Deploy an ONNX model using FastAPI,” Ovhcloud.com, 2016. https://help.ovhcloud.com/csm/en-public-cloud-ai-deploy-densenet-onnx-fastapi?id=kb_article_view&sysparm_article=KB0059789 (accessed Nov. 04, 2024).
