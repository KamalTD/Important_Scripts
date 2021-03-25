from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide2 import QtWidgets
import maya.mel as mel

class DialogWidget(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(DialogWidget, self).__init__(parent=parent)
        #self.setObjectName('MY_CUSTOM_UI')
        self.setWindowTitle('TEST')
        layout = QtWidgets.QGridLayout()
        button = QtWidgets.QPushButton("HELP")
        layout.addWidget(button)
        self.setLayout(layout)



DialogWidget_= DialogWidget()

workspaceControlName = DialogWidget_.objectName() + 'WorkspaceControl'
if cmds.workspaceControl(workspaceControlName, q=True, exists=True):
    cmds.workspaceControl(workspaceControlName, e=True, close=True)
    cmds.deleteUI(workspaceControlName, control=True)

DialogWidget_.show(dockable=True,area="right", floating=False)

mayaPanelName = "AttributeEditor"
cmds.workspaceControl(workspaceControlName, edit=True, tabToControl=[mayaPanelName, -1], widthProperty="preferred", minimumWidth=620)
