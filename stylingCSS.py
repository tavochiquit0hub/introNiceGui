from nicegui import ui

ui.icon('thumb_up', color='red').classes('text-25xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('The Glorious').style('color: #006680; font-weight: bold; font-family: "Arial", sans-serif; font-size: 20px')
    ui.label('Final').classes('font-serif')
    ui.label('Evolution').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()