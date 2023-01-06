from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
Window.size=(350,600)


class CalculatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        self.num1_input = TextInput(hint_text='Enter first number', size_hint=(1, 0.1), font_size=20)
        self.num2_input = TextInput(hint_text='Enter second number', size_hint=(1, 0.1), font_size=20)
        self.operator = TextInput(hint_text='Enter operator (+, -, *, /)', size_hint=(1, 0.1), font_size=20)
        self.calculate_button = Button(text='Calculate', size_hint=(1, 0.1), font_size=20)
        self.calculate_button.bind(on_release=self.calculate)
        self.result_label = Label(font_size=20)
        layout.add_widget(self.num1_input)
        layout.add_widget(self.num2_input)
        layout.add_widget(self.operator)
        layout.add_widget(self.calculate_button)
        layout.add_widget(self.result_label)
        return layout

    def calculate(self, instance):
        result = 0
        num1 = int(self.num1_input.text)
        num2 = int(self.num2_input.text)
        operator = self.operator.text
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        self.result_label.text = str(result)


obj=CalculatorApp()
obj.run()