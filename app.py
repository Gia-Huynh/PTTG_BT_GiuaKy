from models.image_model import Image_Model
from views.root import Root
from controllers.image_controller import Image_Controller

def main():
    image = Image_Model()
    view = Root()
    controller = Image_Controller(image, view)
    view.start()

if __name__ == '__main__':
    main()