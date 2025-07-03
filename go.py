from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button  
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import math

Window.size = (300, 500)

class Calc(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.is_scientific = False

        self.result = TextInput(
            font_size=45, size_hint_y=0.2, readonly=True, halign="right", multiline=False,
            background_color=(0.2, 0.2, 0.2, 1),  # dark grey result box
            foreground_color=(1, 1, 1, 1)
        )
        
        self.mode_button = Button(
            text="Change to Sci. Mode", size_hint_y=0.2, on_press=self.mode,
            background_normal='', background_color=(0.1, 0.5, 0.8, 1), color=(1,1,1,1)
        )
        self.add_widget(self.mode_button)
        self.add_widget(self.result)

        self.main_grid = GridLayout(cols=4, spacing=5, padding=10)
        self.build_buttons()
        self.add_widget(self.main_grid)

    def build_buttons(self):
        self.main_grid.clear_widgets()

        buttons = [
            ['AC', 'C', '+/-', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '00', '.', '=']
        ]

        for row in buttons:
            for item in row:
                button = Button(
                    text=item, font_size=32, on_press=self.butn_onclick,
                    background_normal=''
                )

                if item in ['AC', 'C']:
                    button.background_color = (1, 0.3, 0.3, 1)  # red
                elif item in ['/', '*', '-', '+', '=', '+/-']:
                    button.background_color = (1, 0.7, 0, 1)  # orange
                else:
                    button.background_color = (0.3, 0.3, 0.3, 1)  # dark grey
                    button.color = (1,1,1,1)

                self.main_grid.add_widget(button)

        if self.is_scientific:
            sci_buttons = ['sin', 'cos', 'tan', 'log', 'sqrt', '^', ')', '(']
            for func in sci_buttons:
                button = Button(
                    text=func, font_size=28, on_press=self.butn_onclick,
                    background_normal='',
                    background_color=(0.2, 0.6, 0.5, 1),  # teal for sci functions
                    color=(1,1,1,1)
                )
                self.main_grid.add_widget(button)

    def mode(self, instance):
        self.is_scientific = not self.is_scientific
        instance.text = "Basic Mode" if self.is_scientific else "Change to Sci. Mode"
        self.build_buttons()

    def butn_onclick(self, instance):
        text = instance.text
        if text == "AC":
            self.result.text = ""
        elif text == "C":
            if self.result.text:
                self.result.text = self.result.text[:-1]
        elif text == "=":
            self.calculate()
        elif text == "+/-":
            self.toggle_neg()
        elif text == "%":
            self.convert()
        elif text in ['sin', 'cos', 'tan', 'log', 'sqrt']:
            self.result.text += text + '('
        elif text == '^':
            self.result.text += '**'
        else:
            self.result.text += text

    def calculate(self):
        try:
            expression = self.result.text

            for func in ['sin', 'cos', 'tan']:
                expression = expression.replace(f"{func}(", f"math.{func}(math.radians(")

            open_radians = expression.count('math.radians(')
            close_parentheses = expression.count(')')
            total_open = expression.count('(')
            if total_open > close_parentheses:
                expression += ')' * (total_open - close_parentheses)

            for func in ['log', 'sqrt']:
                expression = expression.replace(f"{func}(", f"math.{func}(")

            result = round(eval(expression),4)
            self.result.text = str(result)
        except Exception as e:
            self.result.text = "error"
            print("Calculation error:", e)

    def toggle_neg(self):
        if self.result.text:
            self.result.text = self.result.text[1:] if self.result.text[0] == '-' else '-' + self.result.text

    def convert(self):
        try:
            self.result.text = str(float(self.result.text) / 100)
        except ValueError:
            self.result.text = "error"

class CalcApp(App):
    def build(self):
        return Calc()

if __name__ == "__main__":
    CalcApp().run()
