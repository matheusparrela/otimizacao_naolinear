import os
from delphifmx import *
import search_result
import metodo_newton
import metodo_newton_modificado
import utils
import sympy as sy


class frmMain(Form):
    last_result: search_result.SearchResult

    def __init__(self, owner):
        self.lytFunction = None
        self.edtFunction = None
        self.lblFunction = None
        self.stbStyle = None
        self.lytOptions = None
        self.btnCalculate = None
        self.lytStartPoint = None
        self.lblStartPoint = None
        self.edtStartPoint = None
        self.lytMethod = None
        self.lblMethod = None
        self.cbxMethod = None
        self.tbcResults = None
        self.tbiPlot = None
        self.imgPlotImage = None
        self.tbiIterations = None
        self.tbi3D = None
        self.memIterations = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "MainForm.pyfmx"))

    def btnCalculateClick(self, Sender):
        self.tbcResults.TabIndex = 0
        self.memIterations.Lines.Text = ""
        start_point = utils.parse_start_point(self.edtStartPoint.Text, 2)

        if self.cbxMethod.ItemIndex == 0:
            self.last_result = metodo_newton.newton(self.edtFunction.Text, start_point[0], start_point[1], 4)
        else:
            self.last_result = metodo_newton_modificado.modificado(self.edtFunction.Text, start_point[0], start_point[1], 4)

        self.last_result.plot("plot.png")
        if os.path.exists("plot.png"):
            self.imgPlotImage.Bitmap.LoadFromFile("plot.png")
            os.remove("plot.png")
        else:
            self.imgPlotImage.Bitmap.Assign(None)
        self.memIterations.Lines.Text = self.last_result

    def imgPlotImageDblClick(self, Sender):
        if not (self.last_result is None):
            self.last_result.plot()  

    def tbcResultsChange(self, Sender):
        if self.last_result is None:
            self.tbcResults.TabIndex = 0

def main():
    Application.Initialize()
    Application.Title = 'Otimização Não Linear'
    Application.MainForm = frmMain(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

#if __name__ == '__main__':
main()
