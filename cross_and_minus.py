import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView


class MainApp(App):
    def __init__(self):
        super().__init__()
        self.switch = True

    def clk(self, win):
        self.title = f"Победил {win}"
        popup = ModalView(size_hint=(0.75, 0.5))
        victory_label = Label(text=f"Победил {win}", font_size=50)
        popup.add_widget(victory_label)
        popup.bind(on_dismiss=self.restart)
        popup.open()

    def restart(self, arg):
        self.switch = True
        for button in self.buttons:
            button.color = [0, 0, 0, 1]
            button.text = ""
            button.disabled = False

    def diagonal_win(sign, index, z):
        WIN = [9, 10, 11]
        for p in WIN:
            win_Y = 1
            if len(z) > (index + p * 4):
                for i2 in range(1, 5):
                    if z[index + p * (i2)] == str(sign):
                        win_Y += 1
            if win_Y == 5:

                break
        return win_Y

    def tic_tac_toe(self, arg):
        arg.disabled = True
        arg.text = "X"
        self.win()

    def win(self):
        z = []
        for i in range(100):
            z.append(self.buttons[i].text)
        win_x = win_y = win_Y = win_X = index = 0
        for i in z:
            win_Y = win_x = win_y = 0
            if i == "X":
                win_y = win_Y = 0
                win_x += 1
                win_X = int(MainApp.diagonal_win("X", index, z))
            elif i == "O":
                win_x = win_X = 0
                win_y += 1
                win_Y = int(MainApp.diagonal_win("O", index, z))
            index += 1
            if win_y == 5 or win_Y == 5:
                self.clk("Х")
                break
            elif win_x == 5 or win_X == 5:
                self.clk("О")
                break
        self.bot()

    def bot(self):
        while True:
            x = random.randint(0, 100)
            if self.buttons[x].text == "":
                self.buttons[x].disabled = True
                self.buttons[x].text = "O"
                break

    def build(self):
        self.title = "Крестики-нолики"
        root = BoxLayout(orientation="vertical", padding=10)
        grid = GridLayout(cols=10)
        self.buttons = []
        for _ in range(100):
            button = Button(disabled=False, on_press=self.tic_tac_toe)
            self.buttons.append(button)
            grid.add_widget(button)
        root.add_widget(grid)
        root.add_widget(Button(text="Сброс", size_hint=[1, 0.1], on_press=self.restart))

        return root


if __name__ == "__main__":
    MainApp().run()
