import flet as ft

def main(page: ft.Page):
    page.theme_mode=ft.ThemeMode.LIGHT
    page.title = "Ejercicio de prueba ñejeje"
    
    page.add(ft.Text(value="¡Bienvenido a tu aplicacion de registro de eventos!", color=ft.Colors.BLUE, size=25))
    page.add(ft.Text(value="Una aplicacion hecha para que puedas tener un control y seguimiento de tus eventos!", color=ft.Colors.PINK_500, size= 15))
    
    #textField
    nombre =ft.TextField(
    label="Nombre",
    hint_text="Ingresa el nombre del evento",
    value="",
    prefix_icon=ft.Icons.PERSON,
    suffix_icon=(ft.Text(".com")),
    password=False,
    can_reveal_password=False,
    multiline=False,
    max_length=50,
    keyboard_type=ft.KeyboardType.TEXT,
    border=ft.InputBorder.OUTLINE,
    border_color=ft.Colors.BLUE,
    focused_border_color=ft.Colors.RED,
    filled=True,
    bgcolor=ft.Colors.GREY_100,
    on_change=lambda e: print(e.control.value),
    on_submit=lambda e: print("Enter presionado")
    )
    page.add(nombre)
    
    def calendario(e):
        date_picker.open = True
        page.update()
    
    fecha_text = ft.Text("Sin fecha seleccionada")
    
    def cambiar_fecha(e):
        fecha_text.value = str(date_picker.value.date())
        page.update()
        
    date_picker = ft.DatePicker(
        on_change = cambiar_fecha
    )
    page.overlay.append(date_picker)
        
    boton_fecha = ft.ElevatedButton("Seleccionar fecha", on_click=calendario)
    page.add(boton_fecha, fecha_text)
    "\n"
    tipo = ft.Dropdown(
        value = "Conferencia",
        label = "Tipo de evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunion")
        ],
    )
    page.add(tipo)
    
    ft.Text("Modalidad del evento")
    radio_group = ft.RadioGroup(
        content = ft.Column([
            ft.Radio(label="Presencial", value="Presencial"),
            ft.Radio(label="Virtual", value="Virtual")
        ]),
        on_change=lambda e: print(e.control.value)
    )
    page.add(radio_group)
    
    page.add(ft.Text("¿Requiere inscripcion previa?"))
    inscripcion = ft.Checkbox(label="Si👍", value= False)
    page.add(inscripcion)
    
    
    page.add(ft.Text("Duracion de el evento en horas:)"))
    duracion = ft.Slider(
        min=0,
        max=8,
        value=1,
        divisions = 8,
        label = "{value}"
    )
    page.add(duracion)
    
    page.add(ft.Divider(height=30, thickness=2, color=ft.Colors.BLUE_400))
    page.add(ft.Row([
        ft.VerticalDivider(width=30, thickness=2, color=ft.Colors.BLUE_400)
    ]))
    
    lista_evento = ft.ListView(expand=True, spacing= 10)
    page.add(lista_evento)
    
    resumen = ft.Text(value="")
    page.add(resumen)
    
    def mostrar_resumen(e):
        if nombre.value == "":
            print("Favor de poner un evento")
            return
        evento = (
            "Evento: " + nombre.value + "\n"
            "Tipo de evento:  " + tipo.value + "\n"
            "Modalidad del evento: " + radio_group.value + "\n"
            "Requiere inscripcion?: " + str(inscripcion.value) + "\n"
            "Duracion del evento⏱: " + str(int(duracion.value)) + "Hr " "\n" 
            "Fecha: " + fecha_text.value 
        )
        lista_evento.controls.append(ft.Text(evento))
        page.update()
    
    page.add(ft.ElevatedButton(
        content=ft.Text("Mostrar resumen"),
        on_click=mostrar_resumen,
        color = ft.Colors.PINK
    ))
    

    
ft.run(main)