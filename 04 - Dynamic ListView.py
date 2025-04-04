import flet as ft

def main(page: ft.Page):
    page.title = "Dynamic ListView Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    # Create controls
    list_view = ft.ListView(expand=True, spacing=10, padding=20)
    counter = 0

    def add_item(e):
        nonlocal counter
        counter += 1
        
        def remove_item(e):
            list_view.controls.remove(item_container)
            page.update()

        item_container = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(f"Item {counter}", expand=True),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color=ft.colors.RED,
                        on_click=remove_item,
                        tooltip="Delete item",
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=ft.colors.BLUE_100,
            padding=10,
            border_radius=5,
        )
        
        list_view.controls.append(item_container)
        page.update()

    # Create button
    add_button = ft.FilledButton(
        "Add Item",
        on_click=add_item,
        icon=ft.icons.ADD,
    )

    # Add controls to page
    page.add(
        ft.Column(
            controls=[
                add_button,
                list_view,
            ],
            expand=True,
        )
    )

ft.app(target=main)
