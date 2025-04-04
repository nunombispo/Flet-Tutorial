import flet as ft

def main(page: ft.Page):
    # Configure the page
    page.title = "Flet Layout Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 50

    # Create controls
    header = ft.Text(
        value="Welcome to Flet",
        size=24,
        weight=ft.FontWeight.BOLD
    )
    
    subheader = ft.Text(
        value="Building layouts is easy!",
        size=16,
        color=ft.colors.BLUE_GREY_500
    )

    # Create a row of buttons
    row_buttons = ft.Row(
        controls=[
            ft.ElevatedButton(
                text="Left Button",
                icon=ft.icons.ARROW_BACK
            ),
            ft.ElevatedButton(
                text="Right Button",
                icon=ft.icons.ARROW_FORWARD
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Create the main column layout
    layout = ft.Column(
        controls=[header, subheader, row_buttons],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    # Add the layout to the page
    page.add(layout)

ft.app(target=main)
