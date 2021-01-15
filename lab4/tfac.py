import unittest
from unittest import TestCase
from unittest.mock import patch
from tfac import WinFactory
from tfac import MacFactory
from tfac import LinuxFactory


class AbstractFactoryTestCase(TestCase):
    def start(self):
        factory = WinFactory()

    @patch('fact.define_resolution', return_value="2560x1600")
    def test_win_window_hr(self, define_resolution):
        factory = WinFactory()
        window = factory.create_window()
        self.assertEqual("Создание и отрисовка окна с разрешением 2560x1600 в стиле Windows",
                         window.paint(define_resolution("platform")))

    @patch('fact.define_resolution', return_value="1600x1200")
    def test_win_window_mr(self, define_resolution):
        factory = WinFactory()
        window = factory.create_window()
        self.assertEqual("Создание и отрисовка окна с разрешением 1600x1200 в стиле Windows",
                         window.paint(define_resolution("platform")))

    @patch('fact.define_resolution', return_value="1280x1024")
    def test_win_window_lr(self, define_resolution):
        factory = WinFactory()
        window = factory.create_window()
        self.assertEqual("Создание и отрисовка окна с разрешением 1280x1024 в стиле Windows",
                         window.paint(define_resolution("platform")))

    def test_win_button(self):
        factory = WinFactory()
        button = factory.create_button()
        self.assertEqual("Отрисовка кнопки в стиле Windows", button.paint())

    def test_win_checkbox(self):
        factory = WinFactory()
        checkbox = factory.create_checkbox()
        self.assertEqual("Отрисовка чек-бокса в стиле Windows", checkbox.paint())

    def test_win_checkbox_button(self):
        factory = WinFactory()
        button = factory.create_button()
        checkbox = factory.create_checkbox()
        self.assertEqual("Отрисовка чек-бокса и Отрисовка кнопки в стиле Windows", checkbox.paint_with_button(button))

    def test_win_error_textfield_checkbox_button(self):
        factory = WinFactory()
        textfield = factory.create_textfield()
        checkbox = factory.create_checkbox()
        self.assertRaises(ValueError, checkbox.paint_with_button, textfield)

    def test_win_error_checkbox_checkbox_button(self):
        factory = WinFactory()
        checkbox = factory.create_checkbox()
        self.assertRaises(ValueError, checkbox.paint_with_button, checkbox)

    def test_win_textfield(self):
        factory = WinFactory()
        textfield = factory.create_textfield()
        self.assertEqual("Отрисовка текстового поля в стиле Windows", textfield.paint())

    @patch('fact.define_resolution', return_value="2560x1600")
    def test_mac_window_hr(self, define_resolution):
        factory = MacFactory()
        window = factory.create_window()
        self.assertEqual("Создание и отрисовка окна с разрешением 2560x1600 в стиле macOS",
                         window.paint(define_resolution("platform")))

    @patch('fact.define_resolution', return_value="1600x1200")
    def test_mac_window_mr(self, define_resolution):
        factory = MacFactory()
        window = factory.create_window()
        self.assertEqual("Создание и отрисовка окна с разрешением 1600x1200 в стиле macOS",
                         window.paint(define_resolution("platform")))

    @patch('fact.define_resolution', return_value="1280x1024")
    def test_mac_window_lr(self, define_resolution):
        factory = MacFactory()
        window = factory.create_window()
        self.assertEqual("Создание и отрисовка окна с разрешением 1280x1024 в стиле macOS",
                         window.paint(define_resolution("platform")))

    def test_mac_button(self):
        factory = MacFactory()
        button = factory.create_button()
        self.assertEqual("Отрисовка кнопки в стиле macOS", button.paint())

    def test_mac_checkbox(self):
        factory = MacFactory()
        checkbox = factory.create_checkbox()
        self.assertEqual("Отрисовка чек-бокса в стиле macOS", checkbox.paint())

    def test_mac_checkbox_button(self):
        factory = MacFactory()
        button = factory.create_button()
        checkbox = factory.create_checkbox()
        self.assertEqual("Отрисовка чек-бокса и Отрисовка кнопки в стиле macOS", checkbox.paint_with_button(button))

    def test_mac_error_textfield_checkbox_button(self):
        factory = MacFactory()
        textfield = factory.create_textfield()
        checkbox = factory.create_checkbox()
        self.assertRaises(ValueError, checkbox.paint_with_button, textfield)

    def test_mac_error_checkbox_checkbox_button(self):
        factory = MacFactory()
        checkbox = factory.create_checkbox()
        self.assertRaises(ValueError, checkbox.paint_with_button, checkbox)

    def test_mac_textfield(self):
        factory = MacFactory()
        textfield = factory.create_textfield()
        self.assertEqual("Отрисовка текстового поля в стиле macOS", textfield.paint())

    @patch('fact.define_resolution', return_value="2560x1600")
    def test_linux_window_hr(self, define_resolution):
        factory = LinuxFactory()
        window = factory.create_window()
        self.assertEqual("Создание и отрисовка окна с разрешением 2560x1600 в стиле Linux",
                         window.paint(define_resolution("platform")))

    @patch('fact.define_resolution', return_value="1600x1200")
    def test_linux_window_mr(self, define_resolution):
        factory = LinuxFactory()
        window = factory.create_window()
        self.assertEqual("Создание и отрисовка окна с разрешением 1600x1200 в стиле Linux",
                         window.paint(define_resolution("platform")))

    @patch('fact.define_resolution', return_value="1280x1024")
    def test_linux_window_lr(self, define_resolution):
        factory = LinuxFactory()
        window = factory.create_window()
        self.assertEqual("Создание и отрисовка окна с разрешением 1280x1024 в стиле Linux",
                         window.paint(define_resolution("platform")))

    def test_linux_button(self):
        factory = LinuxFactory()
        button = factory.create_button()
        self.assertEqual("Отрисовка кнопки в стиле Linux", button.paint())

    def test_linux_checkbox(self):
        factory = LinuxFactory()
        checkbox = factory.create_checkbox()
        self.assertEqual("Отрисовка чек-бокса в стиле Linux", checkbox.paint())

    def test_linux_checkbox_button(self):
        factory = LinuxFactory()
        button = factory.create_button()
        checkbox = factory.create_checkbox()
        self.assertEqual("Отрисовка чек-бокса и Отрисовка кнопки в стиле Linux", checkbox.paint_with_button(button))

    def test_linux_error_textfield_checkbox_button(self):
        factory = LinuxFactory()
        textfield = factory.create_textfield()
        checkbox = factory.create_checkbox()
        self.assertRaises(ValueError, checkbox.paint_with_button, textfield)

    def test_linux_error_checkbox_checkbox_button(self):
        factory = LinuxFactory()
        checkbox = factory.create_checkbox()
        self.assertRaises(ValueError, checkbox.paint_with_button, checkbox)

    def test_linux_textfield(self):
        factory = LinuxFactory()
        textfield = factory.create_textfield()
        self.assertEqual("Отрисовка текстового поля в стиле Linux", textfield.paint())


if __name__ == '__main__':
    unittest.main()