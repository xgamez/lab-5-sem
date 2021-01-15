from abc import ABC, abstractmethod


def define_resolution(platform):
    if platform == "Стационарный ПК":
        return "2560x1600"
    elif platform == "Переносной ПК":
        return "1600x1200"
    elif platform == "Смартфон":
        return "1280x1024"


class Window(ABC):

    @abstractmethod
    def paint(self, resolution):
        pass


class Button(ABC):

    @abstractmethod
    def paint(self):
        pass


class Checkbox(ABC):

    @abstractmethod
    def paint(self):
        pass

    @abstractmethod
    def paint_with_button(self, button):
        pass


class Textfield(ABC):

    @abstractmethod
    def paint(self):
        pass


class GUIFactory(ABC):

    @abstractmethod
    def create_window(self):
        pass

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

    @abstractmethod
    def create_textfield(self):
        pass


class WinWindow(Window):

    def paint(self, resolution):
        return f"Создание и отрисовка окна с разрешением {resolution} в стиле Windows"


class MacWindow(Window):

    def paint(self, resolution):
        return f"Создание и отрисовка окна с разрешением {resolution} в стиле macOS"


class LinuxWindow(Window):

    def paint(self, resolution):
        return f"Создание и отрисовка окна с разрешением {resolution} в стиле Linux"


class WinButton(Button):

    def paint(self):
        return "Отрисовка кнопки в стиле Windows"


class MacButton(Button):

    def paint(self):
        return "Отрисовка кнопки в стиле macOS"


class LinuxButton(Button):

    def paint(self):
        return "Отрисовка кнопки в стиле Linux"


class WinCheckbox(Checkbox):

    def paint(self):
        return "Отрисовка чек-бокса в стиле Windows"

    def paint_with_button(self, button):
        if type(button) == WinButton:
            result = button.paint()
            return f"Отрисовка чек-бокса и {result}"
        else:
            raise ValueError


class MacCheckbox(Checkbox):

    def paint(self):
        return "Отрисовка чек-бокса в стиле macOS"

    def paint_with_button(self, button):
        if type(button) == MacButton:
            result = button.paint()
            return f"Отрисовка чек-бокса и {result}"
        else:
            raise ValueError


class LinuxCheckbox(Checkbox):

    def paint(self):
        return "Отрисовка чек-бокса в стиле Linux"

    def paint_with_button(self, button):
        if type(button) == LinuxButton:
            result = button.paint()
            return f"Отрисовка чек-бокса и {result}"
        else:
            raise ValueError


class WinTextfield(Textfield):

    def paint(self):
        return "Отрисовка текстового поля в стиле Windows"


class MacTextfield(Textfield):

    def paint(self):
        return "Отрисовка текстового поля в стиле macOS"


class LinuxTextfield(Textfield):

    def paint(self):
        return "Отрисовка текстового поля в стиле Linux"


class WinFactory(GUIFactory):

    def create_window(self):
        return WinWindow()

    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()

    def create_textfield(self):
        return WinTextfield()


class MacFactory(GUIFactory):

    def create_window(self):
        return MacWindow()

    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

    def create_textfield(self):
        return MacTextfield()


class LinuxFactory(GUIFactory):

    def create_window(self):
        return LinuxWindow()

    def create_button(self):
        return LinuxButton()

    def create_checkbox(self):
        return LinuxCheckbox()

    def create_textfield(self):
        return LinuxTextfield()


def client_code(factory):
    window = factory.create_window()
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    textfield = factory.create_textfield()

    print(window.paint(define_resolution("Стационарный ПК")))
    print(window.paint(define_resolution("Переносной ПК")))
    print(window.paint(define_resolution("Смартфон")))
    print(button.paint())
    print(checkbox.paint())
    print(textfield.paint())
    print(checkbox.paint_with_button(button))


if __name__ == "__main__":
    print("Клиентский код на Windows")
    client_code(WinFactory())

    print('\n')

    print("Клиентский код на macOS")
    client_code(MacFactory())

    print('\n')

    print("Клиентский код на Linux")
    client_code(LinuxFactory())