import tkinter as tk
import tkinter.messagebox
root = tk.Tk()
root.title("Tic-Tac-Toe")
player_1_var = tk.StringVar()
player_1_label = tk.Label(root,text= "Player 1 : ",bg="white",fg="green",font="Times 20 bold")
player_1_entry = tk.Entry(root,textvariable = player_1_var,bd=5)
player_2_var = tk.StringVar()
player_2_label = tk.Label(root,text= "Player 2 : ",bg="white",fg="green",font="Times 20 bold")
player_2_entry = tk.Entry(root,textvariable = player_2_var,bd=5)
player_1_win = ""
player_2_win = ""
flag = 0 # to count total buttons clicked and to check tie condition
b_click = True # to track X and O of each user
buttons = tk.StringVar()
def disable_buttons(): # to disable all buttons when user wins
	button1.configure(state="disabled")
	button2.configure(state="disabled")
	button3.configure(state="disabled")
	button4.configure(state="disabled")
	button5.configure(state="disabled")
	button6.configure(state="disabled")
	button7.configure(state="disabled")
	button8.configure(state="disabled")
	button9.configure(state="disabled")
def btn_click(buttons):
	global b_click,flag,player_1_win,player_2_win
	if buttons['text'] == "" and b_click == True :
		buttons["text"] = "X"
		b_click = False
		flag = flag +  1
		player_1_win = player_1_var.get() + " Wins!"
		check_for_win()
	elif buttons['text'] == "" and b_click == False :
		buttons["text"] = "O"
		b_click = True
		flag = flag +  1
		player_2_win = player_2_var.get() + " Wins!"
		check_for_win()
	else:
		tkinter.messagebox.showinfo("Tic-Tac-Toe","Button Already Clicked!!")
def check_for_win():
	if  button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"  or button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"  or button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" :
		tkinter.messagebox.showinfo("Tic-Tac-Toe",player_1_win)
		disable_buttons()
	elif  button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O"  or button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"  or button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" :
		tkinter.messagebox.showinfo("Tic-Tac-Toe",player_2_win)
		disable_buttons()
	elif flag == 9 : 
		tkinter.messagebox.showinfo("Tic-Tac-Toe","It's a Tie!!")
		disable_buttons()
button1 = tk.Button(root,text="",fg="white",bg="grey",font="Times 20 bold",height=4,width=8,command = lambda : btn_click(button1))
button2 = tk.Button(root,text="",fg="white",bg="grey",font="Times 20 bold",height=4,width=8,command = lambda : btn_click(button2))
button3 = tk.Button(root,text="",fg="white",bg="grey",font="Times 20 bold",height=4,width=8,command = lambda : btn_click(button3))
button4 = tk.Button(root,text="",fg="white",bg="grey",font="Times 20 bold",height=4,width=8,command = lambda : btn_click(button4))
button5 = tk.Button(root,text="",fg="white",bg="grey",font="Times 20 bold",height=4,width=8,command = lambda : btn_click(button5))
button6 = tk.Button(root,text="",fg="white",bg="grey",font="Times 20 bold",height=4,width=8,command = lambda : btn_click(button6))
button7 = tk.Button(root,text="",fg="white",bg="grey",font="Times 20 bold",height=4,width=8,command = lambda : btn_click(button7))
button8 = tk.Button(root,text="",fg="white",bg="grey",font="Times 20 bold",height=4,width=8,command = lambda : btn_click(button8))
button9 = tk.Button(root,text="",fg="white",bg="grey",font="Times 20 bold",height=4,width=8,command = lambda : btn_click(button9))
player_1_label.grid(row = 0,column = 0)
player_1_entry.grid(row = 0,column = 1)
player_2_label.grid(row = 1,column = 0)
player_2_entry.grid(row = 1,column = 1)
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
button3.grid(row=2,column=2)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
button7.grid(row=4,column=0)
button8.grid(row=4,column=1)
button9.grid(row=4,column=2)
buttons = tk.StringVar()
root.mainloop()