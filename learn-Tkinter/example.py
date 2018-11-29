import tkinter
mainForm = tkinter.Tk()
mainForm.title('Shahr Fixed Income Fund')
def btnCalculatePressed():
    txtCalculationResult.delete('1.0', 'end')
    #txtCalculationResult.insert(tkinter.INSERT, "Button was pressed")
    #txtCalculationResult.pack()
    yourIncomePortion = txtFixedIncome.get('1.0', 'end')
    print(yourIncomePortion)
    txtCalculationResult.insert(tkinter.INSERT, yourIncomePortion)
btnCalculate = tkinter.Button(mainForm , text = "Calculate", command= btnCalculatePressed)
txtCalculationResult = tkinter.Text(mainForm )
txtCalculationResult.insert(tkinter.INSERT, "CalculationResults")
txtFixedIncome = tkinter.Text(mainForm, height = 1, width = 30 )
txtFixedIncome.insert(tkinter.INSERT, "your income portion")

txtFixedIncome.pack();
txtCalculationResult.pack()
btnCalculate.pack()

mainForm.mainloop()