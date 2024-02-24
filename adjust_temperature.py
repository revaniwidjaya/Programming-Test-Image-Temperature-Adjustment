from PIL import Image
import sys

def adjust_temperature(input_path, output_path, temperature):
    try:
        # Open the image
        image = Image.open(input_path)

        # Get the RGB channels
        r, g, b = image.split()

        # Adjust temperature
        r = r.point(lambda i: min(255, max(0, i + temperature)))
        b = b.point(lambda i: min(255, max(0, i - temperature)))

        # Merge the channels back
        adjusted_image = Image.merge('RGB', (r, g, b))

        # Save the result
        adjusted_image.save(output_path)

        print(f"Image temperature adjusted successfully and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python adjust_temperature.py <input_image_path> <output_image_path> <temperature_adjustment>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    try:
        temperature = float(sys.argv[3])
    except ValueError:
        print("Error: Temperature adjustment must be a numeric value.")
        sys.exit(1)

    adjust_temperature(input_path, output_path, temperature)
