# Agente 3: Monitoreo del Computador con Telegram

## Descripción
Agente que monitorea el estado del computador en tiempo real y envía alertas a Telegram cuando hay problemas de rendimiento, espacio en disco, o amenazas de seguridad.

## Arquitectura

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Telegram Bot   │◀────│   OpenCode      │◀────│   Monitor       │
│   (Alertas)      │     │   Agent         │     │   (psutil)      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                              │                         │
                              ▼                         ▼
                        ┌─────────────────┐     ┌─────────────────┐
                        │   Análisis IA   │     │   Sistema       │
                        │   (Patrones)    │     │   (CPU,RAM,etc) │
                        └─────────────────┘     └─────────────────┘
```

## Funcionalidades

### 1. Alertas de Rendimiento
```
🤖 ALERTA DE RENDIMIENTO

⚠️ Uso de CPU elevado: 92%
📊 Top 3 procesos:
   1. chrome.exe - 45%
   2. code.exe - 23%
   3. node.exe - 15%

🕐 Detectado hace: 5 minutos
💡 Recomendación: Cerrar pestañas de Chrome

[Ver detalles] [Cerrar procesos]
```

### 2. Alerta de Espacio en Disco
```
🤖 ALERTA DE ALMACENAMIENTO

🔴 Disco C: - 15% disponible (12.5 GB libre)
🟡 Disco D: - 45% disponible (180 GB libre)

📁 Top 5 carpetas más pesadas:
   1. C:\Users\user\Downloads - 25 GB
   2. C:\Users\user\AppData - 18 GB
   3. C:\Program Files - 12 GB

💡 Recomendación: Limpiar carpeta de Descargas

[Limpiar ahora] [Ver detalles]
```

### 3. Alerta de Seguridad
```
🤖 ALERTA DE SEGURIDAD

🔴 Intento de acceso sospechoso detectado
📍 IP: 192.168.1.105
⏰ Hora: 14:32:15
🎯 Servicio: SSH (Puerto 22)

📊 Análisis:
- 5 intentos fallidos en 2 minutos
- Origen: Red local

¿Tomar acción?
[ Bloquear IP ] [ Ver logs ] [ Ignorar ]
```

### 4. Reporte Diario
```
🤖 REPORTE DIARIO - 5 Agosto 2026

💻 SISTEMA
├─ CPU: Promedio 45%, Máximo 89%
├─ RAM: Promedio 6.2 GB / 16 GB
├─ Disco: 85% usado
└─ Temperatura: 65°C máxima

🌐 RED
├─ Subida: 2.5 GB
├─ Bajada: 15.3 GB
└─ Latencia promedio: 12ms

🔒 SEGURIDAD
├─ 3 intentos de acceso bloqueados
├─ 0 virus detectados
└─ Firewall: Activo

⚡ RENDIMIENTO
├─ Tiempo de arranque: 45 segundos
├─ Aplicaciones abiertas: 12
└─ Procesos activos: 156
```

### 5. Comandos Interactivos
```
Usuario: /status

🤖 Estado del Sistema

CPU: ████████░░ 78%
RAM: ██████░░░░ 62%
DISCO: █████████░ 85%
RED: ████░░░░░░ 45%

Uptime: 3 días, 5 horas
Procesos: 156
Conexiones: 23
```

## Código del Agente

### monitor_agent.py
```python
import psutil
import platform
from datetime import datetime
import asyncio
from opencode import OpenCodeClient

class SystemMonitor:
    def __init__(self):
        self.client = OpenCodeClient()
        self.alert_thresholds = {
            'cpu': 85,
            'memory': 80,
            'disk': 90,
            'temperature': 75
        }
    
    def get_cpu_info(self) -> dict:
        """Obtener información de CPU."""
        return {
            'percent': psutil.cpu_percent(interval=1),
            'count': psutil.cpu_count(),
            'freq': psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
            'per_cpu': psutil.cpu_percent(percpu=True)
        }
    
    def get_memory_info(self) -> dict:
        """Obtener información de memoria."""
        mem = psutil.virtual_memory()
        return {
            'total': mem.total,
            'available': mem.available,
            'percent': mem.percent,
            'used': mem.used,
            'free': mem.free
        }
    
    def get_disk_info(self) -> list:
        """Obtener información de discos."""
        disks = []
        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                disks.append({
                    'device': part.device,
                    'mountpoint': part.mountpoint,
                    'total': usage.total,
                    'used': usage.used,
                    'free': usage.free,
                    'percent': usage.percent
                })
            except:
                continue
        return disks
    
    def get_network_info(self) -> dict:
        """Obtener información de red."""
        net = psutil.net_io_counters()
        return {
            'bytes_sent': net.bytes_sent,
            'bytes_recv': net.bytes_recv,
            'packets_sent': net.packets_sent,
            'packets_recv': net.packets_recv
        }
    
    def get_top_processes(self, n: int = 5) -> list:
        """Obtener procesos que más consumen."""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append(proc.info)
            except:
                continue
        
        # Ordenar por CPU
        processes.sort(key=lambda x: x.get('cpu_percent', 0), reverse=True)
        return processes[:n]
    
    def get_temperature(self) -> dict:
        """Obtener temperatura del sistema."""
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                return {
                    sensor: max([temp.current for temp in temps_list])
                    for sensor, temps_list in temps.items()
                }
        except:
            return {'cpu': 65}  # Valor por defecto
    
    async def analyze_with_ai(self, metrics: dict) -> str:
        """Analizar métricas con IA para detectar anomalías."""
        prompt = f"""
        Analiza estas métricas del sistema y determina si hay problemas:
        
        CPU: {metrics['cpu']['percent']}%
        Memoria: {metrics['memory']['percent']}%
        Disco: {metrics['disk'][0]['percent'] if metrics['disk'] else 'N/A'}%
        
        Responde con:
        1. Estado general (OK/ALERTA/CRÍTICO)
        2. Problemas detectados
        3. Recomendaciones
        """
        
        return await self.client.chat(prompt)
    
    def check_alerts(self) -> list:
        """Verificar si hay alertas que enviar."""
        alerts = []
        
        cpu = self.get_cpu_info()
        if cpu['percent'] > self.alert_thresholds['cpu']:
            alerts.append({
                'type': 'cpu',
                'level': 'warning',
                'message': f"CPU al {cpu['percent']}%",
                'details': self.get_top_processes()
            })
        
        memory = self.get_memory_info()
        if memory['percent'] > self.alert_thresholds['memory']:
            alerts.append({
                'type': 'memory',
                'level': 'warning',
                'message': f"Memoria al {memory['percent']}%"
            })
        
        disks = self.get_disk_info()
        for disk in disks:
            if disk['percent'] > self.alert_thresholds['disk']:
                alerts.append({
                    'type': 'disk',
                    'level': 'critical',
                    'message': f"Disco {disk['device']} al {disk['percent']}%"
                })
        
        return alerts
    
    def generate_report(self) -> dict:
        """Generar reporte completo del sistema."""
        return {
            'timestamp': datetime.now().isoformat(),
            'system': {
                'platform': platform.system(),
                'version': platform.version(),
                'machine': platform.machine()
            },
            'cpu': self.get_cpu_info(),
            'memory': self.get_memory_info(),
            'disk': self.get_disk_info(),
            'network': self.get_network_info(),
            'temperature': self.get_temperature(),
            'top_processes': self.get_top_processes()
        }
```

### telegram_monitor.py
```python
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from monitor_agent import SystemMonitor
import asyncio

class TelegramMonitor:
    def __init__(self, token: str):
        self.app = Application.builder().token(token).build()
        self.monitor = SystemMonitor()
        
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("status", self.status))
        self.app.add_handler(CommandHandler("report", self.report))
        self.app.add_handler(CommandHandler("alerts", self.check_alerts))
        self.app.add_handler(CommandHandler("processes", self.processes))
        self.app.add_handler(CallbackQueryHandler(self.handle_callback))
    
    async def start(self, update: Update, context):
        await update.message.reply_text(
            "🤖 Monitor de Sistema\n\n"
            "Comandos:\n"
            "/status - Estado actual\n"
            "/report - Reporte completo\n"
            "/alerts - Ver alertas\n"
            "/processes - Top procesos"
        )
    
    async def status(self, update: Update, context):
        """Mostrar estado actual del sistema."""
        report = self.monitor.generate_report()
        
        cpu_bar = self._create_bar(report['cpu']['percent'])
        mem_bar = self._create_bar(report['memory']['percent'])
        disk_bar = self._create_bar(report['disk'][0]['percent'] if report['disk'] else 0)
        
        text = f"""
💻 *Estado del Sistema*

CPU: {cpu_bar} {report['cpu']['percent']}%
RAM: {mem_bar} {report['memory']['percent']}%
DISCO: {disk_bar} {report['disk'][0]['percent'] if report['disk'] else 0}%

🔥 Temperatura: {report['temperature'].get('coretemp', 'N/A')}°C
⏱️ Uptime: {self._get_uptime()}
"""
        
        keyboard = [
            [InlineKeyboardButton("🔄 Actualizar", callback_data='refresh_status')],
            [InlineKeyboardButton("📊 Ver procesos", callback_data='show_processes')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')
    
    async def report(self, update: Update, context):
        """Generar reporte completo."""
        report = self.monitor.generate_report()
        
        text = f"""
📊 *REPORTE COMPLETO*
📅 {report['timestamp']}

*💻 Sistema*
Plataforma: {report['system']['platform']}
Versión: {report['system']['version']}

*🔧 CPU*
Uso: {report['cpu']['percent']}%
Núcleos: {report['cpu']['count']}

*🧠 Memoria*
Total: {self._format_bytes(report['memory']['total'])}
Usada: {self._format_bytes(report['memory']['used'])}
Libre: {self._format_bytes(report['memory']['free'])}

*💾 Disco*
"""
        
        for disk in report['disk']:
            text += f"{disk['device']}: {self._format_bytes(disk['used'])}/{self._format_bytes(disk['total'])}\n"
        
        await update.message.reply_text(text, parse_mode='Markdown')
    
    async def check_alerts(self, update: Update, context):
        """Verificar alertas."""
        alerts = self.monitor.check_alerts()
        
        if not alerts:
            await update.message.reply_text("✅ No hay alertas activas")
            return
        
        text = "⚠️ *Alertas Activas*\n\n"
        
        for alert in alerts:
            emoji = "🟡" if alert['level'] == 'warning' else "🔴"
            text += f"{emoji} {alert['type'].upper()}: {alert['message']}\n"
        
        await update.message.reply_text(text, parse_mode='Markdown')
    
    async def handle_callback(self, update: Update, context):
        query = update.callback_query
        await query.answer()
        
        if query.data == 'refresh_status':
            # Reenviar estado actualizado
            report = self.monitor.generate_report()
            await query.edit_message_text(f"CPU: {report['cpu']['percent']}%")
    
    def _create_bar(self, percent: int) -> str:
        filled = int(percent / 10)
        empty = 10 - filled
        return '█' * filled + '░' * empty
    
    def _format_bytes(self, bytes: int) -> str:
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes < 1024:
                return f"{bytes:.1f} {unit}"
            bytes /= 1024
    
    def _get_uptime(self) -> str:
        import psutil
        boot = datetime.fromtimestamp(psutil.boot_time())
        delta = datetime.now() - boot
        days = delta.days
        hours = delta.seconds // 3600
        return f"{days} días, {hours} horas"
    
    def run(self):
        self.app.run_polling()
```

### alert_scheduler.py
```python
import asyncio
from datetime import datetime
from monitor_agent import SystemMonitor
from telegram_monitor import TelegramMonitor

class AlertScheduler:
    def __init__(self, telegram_token: str, chat_id: int):
        self.monitor = SystemMonitor()
        self.telegram = TelegramMonitor(telegram_token)
        self.chat_id = chat_id
        self.running = False
    
    async def start(self):
        """Iniciar scheduler de alertas."""
        self.running = True
        while self.running:
            # Verificar alertas cada 5 minutos
            alerts = self.monitor.check_alerts()
            
            for alert in alerts:
                await self.send_alert(alert)
            
            await asyncio.sleep(300)  # 5 minutos
    
    async def send_alert(self, alert: dict):
        """Enviar alerta a Telegram."""
        emoji = "🟡" if alert['level'] == 'warning' else "🔴"
        
        text = f"""
{emoji} *ALERTA DE SISTEMA*

Tipo: {alert['type'].upper()}
Mensaje: {alert['message']}
Hora: {datetime.now().strftime('%H:%M:%S')}
"""
        
        await self.telegram.app.bot.send_message(
            chat_id=self.chat_id,
            text=text,
            parse_mode='Markdown'
        )
    
    async def stop(self):
        self.running = False
```

## Configuración

### config_monitor.py
```python
import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Umbrales de alerta
THRESHOLDS = {
    'cpu_warning': 80,
    'cpu_critical': 95,
    'memory_warning': 75,
    'memory_critical': 90,
    'disk_warning': 85,
    'disk_critical': 95,
    'temperature_warning': 70,
    'temperature_critical': 85
}

# Intervalos de monitoreo
CHECK_INTERVAL = 300  # 5 minutos
REPORT_HOUR = 8  # 8 AM para reporte diario
```

## Despliegue

### Docker
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

### Systemd Service
```ini
[Unit]
Description=Computer Monitor Telegram Bot
After=network.target

[Service]
Type=simple
User=monitor
WorkingDirectory=/opt/monitor
ExecStart=/usr/bin/python3 main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

## Beneficios

| Beneficio | Impacto |
|-----------|---------|
| Detección temprana | Prevenir problemas antes de que afecten |
| Monitoreo 24/7 | Alertas en tiempo real |
| Análisis inteligente | IA detecta patrones anómalos |
| Acceso remoto | Verificar estado desde cualquier lugar |
| Historial | Tendencias y análisis de largo plazo |
