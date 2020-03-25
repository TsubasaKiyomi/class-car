class Mobile_phone:
    def call(self):
        print("電話機能")


class To_mail(Mobile_phone):
    def mail(self):
        print("mail")


class To_camera(Mobile_phone):
    def camera(self):
        print("camera")


class Touch_panel(Mobile_phone):
    def touch_panel_display(self):
        print("touch_panel_display")


class Earphone(Mobile_phone):
    def pairing(self):
        print("pairing")


class Music(Mobile_phone):
    def musics(self):
        print("musics")


class Recognition(Mobile_phone):
    def face_recognition(self):
        print("顔認証")


class Latest_phone(Mobile_phone):
    def all_functions(self):
        print("全機能")

    def mail(self):
        print("メール機能")

    def touch_panel_display(self):
        print("タッチパネル式")

    def pairing(self):
        print("ペアリング機能")

    def musics(self):
        print("音楽機能")

    def face_recognition(self):
        print("顔認証機能")

    def camera(self):
        print("カメラ機能")


latest_phone = Latest_phone()
latest_phone.all_functions()
latest_phone.call()
latest_phone.mail()
latest_phone.musics()
latest_phone.camera()
latest_phone.touch_panel_display()
latest_phone.pairing()
latest_phone.face_recognition()


# to_camera = To_camera()
# to_camera.call()
# to_camera.camera()


# music1 = Music()
# music1.call()
# music1.musics()
