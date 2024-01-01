# Dog Breeds Classification

This study introduces a convolutional neural network (CNNs) model designed to recognize dog breeds from images and, intriguingly, determine which dog breed a human face resembles. Leveraging a dataset comprising 133 different dog categories and a substantial collection of 8,351 dog images, along with 13,233 human images, this model endeavors to provide both practical and entertaining outcomes. With 133 dog breeds in the dataset, each with unique characteristics, it's important to accurately recognize dogs and their breeds. In this report, we explore methods for identifying dog breeds using convolutional neural networks (CNNs). We compare our custom CNN design with a model created using a technique called transfer learning. To assess our approach, we also compare our CNN's performance to three established models: VGG16, VGG19, and ResNet-50. Our proposed model is a combination of ResNet-50 and VGG19, resulting in a model that excels in recognizing and classifying a wide range of dog breeds and identifying human faces that resemble them.

## Proposed Algorithm for Humans and Dogs Classification

### Algorithm Strengths: 
As our proposed model is a combination of ResNet-50 and VGG19 algorithms, one of the key strengths of this algorithm is its ability to identify mixed-breed dogs within an image. It not only detects the presence of mixed breeds but also provides information of the top two likely breeds. Another strength of this algorithm is its ability to handle scenarios where neither a dog nor a human is present in the image. In such cases, the algorithm provides clear feedback by indicating that it cannot detect either a dog or a human. The algorithm also demonstrates impressive flexibility in identifying humans who may be wearing accessories such as dog ears or dog nose. This adaptability to human features, combined with its primary purpose of detecting dogs, makes it suitable for applications involving human-dog hybrids, costumes, or creative compositions. It adds an element of fun and creativity to the algorithm's capabilities. 

### Algorithm Weakness: 
One of the algorithm's weaknesses is its difficulty in distinguishing between dogs and humans in images that contain both species. When a picture includes both a dog and a human, the algorithm tends to prioritize dog detection and categorization. As a result, it may incorrectly report that it can detect a dog, even when a human is visible in the image. This limitation can lead to false positives in cases where the primary subject of interest is a human.

## Web App using Flask

Here are example of the interface that was developed to support the visualization and interaction with the dog classification model.

<div align="center">
    <img src="resource_dog/images/Screenshot 2567-01-01 at 16.53.44.png" style="height: 500px; width: auto;">
</div>
After uploading the image, the website displays the upload image before showing the prediction result for easier comparison.<br><br> 


<div align="center">
    <img src="resource_dog/images/Screenshot 2567-01-01 at 16.54.41.png" style="height: 500px; width: auto;">
</div>
In the source code, we set a threshold of 0.99 or 99 percent confidence for the algorithm to classify a dog as mix-breed or not. Meaning, the model has to be at least 99 certain that the input image is not mix-breed dog. The picture above shows the outcome where the algorithm found this dog to be a mix-breed.<br><br> 


<div align="center">
    <img src="resource_dog/images/Screenshot 2567-01-01 at 16.55.43.png" style="height: 500px; width: auto;">
</div>
In the case where the algorithm cannot detect neither human nor dog, it classified the object as "Alien"!. The above visualization demonstrates the specific respond for this particular case. <br><br> 


Remark: For testing the model performance, we took the image from Google Image and Unplash (https://unsplash.com/photos/smiling-woman-holding-cheek-B4TjXnI0Y2c)


### System Description
Utilizing web applications to showcase the outcomes of our prediction models through interactive, engaging, and user-friendly interfaces. This web application developed using Flask offers a seamless experience, making advanced analytics accessible to both experts and novices alike. 

To enhance the algorithm's ability to recognize mixed breed dogs, we have refined our predictive model. Now, it produces results for the top two breeds with the highest likelihood, presented neatly in a nested JSON format. This enriched output includes the probability score, specific dog breed, and a link to a representative image for each breed.

Before delivering the final result, we run a series of checks using our face and dog detection models, proposed in the prior steps. This ensures we present the most accurate visualization on the web application. We assess if the uploaded dog image represents a mixed breed by comparing the top probability against a threshold of 99%. If the dog is deemed mixed breed, our web application displays images of the top two most likely breeds, accompanied by their names and predicted probabilities in percentage. However, for a purebred dog, we present a sample image that matches the identified breed. On the other hand, If a human face is detected, we pair it with a dog breed that shares visual similarities, displaying the breed's name and its probability score. This result is derived from our enhanced dog classification model, focusing solely on the top probable breed. If neither a dog nor a human is discerned, we opt not to display additional imagery.

Furthermore, users can upload multiple images, though one at a time. There's no need to return to the homepage after each upload; simply scroll down post-prediction to add a new image. For a seamless experience and to avoid potential glitches, the prediction button remains inactive until an image file is uploaded.

Due to space limitation, we pivoted from Google Colab to Kaggle for our algorithm development, which offered more storage. While Kaggle restricts the creation of HTML templates, we designed the web application's interface locally, embedding placeholders for the model's results and the dog images. Post development, this template was pushed to GitHub, and subsequently cloned into Kaggle. To host the web application, we leveraged the ngrok API. For a seamless experience, please sign up with ngrok and use your API Token when running the application. Here are some of the snippets from our Dog Classification Web Application!


## Conclusion 
In summary, this paper has highlighted the performance disparities between a CNN model that we built from scratch and those developed through transfer learning: VGG16, VGG19 and ResNet-50, with the latter proving to be significantly more effective due to their ability to harness pre-trained network weights. However, the most important point of our study is our proposed model, a combination of ResNet-50 and VGG19, designed for dog breed classification, human detection, and the recognition of mixed breeds. This model distinguishes itself through its capacity to accurately detect dogs and humans, predict dog breeds, identify mixed breeds, and even discern humans, even when they sport dog accessories. The fusion of these capabilities makes our model a robust tool for a wide array of image recognition tasks.


## Thank you!
