Image filtering involves the application of window operations that perform useful functions, such as noise removal and image enhancement. Compare the effects of mean, median, and Gaussian filters on an image for different kernel windows.

This image contains impulse noise. In OpenCV, write algorithms for this image to do the following:

1. Apply mean, median, and Gaussian filters using a 3x3 kernel. Additionally, for Gaussian, select two different values of sigma. Think about how to select good values of sigma for optimal results.
2. Apply mean, median, and Gaussian filters using a 5x5 kernel. For Gaussian, use the same values of sigma you selected in the above step.
3. Apply mean, median, and Gaussian filters using a 7x7 kernel. For Gaussian, use the same values of sigma you selected in the above step.

Output your filter results as 3 x 4 side-by-side subplots to make comparisons easy to inspect visually. That is, your subplot should have 3 rows (1 for each kernel size) and 4 columns (1 for each filter type, 2 for Gaussian). Be sure to include row and column labels.

Next, write a 2-3 page summary of your output results. Include in your summary, the following:

1. Which filter type is preferred for removal of impulse noise and why? Provide two references of support for your answer and cite them in your summary using correct APA styling.
2. Which filter (include kernel size and sigma, if applicable) performed the best visually? Include details like whether there were image features better preserved and/or better enhanced. Are these preservations and enhancements of image features important? Why or why not?
3. Are your results in line with the preferred method? Discuss why or why not?
