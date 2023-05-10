import os.path

path_apk = 'data/data/com.vlad.runer/files/app/'


class players:
    def __init__(self, name):
        self.path_img = f"sprite/{name}/"

    def anim_run(self, anim):
        self.idel_textures = []
        len_ = len(os.listdir(f"{self.path_img}/{anim}/"))
        for i in range(len_):
            texture = f"{self.path_img}{anim}/{anim.lower()}{i+1}.png"
            self.idel_textures.append(texture)
        return self.idel_textures, len_ - 1
