import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ProgressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # Inicia el proceso al conectarse
        await self.send_progress()

    async def disconnect(self, close_code):
        print(f"Desconectado: {close_code}")

    async def send_progress(self):
        # Simula un proceso que toma 10 pasos
        for i in range(1, 11):
            await asyncio.sleep(1)  # Simula un trabajo que toma tiempo
            progress = i * 10  # Calcula el porcentaje
            await self.send(text_data=json.dumps({
                "progress": progress,
                "message": f"Progreso: {progress}%",
            }))
        await self.send(text_data=json.dumps({
            "progress": 100,
            "message": "¡Proceso completado!",
        }))
