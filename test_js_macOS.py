# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 14:23
# @Author  : fangzeqiang_cover
# @File    : test_js.py
# pyechartsV0.5 pip3 install pyecharts==0.5.11

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QDialog, QApplication, QHBoxLayout, QWidget, QGridLayout, QLabel, QSpinBox, \
    QSpacerItem, QSizePolicy, QComboBox, QLineEdit
from random import randint
from pyecharts import Bar, Pie, Line, Overlap, Sankey
from pyecharts_javascripthon.api import TRANSLATOR

class Form(QDialog):

    TITLE_TEXT = "这是大标题"
    TITLE_SUBTEXT = "这是副标题"
    ATTR = ["属性1", "属性2", "属性3", "属性4", "属性5", "属性6"]

    def __init__(self):
        super(Form, self).__init__()

        self.view = None
        self.echarts = False
        self.initUi()
        self.load_url()

    # 初始化UI界面
    def initUi(self):
        self.hl = QHBoxLayout(self)
        self.widget = QWidget()
        self.gl = QGridLayout(self.widget)
       
        # ATTR1
        #第一个输入属性值的文本框
        self.QLineEdit1=QLineEdit()     # 新建属性输入文本框
        self.QLineEdit1.setPlaceholderText(self.ATTR[1-1]) # 默认值是“属性一”
        self.QLineEdit1.editingFinished.connect(self.reload_canvas)
        self.gl.addWidget(self.QLineEdit1,1 - 1,0,1,1)# 设置该输入框的排版位置
        self.spinbox1 = QSpinBox()      # 新建SpinBox
        self.spinbox1.setSingleStep(100)# 设置每次调节的单位
        self.spinbox1.setObjectName('spinbox')
        self.spinbox1.valueChanged.connect(self.set_options)
        self.spinbox1.setMaximum(1000)
        self.spinbox1.setValue(randint(0, 1000))
        self.gl.addWidget(self.spinbox1, 1 - 1, 1, 1, 2)
        # ATTR2
        self.QLineEdit2=QLineEdit()     
        self.QLineEdit2.setPlaceholderText(self.ATTR[2-1]) 
        self.QLineEdit2.returnPressed.connect(self.reload_canvas)
        self.gl.addWidget(self.QLineEdit2,2 - 1,0,1,1)
        self.spinbox2 = QSpinBox()
        self.spinbox2.setSingleStep(100)
        self.spinbox2.setObjectName('spinbox')
        self.spinbox2.valueChanged.connect(self.set_options)
        self.spinbox2.setMaximum(1000)
        self.spinbox2.setValue(randint(0, 1000))
        self.gl.addWidget(self.spinbox2, 2 - 1, 1, 1, 2)
        # ATTR3
        self.QLineEdit3=QLineEdit()     
        self.QLineEdit3.setPlaceholderText(self.ATTR[3-1]) 
        self.QLineEdit3.returnPressed.connect(self.reload_canvas)
        self.gl.addWidget(self.QLineEdit3,3 - 1,0,1,1)
        self.spinbox3 = QSpinBox()
        self.spinbox3.setSingleStep(100)
        self.spinbox3.setObjectName('spinbox')
        self.spinbox3.valueChanged.connect(self.set_options)
        self.spinbox3.setMaximum(1000)
        self.spinbox3.setValue(randint(0, 1000))
        self.gl.addWidget(self.spinbox3, 3 - 1, 1, 1, 2)
        # ATTR4
        self.QLineEdit4=QLineEdit()     
        self.QLineEdit4.setPlaceholderText(self.ATTR[4-1]) 
        self.QLineEdit4.returnPressed.connect(self.reload_canvas)
        self.gl.addWidget(self.QLineEdit4,4 - 1,0,1,1)
        self.spinbox4 = QSpinBox()
        self.spinbox4.setSingleStep(100)
        self.spinbox4.setObjectName('spinbox')
        self.spinbox4.valueChanged.connect(self.set_options)
        self.spinbox4.setMaximum(1000)
        self.spinbox4.setValue(randint(0, 1000))
        self.gl.addWidget(self.spinbox4, 4 - 1, 1, 1, 2)
        # ATTR5
        self.QLineEdit5=QLineEdit()     
        self.QLineEdit5.setPlaceholderText(self.ATTR[5-1]) 
        self.QLineEdit5.returnPressed.connect(self.reload_canvas)
        self.gl.addWidget(self.QLineEdit5,5 - 1,0,1,1)
        self.spinbox5 = QSpinBox()
        self.spinbox5.setSingleStep(100)
        self.spinbox5.setObjectName('spinbox')
        self.spinbox5.valueChanged.connect(self.set_options)
        self.spinbox5.setMaximum(1000)
        self.spinbox5.setValue(randint(0, 1000))
        self.gl.addWidget(self.spinbox5, 5 - 1, 1, 1, 2)
        # ATTR6
        self.QLineEdit6=QLineEdit()     
        self.QLineEdit6.setPlaceholderText(self.ATTR[6-1]) 
        self.QLineEdit6.returnPressed.connect(self.reload_canvas)
        self.gl.addWidget(self.QLineEdit6,6 - 1,0,1,1)
        self.spinbox6 = QSpinBox()
        self.spinbox6.setSingleStep(100)
        self.spinbox6.setObjectName('spinbox')
        self.spinbox6.valueChanged.connect(self.set_options)
        self.spinbox6.setMaximum(1000)
        self.spinbox6.setValue(randint(0, 1000))
        self.gl.addWidget(self.spinbox6, 6 - 1, 1, 1, 2)
        #属性文本框设置结束

        #左侧菜单设置
        self.hl.addWidget(self.widget)
        vs = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gl.addItem(vs, 8, 0, 1, 2)
        
        #输入大标题与副标题
        #大标题
        label_title = QLabel( '大标题'+ ':')
        self.gl.addWidget(label_title, 6, 0, 1, 2) #addWidget里的四个数字什么意思
        self.QLineEdit_TITLE = QLineEdit()        #查询pyqt的文本输入框是什么控件
        self.QLineEdit_TITLE.setPlaceholderText(self.TITLE_TEXT)
        self.QLineEdit_TITLE.cursorMoveStyle='VisualMoveStyle'
        self.QLineEdit_TITLE.returnPressed.connect(self.reload_canvas)
        self.gl.addWidget(self.QLineEdit_TITLE, 6, 1, 1, 2)
        #小标题
        label_subtitle = QLabel( '小标题'+ ':')
        self.gl.addWidget(label_subtitle, 7, 0, 1, 2)
        self.QLineEdit_SUB = QLineEdit()        #查询pyqt的文本输入框是什么控件
        self.QLineEdit_SUB.setPlaceholderText(self.TITLE_TEXT)
        self.QLineEdit_SUB.cursorMoveStyle='VisualMoveStyle'
        self.QLineEdit_SUB.returnPressed.connect(self.reload_canvas)
        self.gl.addWidget(self.QLineEdit_SUB, 7, 1, 1, 2)
        #输入大标题与副标题

        #图例种类选择
        label_kind = QLabel( '图例'+ ':')
        self.gl.addWidget(label_kind, 9, 0, 1, 2)
        self.combobox_type = QComboBox()
        self.combobox_type.currentIndexChanged.connect(self.reload_canvas)
        self.combobox_type.addItems(['饼状图', '柱状图', '折线图', '折线柱状图','桑基图'])
        self.gl.addWidget(self.combobox_type, 9, 1, 1, 2)
        
        #主题选择按钮
        label_theme = QLabel('主题' + ':')
        self.gl.addWidget(label_theme, 10, 0, 1, 2)
        self.combobox_theme = QComboBox()
        self.combobox_theme.addItems(['日间模式', '暗黑模式','复古香槟'])
        self.combobox_theme.currentTextChanged.connect(self.change_theme)
        self.gl.addWidget(self.combobox_theme, 10, 1, 1, 2)
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
        if self.combobox_theme.currentIndex()==0:
            theme='light'
        if self.combobox_theme.currentIndex()==1:
            theme='dark'
        if self.combobox_theme.currentIndex()==2:
            theme='vintage'

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
        url = QUrl("file:///"+sys.path[0]+"/template.html")
        #the formal version:url = QUrl("file:////Users/fangzeqiang/Desktop/PyQt_Echarts_GUI/template.html")
        self.view.load(url)
        self.view.loadFinished.connect(self.set_options)

    def reload_canvas(self):
        self.TITLE_TEXT=self.QLineEdit_TITLE.displayText()
        self.TITLE_SUBTEXT=self.QLineEdit_SUB.displayText()
        
        #重新渲染时，将左侧属性输入框中数据传入图表
        QLineEdit_Array=[self.QLineEdit1,self.QLineEdit2,self.QLineEdit3,self.QLineEdit4,self.QLineEdit5,self.QLineEdit6]
        for i in range(len(QLineEdit_Array)):
            self.ATTR[i]= QLineEdit_Array[i].displayText()  
            if self.ATTR[i]=='':
                self.ATTR[i]='属性'+str(i+1)
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
                    var myChart = echarts.init(document.getElementById('container'),'light',{renderer: 'canvas'});
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
            # 桑基图
        elif self.combobox_type.currentIndex() == 4:
            options=self.create_sankey(v)
        else:
            return
        return options

    def create_pie(self, v):
        pie = Pie(self.TITLE_TEXT, self.TITLE_SUBTEXT)
        pie.add("属性", self.ATTR, v, is_label_show=True)
        snippet = TRANSLATOR.translate(pie.options)
        options = snippet.as_snippet()
        return options

    def create_bar(self, v):
        bar = Bar(self.TITLE_TEXT, self.TITLE_SUBTEXT)
        bar.add('属性1', self.ATTR, v, is_more_utils=True)
        bar.add('属性2', self.ATTR, v, is_more_utils=True)
        snippet = TRANSLATOR.translate(bar.options)
        options = snippet.as_snippet()
        return options

    def create_line(self, v):
        line = Line(self.TITLE_TEXT, self.TITLE_SUBTEXT)
        line.add("属性", self.ATTR, v, is_smooth=True, mark_line=["max", "average"])
        snippet = TRANSLATOR.translate(line.options)
        options = snippet.as_snippet()
        return options

    def create_line_bar(self, v):
        line = Line(self.TITLE_TEXT, self.TITLE_SUBTEXT)
        line.add("属性", self.ATTR, v, is_smooth=True, mark_line=["max", "average"])
        bar = Bar(self.TITLE_TEXT, self.TITLE_SUBTEXT)
        bar.add('属性', self.ATTR, v, is_more_utils=True)
        overlap = Overlap()
        overlap.add(line)
        overlap.add(bar)
        snippet = TRANSLATOR.translate(overlap.options)
        options = snippet.as_snippet()
        return options

    def create_sankey(self, v): #绘制桑基图
        sankey = Sankey(self.TITLE_TEXT, self.TITLE_SUBTEXT)
        category1,category2,category3,category4,category5,category6=self.ATTR[0],self.ATTR[1],self.ATTR[2],self.ATTR[3],self.ATTR[4],self.ATTR[5]

        nodes = [
            {'name': category1}, {'name': category2}, {'name': category3},
            {'name': category4}, {'name': category5}, {'name': category6}
        ]
        links = [
            {'source': category1, 'target': category2, 'value': 10},
            {'source': category2, 'target': category3, 'value': 15},
            {'source': category3, 'target': category4, 'value': 20},
            {'source': category5, 'target': category6, 'value': 25}
        ]
        sankey.add(
            "sankey",
            nodes,
            links,
            line_opacity=0.2,
            line_curve=0.5,
            line_color="source",
            is_label_show=True,
            label_pos="right",
        )
        snippet = TRANSLATOR.translate(sankey.options)
        options = snippet.as_snippet()
        return options
    

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    form = Form()
    form.show()
    sys.exit(app.exec_())
