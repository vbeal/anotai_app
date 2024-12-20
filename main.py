import flet as ft
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
        'title': 'Reunão de Trabalho',
        'date': datetime.date(2024, 1, 15),
        'content': 'Reuniao de trabalho para a semana: pão, leite, ovo',
        'color': 'red', 
        'expanded': True,
    },
    {
        'id': 3,
        'title': 'Reuniao de Trabalho',
        'date': datetime.date(2024, 1, 15),
        'content': 'Reuniao de trabalho para a semana: pão, leite, ovo',
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
        'title': 'Reuniao de Trabalho',
        'date': datetime.date(2024, 1, 15),
        'content': 'Reuniao de trabalho para a semana: pão, leite, ovo',
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


    #notas
    def notes():
        return ft.ResponsiveRow(
            columns=2,
            controls=[
                ft.Container(
                    col=2 if sn['expanded'] else 1,
                    bgcolor=sn['color'],
                    # height=200,
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
                                style=ft.TextThemeStyle.BODY_MEDIUM),

                        ]
                    ),
                    on_hover=apply_shadow,
                         
                )for sn in saved_notes
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
                    scroll= ft.ScrollMode.HIDDEN,
                    controls=[notes()]
                ),
            ]
        )
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        shape=ft.CircleBorder(),
        tooltip='Adicionar Nota',
        bgcolor=ft.colors.INDIGO,

    )


    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)