from PIL import Image


def validate_image(image_path):

    try:
        image = Image.open(image_path)

        width, height = image.size

        # Minimum image size
        if width < 200 or height < 200:
            return False, "Image Too Small"

        # Blank image detection
        gray = image.convert("L")

        histogram = gray.histogram()

        non_zero_pixels = sum(histogram)

        if non_zero_pixels == 0:
            return False, "Blank Image"

        return True, "Valid Image"

    except Exception:
        return False, "Invalid Image"