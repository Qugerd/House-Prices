import numpy as np


def stats_block(df: pd.DataFrame, x_axis: str = '', y_axis: str = ''):
    """
    Отрисовка графика

    :code_assign: users
    :code_type: Пользовательские функции
    :imports: init_gui_dict, Window, Canvas, LinePlot, Scatter2DPlot

    :packages:

    :param_block pd.DataFrame df DataSet: Датасет
    :param str x_axis: Ocь X
    :param str y_axis: Ось Y

    :returns: df, gui_dict, error
    :rtype: pd.DataFrame, dict, str
    :semrtype: DataSet, ,
    """

    error = ''
    gui_dict = init_gui_dict()

    canvases = []

    plots = [Scatter2DPlot(x=np.array(df[x_axis]), y=np.array(df[y_axis]))]

    canvases.append(Canvas(
        title='Диаграмма рассеивания',
        y_title=y_axis,
        x_title=x_axis,
        showlegend=False,
        plots=plots))

    gui_dict['plot'].append(
        Window(
            window_title='Построение графиков параметров',
            canvases=canvases,
        ).to_dict()
    )

    gui_dict['table'].append(
        {
            'title': 'Средние значения',
            'value': {
                'Название столбца': [x_axis, y_axis],
                'Значение': [df[x_axis].mean(), df[y_axis].mean()]
            }
        }
    )

    return df, gui_dict, error