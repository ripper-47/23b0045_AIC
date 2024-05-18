# AI Based Hackathon Preparation

## <u>Problem Statement</u>   :  
### Automatic detecton of Plant diseases from leaf images

## Week 1: 
### Goal: Team formation, dataset collection and research on problem statement

1. In the inital stages, divide the roles of dataset collection and research between the team members. 
2. Look for open source datasets like Plantsvillage. Take help of local farmers too in diversifying and labeling the dataset. 
3. If the data obtained is less, use image augementation to broaden the dataset as well as prevent overfitting in the future,
4. Look up research papers on similar problems on the web like cance diagnosis, skin disease detection in humans etc. Reading these research papers will give much intitution on what the structure of your model should be.

## Week 2: 
### Goal: Exploratory data analysis (EDA) and Data Preprocessing

1. Use graphs/histograms/box plots to visualize the distribution of data and distribution of variables. 
2. Checking the relationships between variables to understand how they might affect each other. This includes computing correlation coefficients and creating correlation matrices.
3. Identifying relationship between various variables can further help in identifying algorithms, model building and feature engineering.
4. Preprocess the dataset acquired. Look out for any missing values. Convert the images to the required format for the model. Apply data augmentation pipeline (rotation, flipping, cropping) to increase dataset size and variability.
5. Determine an optimal loss-function for the problem.

## Week 3: 
### Goal: Model Development

1. Implement and test out different relationships founded during EDA. Compare there results.
2. Experiment with different model architechtures like VGG, Resnets and Inception and add custom layers to enhance them.
3. Split the dataset into training, validaton and testing. Ensure that the training and validation sets have similar class distribution.

## Week 4:
### Goal: Model Evaluation and Deployment

1. Fine-tune the hyperparameters by using grid-search on different fixed parameters like learning_rate, batch size, layers in the neural network of the model and the variables in loss function.
2. Address the overfitting (performing well on training data but not on test data) or underfitting (performing bad even on training data) by adjusting model complexity and regularization parameters.
3. Select the best performing model accordingly.
4. Now prepare the model for deployment. Ensure that the model can handle inputs in real-time and produce outputs smoothly.
