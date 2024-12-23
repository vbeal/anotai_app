import flet as ft
from typing import Dict
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

saved_notes = [
    {
        'id': 1,
        'title': 'Lista de Compras',
        'date': datetime.date(2024, 1, 10),
        'content': 'Comprar itens essenciais para a semana: pão, leite, ovo',
        'color': 'blue',
        'expanded': True,
    },
    {
        'id': 2,
        'title': 'Reunião de Trabalho',
        'date': datetime.date(2024, 1, 15),
        'content': 'Reunião de trabalho para a semana: pão, leite, ovo',
        'color': 'red', 
        'expanded': True,
    },
    {
        'id': 3,
        'title': 'Reunião de Trabalho',
        'date': datetime.date(2024, 1, 15),
        'content': 'Reunião de trabalho para a semana: pão, leite, ovo',
        'color': 'red', 
        'expanded': False,
    },
    {
        'id': 4,
        'title': 'Idéias de Projeto',
        'date': datetime.date(2024, 1, 15),
        'content': '1. Pesquisar tendências de design.\n2. Esboçar layouts novos.\n3. Identificar oportunidades de mercado.',
        'color': 'white', 
        'expanded': False,
    },
    {
        'id': 5,
        'title': 'Reunião de Trabalho',
        'date': datetime.date(2024, 1, 15),
        'content': 'Reunião de trabalho para a semana: pão, leite, ovo',
        'color': 'red', 
        'expanded': True,
    },
    {
        'id': 6,
        'title': 'Idéias de Projeto',
        'date': datetime.date(2024, 1, 15),
        'content': '1. Pesquisar tendências de design.\n2. Esboçar layouts novos.\n3. Identificar oportunidades de mercado.',
        'color': 'red', 
        'expanded': True,
    }
]

def main(page: ft.Page):

    # aplicar sombra
    def apply_shadow(e):
        if e.control.shadow:
            e.control.shadow = None
        else:
            e.control.shadow = ft.BoxShadow(
                blur_radius=20,
                color=e.control.bgcolor,
                blur_style=ft.ShadowBlurStyle.OUTER,
            )
        e.control.update()

    def open_note(e):
        page.controls.pop()

        for sn in saved_notes:
            if sn['id'] == e.control.data:
                page.add(note_details(note=sn))
                return
            
        page.add(note_details())

    # notas
    def notes():
        return ft.ResponsiveRow(
            columns=2,
            controls=[
                ft.Container(
                    col=2 if sn['expanded'] else 1,
                    bgcolor=sn['color'],
                    padding=ft.padding.all(20),
                    border_radius=ft.border_radius.all(20),
                    shadow=None,
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value=sn['title'], 
                                style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                max_lines=3,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            ft.Text(
                                value=sn['date'].strftime('%b. %d, %Y'), 
                                style=ft.TextThemeStyle.BODY_MEDIUM
                            ),
                        ]
                    ),
                    on_hover=apply_shadow,
                    data=sn['id'],
                    on_click=open_note,
                ) for sn in saved_notes
            ]
        )

    layout = ft.Container(
        expand=True,
        padding=ft.padding.all(20),
        content=ft.Column(
            controls=[
                ft.Text(value='AnotAI', style=ft.TextThemeStyle.DISPLAY_LARGE),
                ft.Column(
                    expand=True,
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[notes()]
                ),
            ]
        )
    )

    # Botão para adicionar uma nova nota
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        shape=ft.CircleBorder(),
        tooltip='Adicionar Nota',
        bgcolor=ft.colors.INDIGO,
        on_click=open_note,
    )

    page.add(layout)

    # voltar para a home
    def go_to_home(e):
        page.controls.pop()
        layout.content.controls[-1] = notes()
        page.add(layout)

    # detalhes da nota
    def note_details(note: Dict[str, str] = dict()):

        if note.get('date'):
            date = note.get('date').strftime('%b. %d, %Y')
        else:
            date = datetime.date.today().strftime('%b. %d, %Y')
    
        def change_note(e):
            if e.control.data is not None:
                for sn in saved_notes:
                    if sn['id'] == e.control.data:
                        sn['title'] = title.value
                        sn['content'] = content.value
                        sn['date'] = datetime.datetime.today()
            else:
                saved_notes.append({
                    'id': len(saved_notes) + 1,
                    'title': title.value,
                    'content': content.value,
                    'date': datetime.datetime.today(),
                    'color': 'white',
                    'expanded': True,
                })

            page.controls.pop()
            layout.content.controls[-1] = notes()
            page.add(layout)

        def enable_save_button(e):
            save_button.disabled = False
            save_button.update()
        
        return ft.Container(
            expand=True,
            padding=ft.padding.all(20),
            content=ft.Column(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        tooltip='Voltar',
                        on_click=go_to_home
                    ),
                    title := ft.TextField(
                        value=note.get('title'),
                        max_length=50,
                        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD),
                        border=ft.InputBorder.UNDERLINE,
                        hint_text='Digite o título da nota',
                        hint_style=ft.TextStyle(italic=True),
                        content_padding=ft.padding.only(bottom=20),
                        on_change=enable_save_button
                    ),
                    ft.Text(value=date),
                    content := ft.TextField(
                        value=note.get('content'),
                        text_style=ft.TextStyle(size=20),
                        border=ft.InputBorder.NONE,
                        multiline=True,
                        min_lines=5,
                        hint_text='Digite sua anotação aqui...',
                        hint_style=ft.TextStyle(italic=True),
                        content_padding=ft.padding.only(top=20),
                        on_change=enable_save_button
                    ),
                    save_button := ft.ElevatedButton(
                        text='Salvar Alterações',
                        bgcolor=ft.colors.INDIGO,
                        color=ft.colors.WHITE,
                        disabled=True,
                        data=note.get('id'),
                        on_click=change_note,
                    )
                ]
            )
        )

if __name__ == '__main__':
    ft.app(target=main)
