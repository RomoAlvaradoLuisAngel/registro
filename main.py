import flet as ft

def main(page: ft.Page):
    page.theme_mode=ft.ThemeMode.LIGHT
    page.title = "Ejercicio de prueba ñejeje"
    
    page.add(ft.Text(value="¡Bienvenido a tu aplicacion de registro de eventos!"))
    page.add(ft.Text(value="¡Una aplicacion dedicada a que tengas un control y manejo de tus horarios de eventos!"))
    
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
    
    
    txt_valor = ft.Text(value = "1Hr", size = 25)
    
    page.add(ft.Text("Duracion de el evento"))
    duracion = ft.Slider(
        min=1,
        max=8,
        value=1
    )
    page.add(duracion, txt_valor)
    
    resumen = ft.Text(value="")
    page.add(resumen)
    page.add(ft.Text("Resumen de el evento!"))
    def mostrar_resumen(e):
        resumen.value = "Evento: " + nombre.value + "\n"
        resumen.value += "Tipo: " + tipo.value + "\n"
        resumen.value += "Modalidad: " + radio_group.value + "\n"
        resumen.value += "Duracion: " + str(int(duracion.value)) + "\n"
        page.update()
    
    page.add(ft.ElevatedButton(
        content=ft.Text("Mostrar resumen"),
        on_click=mostrar_resumen
    ))
    
    page.add(ft.Divider(height=10, thickness=2, color=ft.Colors.GREY_400))
    page.add(ft.Row([
        ft.VerticalDivider(width=10, thickness=2, color=ft.Colors.GREY_400)
    ]))
    
ft.run(main)