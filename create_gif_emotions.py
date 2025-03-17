import imageio as iio

filenames = [r"C:\Users\Rabbika Azmi\OneDrive\Desktop\{}.png".format(i) for i in range(1, 10)]
images = []

for filename in filenames:
    try:
        images.append(iio.imread(filename))
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

if images:
    iio.mimsave("emotions.gif", images, duration=500, loop=0)
    print("GIF created successfully!")
else:
    print("No images found. Check file paths.")
