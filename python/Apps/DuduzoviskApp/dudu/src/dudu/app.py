import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class MyApp(toga.App):
    def startup(self):
        # Cria uma janela principal
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Adiciona um botão
        btn = toga.Button(
            'Clique Aqui',
            on_press=self.on_button_click,
            style=Pack(padding=10)
        )

        main_box.add(btn)

        self.main_window = toga.MainWindow(title=self.name)
        self.main_window.content = main_box
        self.main_window.show()

    def on_button_click(self, widget):
        self.main_window.info_dialog('Olá!', 'Você clicou no botão!')

def main():
    return MyApp('Meu App', 'com.seunome.meuapp')

