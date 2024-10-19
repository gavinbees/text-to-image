# text-to-image
This turns a text file into an image. For size reference, I pasted in approximately 3,000,000 characters and the resulting image was about 650x650. Each alphabetical letter within the text is turned into its corresponding spot in the alphabet, a = 1, b = 2, z = 26, etc. These numbers are used to form RGB values which create a pixel. The array of pixels is then formed together and cropped to create a square image.

warandpeace.jpg is a photo representation of the entirety of War and Peace, about 3 million characters. 
Write the name of your text file on line 60. The image is set to automatically display but PIL allows for saving as well.
