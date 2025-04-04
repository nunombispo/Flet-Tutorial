import flet as ft

class ButtonClickApp:
    def __init__(self):
        self.message = ft.Text("Press the button")
        self.click_button = ft.ElevatedButton(
            text="Click me",
            on_click=self.button_clicked
        )

    def button_clicked(self, e: ft.ControlEvent) -> None:
        self.message.value = "Button clicked!"
        self.message.update()

    def build(self) -> ft.Column:
        return ft.Column(
            controls=[
                self.message,
                self.click_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )

def main(page: ft.Page) -> None:
    page.title = "Button Click Event"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    app = ButtonClickApp()
    page.add(app.build())

ft.app(target=main)
