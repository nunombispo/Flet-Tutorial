import flet as ft
import time
import threading

def main(page: ft.Page):
    # Configure page
    page.title = "Counter with Timer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 50
    page.theme_mode = ft.ThemeMode.LIGHT

    count = 0
    counter_text = ft.Text(value=str(count), size=30, weight=ft.FontWeight.BOLD)
    running = True

    def update_counter():
        nonlocal count
        while running:
            try:
                count += 1
                counter_text.value = str(count)
                page.update()
                time.sleep(1)
            except Exception as e:
                print(f"Error updating counter: {e}")

    # Create a container for better layout
    counter_container = ft.Container(
        content=counter_text,
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.BLUE_100,
    )

    # Create a column for centered layout
    main_column = ft.Column(
        controls=[counter_container],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Start the timer in a separate thread
    timer_thread = threading.Thread(target=update_counter, daemon=True)
    timer_thread.start()

    # Add the main column to the page
    page.add(main_column)

    # Cleanup when page is closed
    def on_close(e):
        nonlocal running
        running = False

    page.on_close = on_close

ft.app(target=main)
