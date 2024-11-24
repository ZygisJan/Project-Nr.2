import os
from PIL import Image

def make_collage_from_single_image(image_path, filename, num_slices, strip_indices=None):

    if not os.path.exists(image_path):
        print(f"Image '{image_path}' not found!")
        return False

    img = Image.open(image_path)
    img = img.convert("RGB")
    img_width, img_height = img.size

    slice_width = img_width // num_slices

    slices = [img.crop((i * slice_width, 0, (i + 1) * slice_width, img_height)) for i in range(num_slices)]

    if strip_indices is not None:
        slices = [slices[i] for i in strip_indices]

    collage_width = len(slices) * slice_width

    collage_image = Image.new('RGB', (collage_width, img_height), (35, 35, 35))

    x = 0
    for slice_img in slices:
        collage_image.paste(slice_img, (x, 0))
        x += slice_width

    collage_image.save(filename)
    print(f"Collage saved as '{filename}'")
    return True


def main(image_path="Ice_age.jpg", num_slices=25):

    output_filename_odd = "collage_odd_slices.jpg"
    output_filename_even = "collage_even_slices.jpg"

    print('Making collage with odd slices...')
    odd_indices = [i for i in range(num_slices) if i % 2 == 0]
    make_collage_from_single_image(image_path, output_filename_odd, num_slices, strip_indices=odd_indices)

    print('Making collage with even slices...')
    even_indices = [i for i in range(num_slices) if i % 2 != 0]
    make_collage_from_single_image(image_path, output_filename_even, num_slices, strip_indices=even_indices)

    print('All collages are ready!')


if __name__ == '__main__':
    main()



