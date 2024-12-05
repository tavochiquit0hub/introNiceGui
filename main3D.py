#!/usr/bin/env python3
from nicegui import app, ui

app.add_static_files('/stl', 'static')

with ui.scene(width=1024, height=900) as scene:
    # Añadir varias luces puntuales para mejorar la iluminación
    scene.spot_light(distance=100, intensity=1).move(-10, 0, 10)  # Luz principal
    scene.spot_light(distance=100, intensity=0.7).move(10, 10, 10)  # Luz adicional
    scene.spot_light(distance=100, intensity=0.5).move(0, -10, 5)  # Luz desde abajo

    # Cargar el modelo y aplicar color y opacidad
    scene.stl('/stl/utochka.stl').move(x=1, z=1).scale(0.06).material(color='#f74408', opacity=1)

ui.run()
