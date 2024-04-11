from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


class ClickerApp(App):
    def build(self):
        self.clicks = 0
        self.running = False
        self.label = Label(text=str(self.clicks))
        self.start_button = Button(text='Start')
        self.start_button.bind(on_press=self.start_clicker)
        self.stop_button = Button(text='Stop')
        self.stop_button.bind(on_press=self.stop_clicker)
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.start_button)
        self.layout.add_widget(self.stop_button)
        return self.layout

    def start_clicker(self, instance):
        self.running = True
        Clock.schedule_interval(self.increment_clicks, 1)

    def stop_clicker(self, instance):
        self.running = False

    def increment_clicks(self, dt):
        if self.running:
            self.clicks += 1
            self.label.text = str(self.clicks)

    def on_touch_down(self, touch):
        if self.running:
            self.clicks += 1
            self.label.text = str(self.clicks)


if __name__ == '__main__':
    ClickerApp().run()
