import modelos as cls
import arquivos as func
import os

# Main 
def main():
    data=func.csv_read()

    for path in func.get_images_path():

        # Create AnotatedImage Object
        image=cls.AnotatedImage(path)

        # Populate the Image Object with Boxes
        image.populate(data)

        # Display Image in Window
        image.show()

        # Print Info in Terminal
        # os.system('cls' if os.name == 'nt' else 'clear')
        image.terminal_print()

        # Save Image as a Regular File (.jpg)
        image.write()
    
        # Wait User Input
        if image.wait() == False:
            return 1
        else: pass

        # Close Image
        image.close()

if __name__ == "__main__":
    main()