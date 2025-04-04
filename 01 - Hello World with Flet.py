import flet as ft

def main(page: ft.Page):
    # Configure the page
    page.title = "Hello Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Create and add the text widget
    hello_text = ft.Text(
        value="Hello, Flet!",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE
    )
    page.add(hello_text)

ft.app(target=main)
