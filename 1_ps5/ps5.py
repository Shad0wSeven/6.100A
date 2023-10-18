"""
# Problem Set 5
# Name: Ayush Nayak
# Collaborators: None
# Time: 30 minutes
"""
from PIL import Image, ImageFont, ImageDraw
import numpy

def make_matrix(color):
    """
    Generates a transformation matrix for the specified color. When matrix 
    multiplied with a single RGB pixel, it transforms the pixel into a filtered 
    version representing the specified color deficiency.
    
    Inputs:
        color: string with exactly one of the following values: 'red', 'blue',
               'green', or 'none'
    
    Returns:
        matrix: a transformation matrix corresponding to deficiency in that color
    """
    # You do not need to understand exactly how this function works.
    if color == 'red':
        c = [[.567, .433, 0], [.558, .442, 0], [0, .242, .758]]
    elif color == 'green':
        c = [[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.142, 0.858]]
    elif color == 'blue':
        c = [[.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, .525]]
    elif color == 'none':
        c = [[1, 0., 0], [0, 1, 0.], [0, 0., 1]]
    return c


def apply_transform(m, t):
    """
    Applies the transformation matrix `t` to the input matrix `m`
    
    Inputs:
        m: the input matrix
        t: the transform matrix
    
    Returns:
        result: matrix product of t and m in a list of floats
    """
    product = numpy.matmul(t, m)
    if type(product) == numpy.int64:
        return float(product)
    else:
        result = list(product)
        return result


def img_to_pix(filename):
    """
    Takes a filename (must be inputted as a string with proper file attachment 
    ex: .jpg, .png) and converts that image file to a list of its pixels.

    For RGB images, each pixel is a tuple of (R,G,B) values.
    For BW images, each pixel is an integer.

    Note: Don't worry about determining if an image is RGB or BW.
          The PIL library functions you use will return the correct pixel 
          values for either image mode.

    Inputs:
        filename: string representing an image file, such as 'img_name.jpg'
    
    Returns: list of pixel values
             in form (R,G,B) such as [(0,20,55), (30,50,90), ...] for RGB image
             in form L such as [60, 66, 72...] for BW image
    """
    im = Image.open(filename)
    pixels = list(im.getdata())
    return pixels


def pix_to_img(pixels, size, mode):
    """
    Creates an Image object from a inputted set of RGB tuples.

    Hint: 
        Step 1: Create a new image object with the specified size and model
        Step 2: Populate the image object with the pixels. Search for putdata()!

    Inputs:
        pixels: a list of pixels such as the output of `img_to_pixels`
        size: a tuple of (width, height) representing the dimensions of the 
              desired image. Assume that size is a valid input such that
              size[0] * size[1] == len(pixels).
        mode: 'RGB' or 'L' to indicate an RGB image or a BW image, respectively

    Returns:
        img: Image object made from list of pixels
    """
    im = Image.new(mode, size)
    im.putdata(pixels)
    return im


def filter(pixels, color):
    """
    Applies the specified color deficiency to the pixels

    Note: recall each RGB channel of the pixel must have an integer value!

    Inputs:
        pixels: a list of RGB pixels (ex: [(0,20,55), (30,50,90), ...] )
        color: 'red', 'blue', 'green', or 'none'. 
               string indicating the simulated color deficiency.

    Returns: list of pixels in same format as earlier functions,
             transformed by matrix multiplication
    """
    
    # Step 1: Create the transformation matrix
    matrix = make_matrix(color)
    
    # Step 2: Apply the transformation matrix to each pixel
    result = []
    for pixel in pixels:
        z = apply_transform(pixel, matrix)
        # convert to tuple of ints
        if type(z) == list:
            z = tuple(map(int, z))
        else:
            z = int(z)
        result.append(z)
    return result


def extract_end_bits(num_bits, pixel):
    """
    Extracts the last `num_bits` bits of each pixel if BW or the last `num_bits` 
    bits from each pixel channel if RGB.

    Example for BW pixel:
        num_bits = 5
        pixel = 214

        214 in binary is 11010110. 
        The last 5 bits of 11010110 is 10110.
                              |||||
        The integer representation of 10110 is 22, so we return 22.

    Example for RBG pixel:
        num_bits = 3
        pixel = (214, 17, 8)

        last 3 bits of 214 (in binary, 11010110)
            - 110 --> 6
        last 3 bits of 17 (in binary, 10001)
            - 001 --> 1
        last 3 bits of 8 (in binary, 1000)
            - 000 --> 0

        The integer representation of the 3 least significant bits
        of the R, G, and B channels are 6, 1, and 0, respectively.
        Therefore, we return (6, 1, 0).

    Inputs:
        num_bits: the number of bits to extract
        pixel: if BW, an integer within [0, 255]
               if RGB, a tuple with each channel value within [0, 255]

    Returns: 
        result:
            - if BW, an integer (the last `num_bits` bits of pixel)
            - if RGB, a tuple (the last `num_bits` bits of each channel value in the pixel)
    """
    if type(pixel) == int:
        return pixel & (2**num_bits - 1)
    else:
        result = []
        for channel in pixel:
            result.append((channel & (2**num_bits - 1)))
        return tuple(result)

def reveal_bw_image(filename):
    """
    Extract the hidden image from the base image by creating a new list of pixels 
    using 1 LSB from each pixel in the BW input image 

    Inputs:
        filename: string, input BW file to be processed
    
    Returns:
        result: an Image object containing the hidden image
    """

    # Step 1: Get the pixels from the image
    pixels = img_to_pix(filename)

    # step 2 get height and width of image
    im = Image.open(filename)
    width, height = im.size

    # step 3 convert to image with LSB
    result = []
    for pixel in pixels:
        result.append(255 * extract_end_bits(1, pixel))
    
    # print (result[1:10])

    # step 4 create new image from LSBs
    im = pix_to_img(result, (width, height), 'L')
    return im

def reveal_color_image(filename):
    """
    Extract the hidden image from the base image by creating a new list of pixels 
    using the 3 LSBS from each pixel channel in the RGB input image 
    
    Inputs:
        filename: string, input RGB file to be processed
    
    Returns:
        result: an Image object containing the hidden image
    """
    
    # Step 1: Get the pixels from the image
    pixels = img_to_pix(filename)

    #find image width and height
    im = Image.open(filename)
    width, height = im.size
    
    # Step 2: Extract the 3 LSBs of each pixel channel
    result = []
    for pixel in pixels:
        a, b, c = extract_end_bits(3, pixel)
        m = 255.0/7.0
        n = (int(a * m), int(b * m), int(c * m))
        result.append(n)

    print (result[1:10])
    
    # Step 3: Create a new image from the LSBs with size
    im = pix_to_img(result, (width, height), 'RGB')
    return im


def reveal_image(filename):
    """
    Extracts the single LSB (for a BW image) or the 3 LSBs (for a color image) 
    for each pixel in the input image. 
    
    Hint: you can use a function to determine the mode of the input image (BW or RGB)
          and then use this mode to determine how to process the image.
    
    Inputs:
        filename: string, input BW or RGB file to be processed
    
    Returns:
        result: an Image object containing the hidden image
    """
    im = Image.open(filename)

    if im.mode == '1' or im.mode == 'L':
        return reveal_bw_image(filename)
    elif im.mode == 'RGB':
        return reveal_color_image(filename)
    else:
        raise Exception("Invalid mode %s" % im.mode)


def draw_kerb(filename, kerb, font_color="white"):
    """
    Draws the text "kerb" onto the image located at "filename" and returns a PDF.
    
    Inputs:
        filename: string, input BW or RGB file
        kerb: string, your kerberos
    
    Output:
        Saves output image to "filename_kerb.xxx"
    """
    # split something like "filename.png" into "filename" and ".png"
    ix = filename.find(".")
    old_filename, extension = filename[:ix], filename[ix:] 
    
    font = ImageFont.truetype("noto-sans-mono.ttf", 40)
    im = Image.open(filename)
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), kerb, font_color, font=font)
    
    filename_with_kerb = old_filename + "_kerb" + extension
    im.save(filename_with_kerb)


def main():
    pass

    # Uncomment the following lines to test part 1

    # small_bw_image.png is a 6x2 image which spans from 0 to 253
    small_bw_pixels = img_to_pix('small_bw_image.png')
    
    # small_rgb_pixels.png is a 6x2 image which spans from (0,0,0) to (0,253,253)
    small_rgb_pixels = img_to_pix('small_rgb_image.png')

    im = Image.open('image_15.png')
    width, height = im.size
    pixels = img_to_pix('image_15.png')
    # # print(pixels[0])

    non_filtered_pixels = filter(pixels, 'none')
    # print(non_filtered_pixels[0])
    # im = pix_to_img(non_filtered_pixels, (width, height), 'RGB')
    # im.show()
    # im.save('non_filtered_image.png')

    # red_filtered_pixels = filter(pixels, 'red')
    # im2 = pix_to_img(red_filtered_pixels, (width, height), 'RGB')
    # im2.show()

    # Uncomment the following lines to test part 2
    # Use image_object.save("filename") to save your filtered/unhidden images

    # print(extract_end_bits(3, 13))
    # im = reveal_image('hidden1.bmp')
    # im.show()
    # im.save('unhidden1.bmp')

    im2 = reveal_image('hidden2.bmp')
    im2.show()
    im2.save('unhidden2.bmp')

    # draw_kerb('non_filtered_image.png', 'ayushn', font_color="black")
    # draw_kerb('unhidden1.bmp', 'ayushn')
    draw_kerb('unhidden2.bmp', 'ayushn')

    # When calling draw_kerb() on image_15 (section 2.5), you may pass in 
    # font_color="black" as a parameter to make the watermark stand out against 
    # the white background.  

if __name__ == '__main__':
    main()