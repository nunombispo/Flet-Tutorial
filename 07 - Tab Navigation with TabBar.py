import flet as ft

def main(page: ft.Page):
    # Set page properties
    page.title = "Tab Navigation Demo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    def tab_changed(e):
        print(f"Selected tab: {e.control.selected_index}")
        page.update()

    # Create tabs with icons and better styling
    tab1 = ft.Tab(
        text="Home",
        icon=ft.icons.HOME,
        content=ft.Container(
            content=ft.Text("Welcome to the Home tab!", size=20),
            alignment=ft.alignment.center,
            padding=20
        )
    )
    
    tab2 = ft.Tab(
        text="Profile",
        icon=ft.icons.PERSON,
        content=ft.Container(
            content=ft.Text("This is your profile.", size=20),
            alignment=ft.alignment.center,
            padding=20
        )
    )
    
    tab3 = ft.Tab(
        text="Settings",
        icon=ft.icons.SETTINGS,
        content=ft.Container(
            content=ft.Text("Adjust your settings here.", size=20),
            alignment=ft.alignment.center,
            padding=20
        )
    )

    # Create tab bar with styling
    tab_bar = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        expand=True,
        tabs=[tab1, tab2, tab3],
        on_change=tab_changed
    )

    # Add tab bar to page
    page.add(tab_bar)

ft.app(target=main)
