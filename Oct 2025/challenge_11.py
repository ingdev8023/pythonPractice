# Image Search
# On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this challenge, you will imitate the image search.

# Given an array of image names and a search term, return an array of image names containing the search term.

# Ignore the case when matching the search terms.
# Return the images in the same order they appear in the input array.

def image_search(images, term):
    searched_images = [image for image in images if term.lower() in image.lower()]    
    return searched_images

image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog")
image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun")
image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG")
image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat")