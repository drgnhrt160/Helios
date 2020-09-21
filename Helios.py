import wolframalpha

client = wolframalpha.Client("PT6G92-A37GP6QJHT")
import wikipedia


import PySimpleGUI as sg

sg.theme('DarkBlack1')	
layout = [  [sg.Text('Hey I am Helios! Your assistant. Ask Away!')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Helios', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    try:
        res = client.query(values[0])
        wolfram_res = next(res.results).text
        wiki_res = wikipedia.summary(values[0], sentences=2)
        sg.Popup("Wolfram Results: " + wolfram_res, "Wikipedia Results: " + wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        res = client.query(values[0])
        wolfram_res = next(res.results).text
        sg.Popup("Wolfram Results: " + wolfram_res)
    except wikipedia.exceptions.PageError:
        sg.Popup("No data found")
        

window.close()
