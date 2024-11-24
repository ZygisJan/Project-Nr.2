import os
from PIL import Image


def combine_images_vertically(image1_path, image2_path, output_path):

    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)

    # Resize the images to the same width if needed
    width = min(img1.width, img2.width)
    img1 = img1.resize((width, img1.height), Image.LANCZOS)
    img2 = img2.resize((width, img2.height), Image.LANCZOS)

    combined_height = img1.height + img2.height

    combined_image = Image.new("RGB", (width, combined_height))
    combined_image.paste(img1, (0, 0))
    combined_image.paste(img2, (0, img1.height))

    combined_image.save(output_path)
    print(f"Combined image saved as '{output_path}'")


def slice_image_into_horizontal_strips(image_path, num_slices, output_path_base):

    img = Image.open(image_path)
    img_width, img_height = img.size

    slice_height = img_height // num_slices

    slices = [img.crop((0, i * slice_height, img_width, (i + 1) * slice_height)) for i in range(num_slices)]

    odd_slices = [slices[i] for i in range(len(slices)) if i % 2 == 0]
    odd_collage = Image.new("RGB", (img_width, slice_height * len(odd_slices)))
    y_offset = 0
    for slice_img in odd_slices:
        odd_collage.paste(slice_img, (0, y_offset))
        y_offset += slice_height
    odd_collage.save(f"{output_path_base}_odd.jpg")
    print(f"Odd slices collage saved as '{output_path_base}_odd.jpg'")

    even_slices = [slices[i] for i in range(len(slices)) if i % 2 != 0]
    even_collage = Image.new("RGB", (img_width, slice_height * len(even_slices)))
    y_offset = 0
    for slice_img in even_slices:
        even_collage.paste(slice_img, (0, y_offset))
        y_offset += slice_height
    even_collage.save(f"{output_path_base}_even.jpg")
    print(f"Even slices collage saved as '{output_path_base}_even.jpg'")


def main(image1_path="collage_odd_slices.jpg", image2_path="collage_even_slices.jpg", num_slices=25):

    combined_output = "combined_image.jpg"
    output_base = "sliced_combined_image"

    print("Combining images...")
    combine_images_vertically(image1_path, image2_path, combined_output)

    print("Slicing the combined image...")
    slice_image_into_horizontal_strips(combined_output, num_slices, output_base)

    print("All tasks completed!")


if __name__ == "__main__":
    main()
