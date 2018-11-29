import tkinter
mainForm = tkinter.Tk()
mainForm.title('Shahr Fixed Income Fund')
def updat(text):
    try:txtCalculationResult.insert(tkinter.INSERT,"{:,.0f}".format(float(text)))
    except:txtCalculationResult.insert(tkinter.INSERT,"CalculationResults")
def btnCalculatePressed():
    txtCalculationResult.delete('1.0', 'end')
    yourIncomePortion = txtFixedIncome.get('1.0', 'end')
    updat(yourIncomePortion)
btnCalculate = tkinter.Button(mainForm , text = "Calculate", command= btnCalculatePressed)
txtCalculationResult = tkinter.Text(mainForm)
txtCalculationResult.insert(tkinter.INSERT, "CalculationResults")
txtFixedIncome = tkinter.Text(mainForm, height = 1, width = 30 )
txtFixedIncome.insert(tkinter.INSERT, "your income portion")

txtFixedIncome.bind("<FocusIn>",lambda _:txtFixedIncome.delete('1.0', 'end'))
txtFixedIncome.bind("<FocusOut>",lambda _:txtFixedIncome.insert("1.0","your income portion" if str(txtFixedIncome.get("1.0","end")) == "\n" else ""))

txtFixedIncome.pack();
txtCalculationResult.pack()
btnCalculate.pack()

mainForm.mainloop()