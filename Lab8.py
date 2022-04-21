from tkinter import*
from tkinter import ttk
from turtle import st
from pokeapi import getthepokemon

def main():

    root = Tk()#making the window
    root.title('Pokemon statistic viewer')
    root.iconbitmap('pokeballicon.ico')
    root.resizable(False,False)

    #making the frames of GUI
    input_frame = ttk.Frame(root)
    input_frame.grid(row=0, column=0, columnspan=2)
    info_frame = ttk.LabelFrame(root, text ='Info')
    info_frame.grid(row=1, column=0,padx=(10,5),pady=(0,10),sticky=N)
    stats_frame = ttk.LabelFrame(root, text='Stats')
    stats_frame.grid(row=1, column=1,padx=(5,10),pady=(0,10),sticky=N)
    name_label = ttk.Label(input_frame, text="Name of the Pokemon:")
    name_label.grid(row=0, column=0, padx=10, pady=10)

    name = ttk.Entry(input_frame, width= 25)
    name.grid(row=0,column=1, padx=10, pady=10)

    def button_name_click():
        PokeName = name.get()
        infopoke = getthepokemon(PokeName)
        if infopoke:
            HeightValue['text'] = str(infopoke['height']) + 'dm'
            WeightValue['text'] = str(infopoke['weight']) + 'hg'
            types_list = (t['type']['name']for t in infopoke['types'])
            TypeValue['text'] = ', '.join(types_list) 

            HPBAR['value'] = infopoke['stats'][0]['base_stat']
            ATKBAR['value'] = infopoke['stats'][1]['base_stat']
            DEFBAR['value'] = infopoke['stats'][2]['base_stat']
            SPATKBAR['value'] = infopoke['stats'][3]['base_stat']
            SPDEFBAR['value'] = infopoke['stats'][4]['base_stat']
            SODVAR['value'] = infopoke['stats'][5]['base_stat']
            

    Button = ttk.Button(input_frame, text="Get Info", command=button_name_click)
    Button.grid(row=0,column=2, padx=10, pady=10)

    #stat frames 
    label_hp = ttk.Label(stats_frame,text="HP:")
    label_hp.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    HPBAR = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    HPBAR.grid(row=0,column=1,padx=5,pady=5)
    ATKLABEL = ttk.Label(stats_frame,text="Attack:")
    ATKLABEL.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    ATKBAR = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    ATKBAR.grid(row=1,column=1,padx=5,pady=5)
    DEFLABEL = ttk.Label(stats_frame,text="Defence:")
    DEFLABEL.grid(row=2,column=0,padx=5,pady=5,sticky=E)
    DEFBAR = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    DEFBAR.grid(row=2,column=1,padx=5,pady=5)
    SPATKLABEL = ttk.Label(stats_frame,text="Special Attack:")
    SPATKLABEL.grid(row=3,column=0,padx=5,pady=5,sticky=E)
    SPATKBAR = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    SPATKBAR.grid(row=3,column=1,padx=5,pady=5)
    SPDEFLABEL = ttk.Label(stats_frame,text="Special Defence:")
    SPDEFLABEL.grid(row=4,column=0,padx=5,pady=5,sticky=E)
    SPDEFBAR = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    SPDEFBAR.grid(row=4,column=1,padx=5,pady=5)
    SPDLABEL = ttk.Label(stats_frame,text="Speed:")
    SPDLABEL.grid(row=5,column=0,padx=5,pady=5,sticky=E)
    SODVAR = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    SODVAR.grid(row=5,column=1,padx=5,pady=5)

    #info frames
    Height = ttk.Label(info_frame, text="Height:")
    Height.grid(row=0,column=0,padx=10,pady=10,sticky=E)
    HeightValue = ttk.Label(info_frame, text="---")
    HeightValue.grid(row=0,column=1,padx=10,pady=10,sticky=W)
    Weight = ttk.Label(info_frame, text="Weight:")
    Weight.grid(row=1,column=0,padx=10,sticky=E)
    WeightValue = ttk.Label(info_frame, text="---")
    WeightValue.grid(row=1,column=1,padx=10,sticky=W)
    Type = ttk.Label(info_frame, text="Type:")
    Type.grid(row=2,column=0,padx=10,pady=10,sticky=E)
    TypeValue = ttk.Label(info_frame, text="---")
    TypeValue.grid(row=2,column=1,padx=10,pady=10,sticky=W)
    root.mainloop()

main()