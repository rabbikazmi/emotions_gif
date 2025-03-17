import imageio as iio

filenames = [r"C:\Users\Rabbika Azmi\OneDrive\Desktop\{}.png".format(i) for i in range(1, 10)] #to generate file path dynamically
images = []   #empty list to store the images

for filename in filenames:
    try:                                       #error handling
        images.append(iio.imread(filename))
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

if images:
    iio.mimsave("emotions.gif", images, duration=500, loop=0) #duration of images in milliseconds and loop=0 means it keeps on looping forever
    print("GIF created successfully!")
else:
    print("No images found. Check file paths.")
