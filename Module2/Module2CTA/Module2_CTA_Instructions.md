# Option #1: Puppy Image Multi-Scale Representation in OpenCV
After completing the Required Reading, you should have a good idea of how to use OpenCV for multi-scale representation of images by pixels matrices. Take a look at this image of a puppy. Being a colored image, this image has three channels, corresponding to the primary colors of red, green, and blue.

1. Import this image (using the link) into OpenCV and write code to extract each of these channels separately to create 2D images. This means that from the n x n x 3 shaped image, you will get 3 matrices of the shape n x n.
2. Now, write code to merge all these images back into a colored 3D image.
3. What will the image look like if you exchange the reds with the greens? Write code to merge the 2D images created in step 1 back together, this time swapping out the red channel with the green channel (GRB).

Be sure to display the resulting images for each step.  Your submission should be one executable Python file.