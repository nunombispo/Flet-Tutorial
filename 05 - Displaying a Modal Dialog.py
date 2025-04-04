import flet as ft

def main(page: ft.Page):
    def show_dialog(e):
        dlg = ft.AlertDialog(
            title=ft.Text("Hello Dialog!"),
            content=ft.Text("This is a modal dialog in Flet."),
            actions=[
                ft.TextButton("Close", on_click=lambda e: page.close(dlg))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            modal=True
        )
        page.open(dlg)

    open_dialog_btn = ft.ElevatedButton("Open Dialog", on_click=show_dialog)
    page.add(open_dialog_btn)

ft.app(target=main)
