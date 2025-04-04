import flet as ft

def main(page: ft.Page):
    # Configure page
    page.title = "Form Validation Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 50

    # Form fields with validation
    name_field = ft.TextField(
        label="Name",
        width=300,
        hint_text="Enter your name",
        prefix_icon=ft.icons.PERSON,
        autofocus=True,
        on_change=lambda e: validate_form()
    )
    
    email_field = ft.TextField(
        label="Email",
        width=300,
        hint_text="Enter your email",
        prefix_icon=ft.icons.EMAIL,
        on_change=lambda e: validate_form()
    )

    # Error message container
    error_text = ft.Text(color=ft.colors.RED, visible=False)
    
    # Success message container
    success_text = ft.Text(color=ft.colors.GREEN, visible=False)

    def validate_form():
        # Reset messages
        error_text.visible = False
        success_text.visible = False
        
        # Validate name
        if not name_field.value:
            name_field.error_text = "Name is required"
        else:
            name_field.error_text = None
        
        # Validate email
        if not email_field.value:
            email_field.error_text = "Email is required"
        elif "@" not in email_field.value:
            email_field.error_text = "Please enter a valid email"
        else:
            email_field.error_text = None
        
        page.update()

    def submit(e):
        validate_form()
        
        if not name_field.value or not email_field.value or name_field.error_text or email_field.error_text:
            error_text.value = "Please correct the errors above"
            error_text.visible = True
            success_text.visible = False
        else:
            error_text.visible = False
            success_text.value = f"Hello {name_field.value}, your email is {email_field.value}"
            success_text.visible = True
            
            # Clear form
            name_field.value = ""
            email_field.value = ""
        
        page.update()

    submit_button = ft.ElevatedButton(
        "Submit",
        on_click=submit,
        icon=ft.icons.SEND,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE,
        )
    )

    form = ft.Column(
        [
            ft.Text("Please fill out the form", size=20, weight=ft.FontWeight.BOLD),
            name_field,
            email_field,
            submit_button,
            error_text,
            success_text
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(form)

ft.app(target=main)
