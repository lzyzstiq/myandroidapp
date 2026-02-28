from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # 简单的布局：一个标签和一个按钮
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Hello, Kivy!')
        btn = Button(text='点我', on_press=self.on_button_press)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_button_press(self, instance):
        self.label.text = '你点击了按钮！'

if __name__ == '__main__':
    MyApp().run()
