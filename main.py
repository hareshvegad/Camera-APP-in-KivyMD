from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.list import MDList, OneLineAvatarListItem, ImageLeftWidget
import os
import time
from kivy.utils import platform

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])


Builder.load_file("homescreen.kv")


class Homescreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # GET SELECTOR FROM KV FILE CAMERA
        self.mycamera = self.ids.camera
        self.myimage = Image()
        self.resultbox = self.ids.resultbox
        self.mybox = self.ids.mybox

    def captureyouface(self):
        # CREATE TIMESTAMP NOT FOR YOU FILE IMAGE
        # THIS SCRIPT GET TIME MINUTES AND DAY NOW
        timenow = time.strftime("%Y%m%d_%H%M%S")

        # GET THE INTERNAL STORAGE DIRECTORY
        internal_storage = MDApp.get_running_app().user_data_dir

        # CREATE DIRECTORY IF NOT EXISTS
        save_path = os.path.join(internal_storage, "YourAppImages")
        os.makedirs(save_path, exist_ok=True)

        # AND EXPORT YOU CAMERA CAPTURE TO PNG IMAGE
        image_path = os.path.join(save_path, f"myimage_{timenow}.png")
        self.mycamera.export_to_png(image_path)
        self.myimage.source = image_path
        self.resultbox.add_widget(
            OneLineAvatarListItem(
                ImageLeftWidget(
                    source=image_path,
                    size_hint_x=0.3,
                    size_hint_y=1,
                    # AND SET YOU WIDTH AND HEIGHT YOU PHOTO
                    size=(300, 300),
                ),
                text=self.ids.name.text,
            )
        )


class MyApp(MDApp):
    def build(self):
        return Homescreen()


if __name__ == "__main__":
    MyApp().run()
