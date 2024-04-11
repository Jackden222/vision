from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from plyer import platform
from jnius import autoclass

# Используйте pyjnius для взаимодействия с Android API
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')
WindowManager = autoclass('android.view.WindowManager$LayoutParams')


class OverlayWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(OverlayWindow, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (300, 200)
        self.pos = (Window.width - self.width, 0)

        # Создайте кнопки
        self.start_button = Button(text='Start', size_hint=(
            0.3, 0.2), pos=(0, self.height - self.height * 0.2))
        self.stop_button = Button(text='Stop', size_hint=(0.3, 0.2), pos=(
            self.width - self.width * 0.3, self.height - self.height * 0.2))
        self.reload_button = Button(text='Reload', size_hint=(0.3, 0.2), pos=(
            self.width // 2 - self.width * 0.15, self.height - self.height * 0.2))

        # Добавьте обработчики событий
        self.start_button.bind(on_press=self.start_app)
        self.stop_button.bind(on_press=self.stop_app)
        self.reload_button.bind(on_press=self.reload_app)

        # Добавьте кнопки на экран
        self.add_widget(self.start_button)
        self.add_widget(self.stop_button)
        self.add_widget(self.reload_button)

    def start_app(self, instance):
        print("Starting the app...")

    def stop_app(self, instance):
        print("Stopping the app...")

    def reload_app(self, instance):
        print("Reloading the app...")


class OverlayApp(App):
    def build(self):
        # Создайте окно
        overlay_window = OverlayWindow()

        # Сделайте окно системным оповещением
        if platform == 'android':
            PythonActivity.mActivity.getWindow().addFlags(
                WindowManager.FLAG_NOT_FOCUSABLE | WindowManager.FLAG_NOT_TOUCHABLE)

        return overlay_window


if __name__ == '__main__':
    OverlayApp().run()
