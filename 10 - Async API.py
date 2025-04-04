# pip install aiohttp

import flet as ft
import aiohttp
import asyncio

async def main(page: ft.Page):
    result_text = ft.Text("Click the button to download data.", size=16)
    counter = 0
    counter_text = ft.Text(f"Counter: {counter}", size=16)

    async def download_data():
        try:
            # Simulate network delay
            result_text.value = "Simulating network delay..."
            page.update()
            await asyncio.sleep(5)  # 5 second delay
            
            async with aiohttp.ClientSession() as session:
                async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
                    if response.status == 200:
                        data = await response.json()
                        new_value = f"Downloaded Data: {data}"
                    else:
                        new_value = f"Failed to download data. Status: {response.status}"
        except Exception as ex:
            new_value = f"Error: {ex}"
        result_text.value = new_value
        page.update()
    
    async def start_download(e):
        result_text.value = "Starting download..."
        page.update()
        # Start the async task
        await download_data()

    def increment_counter(e):
        nonlocal counter
        counter += 1
        counter_text.value = f"Counter: {counter}"
        page.update()

    download_button = ft.ElevatedButton("Download API Data", on_click=start_download)
    counter_button = ft.ElevatedButton("Increment Counter", on_click=increment_counter)
    
    page.add(
        ft.Column([
            download_button,
            result_text,
            counter_button,
            counter_text
        ])
    )

ft.app(target=main)
