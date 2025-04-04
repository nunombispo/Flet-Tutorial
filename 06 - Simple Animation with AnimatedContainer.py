import flet as ft

def main(page: ft.Page):
    # Set page properties
    page.title = "Animated Container Demo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 50

    # Create the container
    container = ft.Container(
        width=100,
        height=100,
        bgcolor=ft.Colors.AMBER_400,
        border_radius=ft.border_radius.all(10),
        animate=ft.Animation(300, "easeInOut")
    )

    def toggle_container(e):
        if container.width == 100:
            container.width = 200
            container.height = 200
            container.bgcolor = ft.Colors.BLUE_400
        else:
            container.width = 100
            container.height = 100
            container.bgcolor = ft.Colors.AMBER_400
        page.update()

    # Add click handler
    container.on_click = toggle_container

    # Add container to page
    page.add(container)

if __name__ == "__main__":
    ft.app(target=main)

