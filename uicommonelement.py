from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('La extraño:(', on_click=lambda: ui.notify('Yo tambien'))
with ui.row():
    ui.checkbox('Aceptas TyCs?', on_change=show)
    ui.switch('On/Off', on_change=show)
ui.radio(['Hombre', 'Mujer', 'Furro'], value='Hombre', on_change=show).props('inline')
with ui.row():
    ui.input('Redacta', on_change=show)
    ui.select(['One', 'Two'], value='One', on_change=show)
ui.link('Luna a 5km de distancia', 'https:/github.com/tavochiquit0hub').classes('mt-8')

ui.run()