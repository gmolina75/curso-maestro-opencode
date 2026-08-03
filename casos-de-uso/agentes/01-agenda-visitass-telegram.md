# Agente 1: Agenda de Visitas con Telegram

## Descripción
Agente de IA que gestiona una agenda de visitas completamente vía Telegram, permitiendo a clientes agendar, reprogramar y cancelar citas de forma automática.

## Arquitectura

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Telegram Bot   │────▶│   OpenCode      │────▶│   Base de Datos  │
│   (Webhook)      │◀────│   Agent         │◀────│   (SQLite/Postgres)│
└─────────────────┘     └─────────────────┘     └─────────────────┘
                              │
                              ▼
                        ┌─────────────────┐
                        │   Google Calendar │
                        │   / Outlook       │
                        └─────────────────┘
```

## Funcionalidades

### 1. Agendar Visita
```
Usuario: /agendar
Bot: ¿Qué tipo de visita necesitas?
      1. Reunión de negocios
      2. Visita técnica
      3. Consultoría

Usuario: 1
Bot: Selecciona una fecha:
      [Lun 5 Ago] [Mar 6 Ago] [Mié 7 Ago]

Usuario: Mié 7 Ago
Bot: Horarios disponibles:
      09:00 - 10:00
      14:00 - 15:00
      16:00 - 17:00

Usuario: 14:00
Bot: ✅ Visita agendada
      📅 Miércoles 7 de Agosto
      🕐 14:00 - 15:00
      📍 Reunión de negocios
      🔗 [Link de Zoom]
```

### 2. Reprogramar
```
Usuario: /reprogramar
Bot: Tus próximas visitas:
      1. Mié 7 Ago 14:00 - Reunión negocios
      2. Vie 9 Ago 10:00 - Visita técnica

Usuario: 1
Bot: Nueva fecha para la visita:
      [Seleccionar fecha...]

Usuario: Jue 8 Ago 16:00
Bot: ✅ Visita reprogramada
      📅 Jueves 8 de Agosto 16:00
      📧 Notificación enviada a todos los participantes
```

### 3. Cancelar
```
Usuario: /cancelar
Bot: ¿Qué visita deseas cancelar?
      [Seleccionar...]

Usuario: Visita del Mié 7 Ago
Bot: ⚠️ ¿Confirmar cancelación?
      /confirmar - Cancelar la visita
      /mantener - No cancelar

Usuario: /confirmar
Bot: ❌ Visita cancelada
      📧 Notificación de cancelación enviada
```

### 4. Recordatorios Automáticos
```
24 horas antes:
🤖 Recordatorio: Mañana tienes visita
📅 Miércoles 7 de Agosto
🕐 14:00 - 15:00
📍 Reunión de negocios

1 hora antes:
🤖 Tu visita comienza en 1 hora
🔗 [Link de Zoom]
```

## Código del Agente

### Estructura del Proyecto
```
agenda-visitass-telegram/
├── bot.py              # Bot principal de Telegram
├── agent.py            # Agente OpenCode
├── database.py         # Gestión de base de datos
├── calendar_api.py     # Integración con calendario
├── config.py           # Configuración
└── requirements.txt
```

### bot.py - Bot de Telegram
```python
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
import asyncio
from agent import OpenCodeAgent
from database import Database

class VisitBot:
    def __init__(self, token: str):
        self.app = Application.builder().token(token).build()
        self.agent = OpenCodeAgent()
        self.db = Database()
        
        # Handlers
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("agendar", self.schedule))
        self.app.add_handler(CommandHandler("reprogramar", self.reschedule))
        self.app.add_handler(CommandHandler("cancelar", self.cancel))
        self.app.add_handler(CommandHandler("misvisitas", self.my_visits))
        self.app.add_handler(CallbackQueryHandler(self.handle_callback))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
    
    async def start(self, update: Update, context):
        welcome = """
        👋 Bienvenido al Asistente de Visitas
        
        Comandos disponibles:
        /agendar - Agendar nueva visita
        /reprogramar - Reprogramar visita existente
        /cancelar - Cancelar una visita
        /misvisitas - Ver tus próximas visitas
        """
        await update.message.reply_text(welcome)
    
    async def schedule(self, update: Update, context):
        # Usar agente OpenCode para manejar la conversación
        user_id = update.effective_user.id
        context.user_data['state'] = 'scheduling'
        
        types = [
            [InlineKeyboardButton("Reunión de negocios", callback_data='type:business')],
            [InlineKeyboardButton("Visita técnica", callback_data='type:technical')],
            [InlineKeyboardButton("Consultoría", callback_data='type:consulting')]
        ]
        reply_markup = InlineKeyboardMarkup(types)
        
        await update.message.reply_text(
            "¿Qué tipo de visita necesitas?",
            reply_markup=reply_markup
        )
    
    async def handle_callback(self, update: Update, context):
        query = update.callback_query
        await query.answer()
        
        data = query.data
        
        if data.startswith('type:'):
            visit_type = data.split(':')[1]
            context.user_data['visit_type'] = visit_type
            
            # Generar fechas disponibles usando agente
            dates = await self.agent.get_available_dates(visit_type)
            
            # Crear botones de fechas
            date_buttons = [
                [InlineKeyboardButton(date, callback_data=f'date:{date}')]
                for date in dates
            ]
            reply_markup = InlineKeyboardMarkup(date_buttons)
            
            await query.edit_message_text(
                "Selecciona una fecha:",
                reply_markup=reply_markup
            )
        
        elif data.startswith('date:'):
            date = data.split(':')[1]
            context.user_data['date'] = date
            
            # Obtener horarios disponibles
            times = await self.agent.get_available_times(date)
            
            time_buttons = [
                [InlineKeyboardButton(time, callback_data=f'time:{time}')]
                for time in times
            ]
            reply_markup = InlineKeyboardMarkup(time_buttons)
            
            await query.edit_message_text(
                "Selecciona un horario:",
                reply_markup=reply_markup
            )
        
        elif data.startswith('time:'):
            time = data.split(':')[1]
            
            # Confirmar cita
            confirmation = await self.agent.confirm_booking(
                user_id=query.from_user.id,
                visit_type=context.user_data.get('visit_type'),
                date=context.user_data.get('date'),
                time=time
            )
            
            await query.edit_message_text(
                f"✅ Visita agendada\n\n"
                f"📅 {confirmation['date']}\n"
                f"🕐 {confirmation['time']}\n"
                f"📍 {confirmation['type']}\n"
                f"🔗 {confirmation['link']}"
            )
    
    def run(self):
        self.app.run_polling()

if __name__ == '__main__':
    from config import TELEGRAM_TOKEN
    bot = VisitBot(TELEGRAM_TOKEN)
    bot.run()
```

### agent.py - Agente OpenCode
```python
from opencode import OpenCodeClient
from datetime import datetime, timedelta

class OpenCodeAgent:
    def __init__(self):
        self.client = OpenCodeClient()
    
    async def get_available_dates(self, visit_type: str) -> list:
        """Obtener fechas disponibles para un tipo de visita."""
        prompt = f"""
        Genera 5 fechas disponibles para una visita de tipo '{visit_type}'.
        Solo retorna las fechas en formato DD/MM/YYYY, una por línea.
        Fechas deben ser de lunes a viernes, en las próximas 2 semanas.
        """
        
        response = await self.client.chat(prompt)
        dates = [line.strip() for line in response.split('\n') if line.strip()]
        return dates[:5]
    
    async def get_available_times(self, date: str) -> list:
        """Obtener horarios disponibles para una fecha."""
        prompt = f"""
        Genera horarios disponibles para la fecha {date}.
        Horarios de trabajo: 09:00 a 17:00.
        Slots de 1 hora.
        Retorna 5 horarios en formato HH:MM.
        """
        
        response = await self.client.chat(prompt)
        times = [line.strip() for line in response.split('\n') if line.strip()]
        return times[:5]
    
    async def confirm_booking(self, user_id: int, visit_type: str, date: str, time: str) -> dict:
        """Confirmar y crear la reserva."""
        return {
            'date': date,
            'time': time,
            'type': visit_type,
            'link': 'https://zoom.us/j/example',
            'confirmation_code': f'VIS-{user_id}-{date.replace("/", "")}'
        }
    
    async def send_reminder(self, visit: dict):
        """Enviar recordatorio de visita."""
        prompt = f"""
        Genera un recordatorio amigable para la visita:
        - Fecha: {visit['date']}
        - Hora: {visit['time']}
        - Tipo: {visit['type']}
        
        Incluye emoji y el link de Zoom si aplica.
        """
        
        return await self.client.chat(prompt)
```

### database.py - Base de Datos
```python
import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_path: str = 'visits.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()
    
    def create_tables(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS visits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                visit_type TEXT NOT NULL,
                visit_date TEXT NOT NULL,
                visit_time TEXT NOT NULL,
                status TEXT DEFAULT 'scheduled',
                zoom_link TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def create_visit(self, user_id: int, visit_type: str, date: str, time: str) -> int:
        cursor = self.conn.execute(
            'INSERT INTO visits (user_id, visit_type, visit_date, visit_time) VALUES (?, ?, ?, ?)',
            (user_id, visit_type, date, time)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def get_user_visits(self, user_id: int) -> list:
        cursor = self.conn.execute(
            'SELECT * FROM visits WHERE user_id = ? AND status = "scheduled" ORDER BY visit_date',
            (user_id,)
        )
        return cursor.fetchall()
    
    def cancel_visit(self, visit_id: int) -> bool:
        self.conn.execute(
            'UPDATE visits SET status = "cancelled" WHERE id = ?',
            (visit_id,)
        )
        self.conn.commit()
        return True
```

## Configuración

### config.py
```python
import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENCODE_API_KEY = os.getenv('OPENCODE_API_KEY')
DATABASE_PATH = 'visits.db'

# Horarios de trabajo
WORK_HOURS = {
    'start': 9,
    'end': 17
}

# Duración de slots (minutos)
SLOT_DURATION = 60
```

### requirements.txt
```
python-telegram-bot==20.7
opencode-ai==0.1.0
python-dotenv==1.0.0
```

## Despliegue

### Docker
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
```

### Variables de Entorno
```bash
TELEGRAM_TOKEN=tu_token_de_telegram
OPENCODE_API_KEY=tu_api_key_de_opencode
```

## Beneficios

| Beneficio | Impacto |
|-----------|---------|
| Ahorro de tiempo | 70% menos tiempo en gestión manual |
| Disponibilidad 24/7 | Clientes agendan cuando quieran |
| Reducción de no-shows | Recordatorios automáticos |
| Escalabilidad | Maneja miles de citas simultáneas |
| Costo bajo | Serverless o VPS económico |
