import cv2 as cv
from pathlib import Path
from globals import COLORS

class Detection:
    def __init__(self,id,x_min,y_min,x_max,y_max):
        self.class_id=id
        self.x_min=x_min
        self.x_max=x_max
        self.y_min=y_min
        self.y_max=y_max

    def draw(self,file):
        height, width, channels = file.shape
        if 0 <= self.x_min and self.x_min < self.x_max and self.x_max < width and 0 <= self.y_min and self.y_min < self.y_max and self.y_max < height:
            cv.rectangle(file,(self.x_min,self.y_min),(self.x_max,self.y_max),COLORS[self.class_id],1)
        else:
            raise ValueError(f"{self.class_id} {self.x_max} {self.y_min} {self.x_max} {self.x_min}")

class AnotatedImage:
    def __init__(self,path):
        self.path=path
        self.boxes=[]

    def populate(self,data):
        for box in data[self.file_name()]:
            self.boxes.append(Detection(*box))
        self.make_box()
        self.subtitle()

    def subtitle(self):
        cv.rectangle(self.file,(10,10),(35,35),COLORS[1],-1)
        cv.rectangle(self.file,(10,45),(35,70),COLORS[0],-1)
        cv.putText(self.file,"Class 1",(40,32),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255))
        cv.putText(self.file,"Class 0",(40,67),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255))

    def make_box(self):
        self.file=cv.imread(self.path)

        if self.file is None:
            raise FileNotFoundError("Image Not Found")

        for box in self.boxes:
            box.draw(self.file)
        
    def write(self):
        cv.imwrite(Path("resultados/") / self.file_name(),self.file)

    def show(self):
        #cv.namedWindow(self.file_name(), cv.WINDOW_KEEPRATIO)
        cv.imshow(self.file_name(), self.file)
        #cv.resizeWindow(self.file_name(), 1000, 800)

    def close(self):
        cv.destroyWindow(self.file_name())
      
    def file_name(self) -> str:
        return self.path.parts[-1]

    def wait(self):
        while (key := cv.waitKey(0)) != ord("q") and key != ord(" "):
            pass
        if key == ord("q"):
            return False
        else: return True

    def terminal_print(self):
        print(f"File Name: {self.file_name()} \033[92mBoxes: {len(self.boxes)}\033[0m")

