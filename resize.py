# this file do  resize  or padding multiple images at the same time   



from PIL import Image
import os, shutil
# import os

# Resize function
def resize_image():
    
    print ("Resizing Images with maxemum dimensions of:")
    # Directory Path for trainging data
    path = get_path
    # path = "/CS/JCU/Paper/FAC_2018/Identify_the_Digits/data/train_dist2_copy_padded/"

    # make dir for output
    output_dir = os.path.join(path, 'output')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    max_size = (0,0)
    images_path = []

    images = os.listdir(path)
    for image_path in images:
        if image_path.endswith("jpg"):
            image_path = path+image_path
            images_path.append(image_path)
            image = Image.open(image_path)
            if max_size < image.size:
                max_size = image.size

    print (max_size)
    # print (images_path)
    # Ratio to resize
    # desired_size = max(max_size)   # if you want maxemum ratio of the largest image in the folder
    desired_size = int(input('Enter the image width:')) # if you want exact ratio 

    for im_pth in images_path:
        im = Image.open(im_pth)
        old_size = im.size  # old_size[0] is in (width, height) format
        # print im.size

        ratio = float(desired_size)/max(old_size)
        new_size = tuple([int(x*ratio) for x in old_size])
        # # use thumbnail() or resize() method to resize the input image

        # # # thumbnail is a in-place operation

        # # im.thumbnail(new_size, Image.ANTIALIAS)

        im = im.resize(new_size, Image.ANTIALIAS)
        # # # create a new image and paste the resized on it

        new_im = Image.new("RGB", (desired_size, desired_size))
        new_im.paste(im, ((desired_size-new_size[0])//2, (desired_size-new_size[1])//2))

        # new_im.show()
        new_im.save(path+"output/%s" % im_pth.replace(path, ""))
    print ("Done!")

# padding function
def pad_image():
    print ("Padding Images.....")

    # Directory Path for trainging data
    path = get_path
    # path = "/CS/JCU/Paper/FAC_2018/Identify_the_Digits/data/train_dist2_copy_padded/"

    # make dir for output
    output_dir = os.path.join(path, 'output')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    max_size = (0,0)
    images_path = []

    images = os.listdir(path)
    for image_path in images:
        if image_path.endswith("jpg"):
            image_path = path+image_path
            images_path.append(image_path)
            image = Image.open(image_path)
            if max_size < image.size:
                max_size = image.size

    desired_size = max_size
    background = Image.new("RGB", desired_size)
    
    for im_pth in images_path:
        im = Image.open(im_pth)
        cp = background.copy()
        cp.paste(im,((desired_size[0]-im.size[0])//2, (desired_size[1]-im.size[1])//2))
        cp.save(path+"output/%s" % im_pth.replace(path, ""))
    print ("Done!")

# get file path from user
get_path = input('Enter the image path in this format  /../../ :')
print('The image path is:', get_path)

# get function from user
get_def=input('To (resize) press: r  to (pad) press: p :')

# run the function
if get_def == "p":
    pad_image()
elif get_def=="r":
    resize_image()


# resize_image()
# pad_image()