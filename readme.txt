Project Name: Rice Grain Variety Dataset Creation
Course: Introduction to Image Processing (IIP)

----------------------------------------
SYSTEM REQUIREMENTS
----------------------------------------
• Python 3.x
• Required Python Libraries:
  - numpy
  - scikit-image
  - pandas
  - matplotlib

(OpenCV is NOT used as per project rules)

----------------------------------------
PROJECT FOLDER STRUCTURE
----------------------------------------

Project_Folder/
│
├── RawImages/
│   ├── PK386/
│   │   ├── L1F23BSCS0608_PK386_Raw_001.jpg
│   │   ├── L1F23BSCS0608_PK386_Raw_002.jpg
│   │   └── ...
│   ├── SuperKernel/
│   └── ...
│
├── GrainImages/
│   ├── L1F23BSCS0608_PK386_Raw_001_Grain_0001.jpg
│   ├── L1F23BSCS0608_PK386_Raw_001_Grain_0002.jpg
│   └── ...
│
├── metadata.csv
├── scripts
│   └── main.py
│
├── Group Members.txt
├── Readme.txt
└── Bonus Claim.txt (optional)

----------------------------------------
INPUT FILES LOCATION
----------------------------------------
• Store all captured RAW images inside:
  RawImages/<Variety_Name>/

• Naming format for RAW images:
  <RollNo>_<VarietyName>_Raw_XXX.jpg

Example:
L1F23BSCS0608_PK386_Raw_001.jpg

----------------------------------------
OUTPUT FILES LOCATION
----------------------------------------
• Extracted grain images are saved in:
  GrainImages/

• Naming format for grain images:
  <RawFileName>_Grain_XXXX.jpg

Example:
L1F23BSCS0608_PK386_Raw_001_Grain_0001.jpg

• Metadata file:
  metadata.csv (stored in main project folder)

----------------------------------------
HOW TO RUN THE PROJECT
----------------------------------------
1. Place all raw images in the correct RawImages folder structure.
2. Open terminal / command prompt in the project folder.
3. Run the following command:

   python main.py

also make sure your python environment is in

../Rice_Project/scripts/

----------------------------------------
PROCESSING STEPS
----------------------------------------
• Convert image to grayscale
• Apply thresholding for segmentation
• Morphological cleanup
• Remove border objects
• Identify reference object for scale
• Extract individual grains
• Rotate grains vertically
• Crop and save grain images
• Extract features (height, width, orientation, average color)
• Save all features to metadata.csv

----------------------------------------
NOTES
----------------------------------------
• No OpenCV is used.
• scikit-image is used as allowed.
• Grain images are stored in a single folder with continuous numbering.
