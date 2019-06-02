# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 14:23
# @Author  : fangzeqiang_cover
# @File    : test_js.py

#V0.5 pip3 install pyecharts==0.5.11
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QDialog, QApplication, QHBoxLayout, QWidget, QGridLayout, QLabel, QSpinBox, \
    QSpacerItem, QSizePolicy, QComboBox
from random import randint
from pyecharts import Bar, Pie, Line, Overlap
from pyecharts_javascripthon.api import TRANSLATOR

TITLE_TEXT = "图表大标题"
TITLE_SUBTEXT = "副标题"
ATTR = ["属性1", "属性2", "属性3", "属性4", "属性5", "属性6"]


class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()

        self.view = None
        self.echarts = False
        self.initUi()
        self.load_url()

    def initUi(self):
        self.hl = QHBoxLayout(self)
        self.widget = QWidget()
        self.gl = QGridLayout(self.widget)
        # ATTR1
        label1 = QLabel(ATTR[0] + ':')
        self.gl.addWidget(label1, 1 - 1, 0, 1, 1)
        self.spinbox1 = QSpinBox()
        self.spinbox1.setSingleStep(100)
        self.spinbox1.setObjectName('spinbox')
        self.spinbox1.valueChanged.connect(self.set_options)
        self.spinbox1.setMaximum(1000)
        self.spinbox1.setValue(randint(0, 1000))
        self.gl.addWidget(self.spinbox1, 1 - 1, 1, 1, 1)
        # ATTR2
        label2 = QLabel(ATTR[1] + ':')
        self.gl.addWidget(label2, 2 - 1, 0, 1, 1)
        self.spinbox2 = QSpinBox()
        self.spinbox2.setSingleStep(100)
        self.spinbox2.setObjectName('spinbox')
        self.spinbox2.valueChanged.connect(self.set_options)
        self.spinbox2.setMaximum(1000)
        self.spinbox2.setValue(randint(0, 1000))
        self.gl.addWidget(self.spinbox2, 2 - 1, 1, 1, 1)
        # ATTR3
        label3 = QLabel(ATTR[2] + ':')
        self.gl.addWidget(label3, 3 - 1, 0, 1, 1)
        self.spinbox3 = QSpinBox()
        self.spinbox3.setSingleStep(100)
        self.spinbox3.setObjectName('spinbox')
        self.spinbox3.valueChanged.connect(self.set_options)
        self.spinbox3.setMaximum(1000)
        self.spinbox3.setValue(randint(0, 1000))
        self.gl.addWidget(self.spinbox3, 3 - 1, 1, 1, 1)
        # ATTR4
        label4 = QLabel(ATTR[3] + ':')
        self.gl.addWidget(label4, 4 - 1, 0, 1, 1)
        self.spinbox4 = QSpinBox()
        self.spinbox4.setSingleStep(100)
        self.spinbox4.setObjectName('spinbox')
        self.spinbox4.valueChanged.connect(self.set_options)
        self.spinbox4.setMaximum(1000)
        self.spinbox4.setValue(randint(0, 1000))
        self.gl.addWidget(self.spinbox4, 4 - 1, 1, 1, 1)
        # ATTR5
        label5 = QLabel(ATTR[4] + ':')
        self.gl.addWidget(label5, 5 - 1, 0, 1, 1)
        self.spinbox5 = QSpinBox()
        self.spinbox5.setSingleStep(100)
        self.spinbox5.setObjectName('spinbox')
        self.spinbox5.valueChanged.connect(self.set_options)
        self.spinbox5.setMaximum(1000)
        self.spinbox5.setValue(randint(0, 1000))
        self.gl.addWidget(self.spinbox5, 5 - 1, 1, 1, 1)
        # ATTR6
        label6 = QLabel(ATTR[5] + ':')
        self.gl.addWidget(label6, 6 - 1, 0, 1, 1)
        self.spinbox6 = QSpinBox()
        self.spinbox6.setSingleStep(100)
        self.spinbox6.setObjectName('spinbox')
        self.spinbox6.valueChanged.connect(self.set_options)
        self.spinbox6.setMaximum(1000)
        self.spinbox6.setValue(randint(0, 1000))
        self.gl.addWidget(self.spinbox6, 6 - 1, 1, 1, 1)

        self.hl.addWidget(self.widget)
        vs = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gl.addItem(vs, 6, 0, 1, 2)
        self.combobox_type = QComboBox()
        self.combobox_type.currentIndexChanged.connect(self.reload_canvas)
        self.combobox_type.addItems(['饼图', '柱状图', '折线图', '折线\柱状图'])
        self.gl.addWidget(self.combobox_type, 7, 0, 1, 2)
        self.combobox_theme = QComboBox()
        self.combobox_theme.currentTextChanged.connect(self.change_theme)
        self.combobox_theme.addItems(['日间模式', '暗黑模式'])
        self.gl.addWidget(self.combobox_theme, 8, 0, 1, 2)
        # 添加web view
        self.view = QWebEngineView()
        self.view.setContextMenuPolicy(Qt.NoContextMenu)
        self.hl.addWidget(self.view)

    def change_theme(self, theme):
        if not self.view:
            return
        options = self.get_options()
        if not options:
            return
        self.view.page().runJavaScript(
            f'''
                myChart.dispose();
                var myChart = echarts.init(document.getElementById('container'), '{theme}', {{renderer: 'canvas'}});
                myChart.clear();
                var option = eval({options});
                myChart.setOption(option);
            '''
        )

    def load_url(self):
        url = QUrl("file:////Users/fangzeqiang/Desktop/py_to_learn/PyQt_Echarts_GUI/template.html")
        self.view.load(url)
        self.view.loadFinished.connect(self.set_options)

    def reload_canvas(self):
        if not self.view:
            return
            # 重载画布
        options = self.get_options()
        if not options:
            return
        self.view.page().runJavaScript(
            f'''
                myChart.clear();
                var option = eval({options});
                myChart.setOption(option);
            '''
        )

    def set_options(self):
        if not self.view:
            return
        if not self.echarts:
            # 初始化echarts
            self.view.page().runJavaScript(
                '''
                    var myChart = echarts.init(document.getElementById('container'), 'light', {renderer: 'canvas'});
                '''
            )
            self.echarts = True

        options = self.get_options()
        if not options:
            return

        self.view.page().runJavaScript(
            f'''
                var option = eval({options});
                myChart.setOption(option);
            '''
        )

    def get_options(self):
        v1, v2, v3, v4, v5, v6 = self.spinbox1.value(), self.spinbox2.value(), self.spinbox3.value(), self.spinbox4.value(), \
                                 self.spinbox5.value(), self.spinbox6.value()
        v = [v1, v2, v3, v4, v5, v6]
        if self.combobox_type.currentIndex() == 0:
            # 饼图
            options = self.create_pie(v)
        elif self.combobox_type.currentIndex() == 1:
            # 柱状图
            options = self.create_bar(v)
        elif self.combobox_type.currentIndex() == 2:
            # 折线图
            options = self.create_line(v)
        elif self.combobox_type.currentIndex() == 3:
            # 折线、柱状图
            options = self.create_line_bar(v)
        else:
            return
        return options

    def create_pie(self, v):
        pie = Pie(TITLE_TEXT, TITLE_SUBTEXT)
        pie.add("属性", ATTR, v, is_label_show=True)
        snippet = TRANSLATOR.translate(pie.options)
        options = snippet.as_snippet()
        return options

    def create_bar(self, v):
        bar = Bar(TITLE_TEXT, TITLE_SUBTEXT)
        bar.add('属性1', ATTR, v, is_more_utils=True)
        bar.add('属性2', ATTR, v, is_more_utils=True)
        snippet = TRANSLATOR.translate(bar.options)
        options = snippet.as_snippet()
        return options

    def create_line(self, v):
        line = Line(TITLE_TEXT, TITLE_SUBTEXT)
        line.add("属性", ATTR, v, is_smooth=True, mark_line=["max", "average"])
        snippet = TRANSLATOR.translate(line.options)
        options = snippet.as_snippet()
        return options

    def create_line_bar(self, v):
        line = Line(TITLE_TEXT, TITLE_SUBTEXT)
        line.add("属性", ATTR, v, is_smooth=True, mark_line=["max", "average"])
        bar = Bar(TITLE_TEXT, TITLE_SUBTEXT)
        bar.add('属性', ATTR, v, is_more_utils=True)

        overlap = Overlap()
        overlap.add(line)
        overlap.add(bar)
        snippet = TRANSLATOR.translate(overlap.options)
        options = snippet.as_snippet()
        return options


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle('fusion')
    form = Form()
    form.show()
    sys.exit(app.exec_())
