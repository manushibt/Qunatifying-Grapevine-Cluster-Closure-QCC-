# Qunatifying-Grapevine-Cluster-Closure-QCC-

# Contents
<br/> [Cluster Segmnetation](#cluster-segmnetation)
<br/> [Image thresolding](#image-thresolding)
<br/> [Stat-Analysis](#stat-analysis)

# Cluster Segmnetation

The rpository provide code for running the PSPNet for running the cluster segmnetation in the folder named 'Segmnetation'. 

Step 1: Install PaddleSeg
Before running the code provided in the Segmentation folder, you need to install PaddleSeg. PaddleSeg is an open-source image segmentation framework based on PaddlePaddle. To install PaddleSeg, you can follow the instructions provided in the PaddleSeg documentation. Here's how you can install it using pip:

python
Copy code
!pip install paddleseg

Step 2: Copy the code to the installed PaddleSeg folder
After installing PaddleSeg, you need to copy the code provided in the Segmentation folder to the installed PaddleSeg folder. You can do this by navigating to the PaddleSeg installation folder and copying the files to the Segmentation folder.

Step 3: Train the algorithm
Once you have installed PaddleSeg and copied the code to the Segmentation folder, you can train the PSPNet model on your dataset. To do this, you need to run the train.py script provided in the Segmentation folder. You will need to specify the path to your dataset, the number of epochs to train for, and other hyperparameters. The script will save the trained model to the models directory.

python
Copy code
python train.py --config configs/pspnet/pspnet.yaml

Step 4: Run the algorithm on your collected images
After training the PSPNet model, you can use it to perform cluster segmentation on your collected images. To do this, you need to run the inference.py script provided in the Segmentation folder. You will need to specify the path to your input image and the path to the trained model. The script will generate a segmented image, which you can then use for further analysis.

python
Copy code
python inference.py --config configs/pspnet/pspnet.yaml --model_path models/pspnet/best_model/model.pdparams --image_path data/example.jpg --save_dir results

# Image thresolding

Use the code Calculating_Cluster_Closure to quntify the %CC. Please adjust the paramter path and toggle for contrast enhancement accrodingly.

# Stat Analysis
