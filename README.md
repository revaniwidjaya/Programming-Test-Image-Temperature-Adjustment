# Programming-Test-Image-Temperature-Adjustment

1. **Import Libraries:**
   ```python
   from PIL import Image
   import sys
   ```
   We import necessary tools to work with images (`Image` from the Pillow library) and handle command-line input (`sys`).

2. **Define `adjust_temperature` Function:**
   ```python
   def adjust_temperature(input_path, output_path, temperature):
   ```
   This function will change the color tones of an image to make it look warmer or cooler. It needs the path of the input image, the path to save the output image, and a temperature adjustment value.

3. **Try-Except Block:**
   ```python
   try:
   ```
   We try to do something (in this case, adjust the image temperature), and if there's an issue, we'll handle it in the "except" part.

4. **Open the Image:**
   ```python
   image = Image.open(input_path)
   ```
   We open the image from the given file path.

5. **Split RGB Channels:**
   ```python
   r, g, b = image.split()
   ```
   The image is separated into its color components: red (r), green (g), and blue (b).

6. **Adjust Temperature - Red Channel:**
   ```python
   r = r.point(lambda i: min(255, max(0, i + temperature)))
   ```
   We make the image warmer by increasing the intensity of the red color. The lambda function ensures the values stay within the valid range.

7. **Adjust Temperature - Blue Channel:**
   ```python
   b = b.point(lambda i: min(255, max(0, i - temperature)))
   ```
   Similarly, we make the image cooler by reducing the intensity of the blue color.

8. **Merge Channels Back:**
   ```python
   adjusted_image = Image.merge('RGB', (r, g, b))
   ```
   We combine the adjusted red, green, and blue components to get the final image.

9. **Save the Result:**
   ```python
   adjusted_image.save(output_path)
   ```
   We save the adjusted image to the specified output path.

10. **Print Success Message:**
    ```python
    print(f"Image temperature adjusted successfully and saved to {output_path}")
    ```
    If everything goes well, we print a success message.

11. **Exception Handling:**
    ```python
    except Exception as e:
        print(f"Error: {e}")
    ```
    If something goes wrong (an exception occurs), we print an error message.

12. **Main Block for Command-Line Usage:**
    ```python
    if __name__ == "__main__":
        if len(sys.argv) != 4:
            print("Usage: python adjust_temperature.py <input_image_path> <output_image_path> <temperature_adjustment>")
            sys.exit(1)
    ```
    We check if the script is being run directly and if the correct number of command-line arguments is provided. If not, we print a usage message and exit.

13. **Parse Command-Line Arguments:**
    ```python
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    try:
        temperature = float(sys.argv[3])
    except ValueError:
        print("Error: Temperature adjustment must be a numeric value.")
        sys.exit(1)
    ```
    We get the input image path, output image path, and temperature adjustment value from the command line. We make sure the temperature is a valid number.

14. **Call `adjust_temperature` Function:**
    ```python
    adjust_temperature(input_path, output_path, temperature)
    ```
    We use the provided function to adjust the temperature of the image based on the given parameters. As for the example, i use the temperature of -10, so the result in the output image is the colder and bluer tone than the input image. 
