from tkinter import *
import tkinter as tk
from tkinter import ttk
import cv2
import time
import pygame
from PIL import Image, ImageTk
import winsound
splash_window = Tk()
time = 5
splash_window.title("Splash Screen")
splash_window.overrideredirect(True)
app_width = splash_window.winfo_screenwidth()
app_height = splash_window.winfo_screenheight()

splash_window.geometry(f'{app_width}x{app_height}')
splash_window.config(bg="black")
window_label = Label(splash_window, text="The \n FLASH", font=("BLOODY TYPE PERSONAL USE", 200, "bold"), fg="red", bg="black")
window_label.pack(pady=30)

progressbar = ttk.Progressbar()
progress = ttk.Style()
progress.theme_use('alt')

progressbar.place(x=300, y=600, width=800, height=20)
progressbar.step(time)
progressbar.start()

time = 60
heart=3
prev_score = 0 
#sound

def sound_win():
    winsound.PlaySound('./sound/TB7L64W-winning.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
def sound_lost():
    winsound.PlaySound('./sound/mixkit-battle-man-scream-2175.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
def sound_menu():
    pygame.mixer.init()
    pygame.mixer.music.load('sound/menu_sound.wav')
    pygame.mixer.music.play(loops=-1)
def stop_sound():
    winsound.PlaySound(None, winsound.SND_PURGE)
def sound_start():
    winsound.PlaySound('sound/_start_game.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
def monster_sound():
    winsound.PlaySound('sound/monster_sound.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

def sound_win():
    winsound.PlaySound('./sound/TB7L64W-winning.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

def play_video(video_path, window_width, window_height, playback_fps):
    video_capture = cv2.VideoCapture(video_path)
    cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video Player', window_width, window_height)
    delay = int(1000 / playback_fps)
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        cv2.imshow('Video Player', frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    # menu()


#main
def main():
    splash_window.destroy()
    global window, canvas, wall_1, wall_2, wall_3
    window = Tk()
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()

    window.geometry(f'{app_width}x{app_height}')
    window.title("Jump to heart")
    frame = Frame(window)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height, bg="white")
    canvas.pack(pady=10)
    # video_path = './image/a.mp4'
    # window1_width = app_width
    # window1_height = app_height
    # playback_fps =1000

    # play_video(video_path, window1_width, window1_height, playback_fps)
    menu()
    # startGame()
    window.mainloop()
 

#times

def settime():
    global time, canvas, lose_heart, heart, score, prev_score,score_game
    canvas.itemconfig(timer_text, text='Timer : ' + str(time) + "s")
    if time <= 100 :
        time -= 1

    if time <= 0:
        window.after(1000, lost)

    # Check if the score has changed
    if score != prev_score:
        score_game()  
        prev_score = score  
    canvas.after(1000, settime)


#change bg
def chage_bg():
    canvas.itemconfig(background_image_label_1,image=background_image1)
    canvas.itemconfig(background_image_label_2,image=background_image1)
    canvas.itemconfig('wall',fill='red')

#auto sound
def sound_menu_auto():
    try:
        while True:
            continue
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
def count_point():
    pass
def lost():
    lost_side()
def win():
    win_side()

#keypress for player work
a=1
arr = []
def key_press(event):
    global arr, canvas, player, wall_2, wall_3, ply_lefts, sword_wall2_id,players_img,change_original2,time2_id,time,check_collision,a
    def collisionCheck():
        oval_coords = canvas.coords(player)
        wall_coords3 = canvas.coords(wall_3)
        if oval_coords[0]==wall_coords3[0]:
            return True
        return False
    def moveright():
        canvas.move(player, 209, 0)

    def moverleft():
        canvas.move(player, -209, 0)

    oval_coords = canvas.coords(player)
    wall_coords2 = canvas.coords(wall_2)
    wall_coords3 = canvas.coords(wall_3)

    def check_collision():
        player_x, player_y = canvas.coords(player)
        enemy1_x, enemy1_y = canvas.coords(insect1s1i_ds)
        enemy2_x, enemy2_y = canvas.coords(lion1s)
        enemy3_x, enemy3_y = canvas.coords(sword_wall2_id)
        enemy4_x, enemy4_y = canvas.coords(sward_wall3_id)
        enemy5_x, enemy5_y = canvas.coords(lion1s)

        if (player_x - enemy1_x)**2 + (player_y - enemy1_y)**2 <= 70**2:  
            print("Player collided with enemy 1")
            game_over()

        if (player_x - enemy2_x)**2 + (player_y - enemy2_y)**2 <= 70**2:
            print("Player collided with enemy 2")
            game_over()
        if (player_x - enemy3_x)**2 + (player_y - enemy3_y)**2 <= 70**2:
            print("Player collided with enemy 2")
            game_over()
        if (player_x - enemy4_x)**2 + (player_y - enemy4_y)**2 <= 70**2:
            print("Player collided with enemy 2")
            game_over()
        if (player_x - enemy5_x)**2 + (player_y - enemy5_y)**2 <= 70**2:
            print("Player collided with enemy 2")
            game_over()
    def game_over():
        print("Game Over")
        lost_side()
    def change_original():
        canvas.itemconfig(player, image=ply_lefts)
    def change_original2():
    
        canvas.itemconfig(player, image=players_img)
    if event.keysym == "Right" and "Right" not in arr:
        if oval_coords[0] <= wall_coords3[0]:
            if collisionCheck:
                canvas.itemconfig(player,image=ply_lefts)
                moveright() 
                arr = ["Right"]
                a=0
    elif event.keysym == "Left" and "Left" not in arr and a ==0:
        if oval_coords[0] > wall_coords2[0]:
            canvas.itemconfig(player, image=players_img)
            moverleft()
            arr = ["Left"]
   
    elif event.keysym == "Down":
        if oval_coords[0] >wall_coords2[0] :
            canvas.move(player, 0, 15)
            if arr == ["Right"]:
                canvas.itemconfig(player, image=ply_lefts)
                canvas.after(5, change_original)
            else:
                canvas.itemconfig(player,image=ply_fight_ri)
                canvas.after(5, change_original2)   
    elif event.keysym == "Up":
        if oval_coords[0] >= wall_coords2[2] :
            canvas.move(player, 0, -15)
            if arr == ["Right"]:
                canvas.itemconfig(player, image=ply_lefts)
                canvas.after(5, change_original)
            else:
                canvas.itemconfig(player,image=ply_fight_ri)
                canvas.after(5, change_original2)
    window.bind("<Key>",key_press)
    check_collision()
#start gameplay
def startGame():
    global window, canvas,c, wall_2, wall_3,timer_text,lost_side,time,win_side,lose_heart,score_text,score,player,ply_lefts,sword_wall2_id,players_img,SCROLLING_SPEED,background_image1,background_image_label_1,background_image_label_2,ply_fight_lt,ply_fight_ri,time2_id,insect1s1i_ds,lion1s,score_game,sward_wall3_id
    window.destroy()
    window = Tk()
    time=100
    SCROLLING_SPEED =1000
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry('2000x800')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    original_image = Image.open("image/forest.png")
    image_resize = original_image.resize((app_width, app_height))
    background_image = ImageTk.PhotoImage(image_resize)

    original_image1 = Image.open("img/hell.jpg")
    image_resize1 = original_image1.resize((app_width, app_height))
    background_image1 = ImageTk.PhotoImage(image_resize1)

    background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_image)
    background_image_label_2= canvas.create_image(app_width, 0,anchor=tk.NW, image=background_image)

    #auto bg
    def scroll_bg_image():
        
        canvas.move(background_image_label_1, -0.2, 0)
        canvas.move(background_image_label_2, -0.2, 0)

        if canvas.coords(background_image_label_1)[0]< -app_width:
            canvas.coords(background_image_label_1, app_width, 0)
        elif canvas.coords(background_image_label_2)[0]< -app_width:
            canvas.coords(background_image_label_2, app_width, 0)
        canvas.after(1, scroll_bg_image)

    scroll_bg_image()
    score=0
    def score_game():
        global score
        canvas.itemconfig(score_text, text=f"Score: {score}")
        if score==70:
            window.after(1000, win)
        if score>=50:
            chage_bg()
#move enemy
    def move_insects():
        canvas.move(lion1s, 0, 2)
        canvas.move(insect1s1i_ds, 0, -2)
        canvas.move(insect2_id, 0, -2)
        canvas.move(lion_wall3_ds, 0, -2)
        canvas.move(insect1_wall3_id, 0, -2)
        canvas.move(sward_wall3_id, 0, -0.2)
        if score>=70:
            canvas.move(the_king1, 0, -0.6)
        canvas.after(10, move_insects)
    def move_insects1():
        global score
        canvas.move(lion2s, 0, 2)
        canvas.move(insect2s_id, 0, 2)
        canvas.move(kondob_wall3_id, 0, 2)
        if canvas.coords(lion2s)[1] >= app_height-100:
            canvas.move(lion2s, 0, -app_height)
            score+=1
        if canvas.coords(insect2s_id)[1] >= app_height-100:
            canvas.move(insect2s_id, 0, -app_height)
            score+=1
        if canvas.coords(kondob_wall3_id)[1] >= app_height-100:
            canvas.move(kondob_wall3_id, 0, -app_height)
            score+=1

        if time <= 45:
            canvas.move(time2_id, 0, 1)
        if time >=50:
            canvas.move(The_king2, 0, 1)
            monster_sound()

        canvas.after(10, move_insects1)


    def change_bg():
        if score>=10:
            canvas.itemconfig(background_image,image=background_image1)
    
    #lose window
    def lost_side():
        nonlocal game_over_shown

        if game_over_shown:
            return

        game_over_shown = True
        win_window = Toplevel(window)
        win_window.title("Game Over")
        lost_window_width = 700
        win_window_height = 500
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - lost_window_width) // 2
        y = (screen_height - win_window_height) // 2
        win_window.geometry(f'{lost_window_width}x{win_window_height}+{x}+{y}')
        
        frame = Frame(win_window, width=lost_window_width, height=win_window_height)
        frame.pack()

        canvas = Canvas(frame, width=lost_window_width, height=win_window_height)
        canvas.pack()

        # Load the background image
        bg_image = Image.open("./image/lost.jpg")
        bg_image = bg_image.resize((lost_window_width, win_window_height))
        background = ImageTk.PhotoImage(bg_image)
        canvas.background = background
        # Create a background image on the canvas
        canvas.create_image(0, 0, image=background,anchor=NW)
        canvas.create_text(340, 100, text="YOU DIE", fill="red", font=('BLOODY TYPE PERSONAL USE', 100))

        # Load the image to overlay on top of the background
        overlay1 = Image.open("image/dav.png")
        overlay1 = overlay1.resize((200, 200))
        overlay1 = ImageTk.PhotoImage(overlay1)
        canvas.create_image(100, 50, image=overlay1, anchor=CENTER)

        overlay_image = Image.open("image/dav.png")
        overlay_image = overlay_image.resize((200, 200))
        overlay = ImageTk.PhotoImage(overlay_image)
        Sward1 = canvas.create_image(580, 50, image=overlay, anchor="center")
            
        button_back = Button(frame, text="Back!", command=menu, bg='red', border=10)
        button_back.pack()
        button_back.place(x=70, y=400, width=100)

        button_play_again = Button(frame, text="PLAY AGAIN", command=startGame, bg='red', border=10)
        button_play_again.pack()
        button_play_again.place(x=550, y=400, width=100)
        sound_lost()

    game_over_shown = False
    #win window
    def win_side():
        nonlocal game_win_shown

        if game_win_shown:
            return

        game_win_shown = True

        win_window = Toplevel(window)
        win_window.title("Game Win")
        win_window_width = 700
        win_window_height = 500
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - win_window_width) // 2
        y = (screen_height - win_window_height) // 2
        win_window.geometry(f'{win_window_width}x{win_window_height}+{x}+{y}')
        
        frame = Frame(win_window, width=win_window_width, height=win_window_height)
        frame.pack()

        canvas = Canvas(frame, width=win_window_width, height=win_window_height)
        canvas.pack()
        bg_image = Image.open("./image/win.jpg")
        bg_image = bg_image.resize((700, 500))
        background = ImageTk.PhotoImage(bg_image)
        canvas.background = background
        # Create a background image on the canvas
        canvas.create_image(0, 0, image=background, anchor=NW)

        canvas.create_text(340, 100, text="YOU WIN", fill="red", font=('BLOODY TYPE PERSONAL USE', 100))
 
        button_back = Button(frame, text="PLAY AGAIN", command=startGame, bg='red',border=10)
        button_back.pack()
        button_back.place(x=70, y=400, width=100)

        button_play_again = Button(frame, text="Exit!", command=exitGame, bg='red',border=10)
        button_play_again.pack()
        button_play_again.place(x=550, y=400, width=100)
        sound_win()
    game_win_shown=False

    # # dav_back
    sword_wall2 = Image.open("./image/dav1.png")
    sword_wall2 = sword_wall2.resize((200, 200))
    sword_wall2 = ImageTk.PhotoImage(sword_wall2)
    sword_wall2_id=canvas.create_image(310, 80, image=sword_wall2, anchor=CENTER, tags="time")
    # 
    sward_back = Image.open("image/dav_up.png")
    sward_back = sward_back.resize((200, 200))
    sward_back = ImageTk.PhotoImage(sward_back)

    #charater right
    players = Image.open("./image/player_right.png")
    player_resize = players.resize((70, 70))
    players_img = ImageTk.PhotoImage(player_resize)
    player = canvas.create_image(730, 400, image=players_img, anchor=CENTER, tags="time")

    # character left
    ply_left = Image.open("image/player_left.png")
    ply_left = ply_left.resize((70, 70))
    ply_lefts = ImageTk.PhotoImage(ply_left)
    #character fight right
    ply_fight_right = Image.open("image/player_right_fight.png")
    ply_fight_right = ply_fight_right.resize((70, 70))
    ply_fight_ri = ImageTk.PhotoImage(ply_fight_right)
    
    ply_fight_lefts1 = Image.open("image/player_left_fight.png")
    ply_fight_lefts1 = ply_fight_lefts1.resize((70, 70))
    ply_fight_lt = ImageTk.PhotoImage(ply_fight_lefts1)
#wall 2
    # int1_wall2 = Image.open("./img/insect_kadob1.png")
    # int1_wall2 = int1_wall2.resize((70, 70))
    # int1_wall2 = ImageTk.PhotoImage(int1_wall2)
    # int1_wall2_id =canvas.create_image(350, 900, image=int1_wall2, anchor=CENTER)
    
    insect1xa = Image.open("img/lion1.png")
    insect1xa = insect1xa.resize((70, 70))
    insect1xa = ImageTk.PhotoImage(insect1xa)
    insect1s1i_ds =canvas.create_image(720, 1000, image=insect1xa, anchor=CENTER)

    the_king = Image.open("img/king2.png")
    the_king = the_king.resize((70, 70))
    the_king = ImageTk.PhotoImage(the_king)
    the_king1 =canvas.create_image(990, 1000, image=the_king, anchor=CENTER)

    The_king_lady = Image.open("img/king1.png")
    The_king_lady = The_king_lady.resize((70, 70))
    The_king_lady = ImageTk.PhotoImage(The_king_lady)
    The_king2 =canvas.create_image(720, 1000, image=The_king_lady, anchor=CENTER)
    
    lion1 = Image.open("img/lion1.png")
    lion1 = lion1.resize((70, 70))
    lion1 = ImageTk.PhotoImage(lion1)
    lion1s =canvas.create_image(720, 900, image=lion1, anchor=CENTER)

    insect2 = Image.open("./img/insect_ruy1.png")
    insect2 = insect2.resize((70, 70))
    insect2 = ImageTk.PhotoImage(insect2)
    insect2_id=canvas.create_image(720, 700, image=insect2, anchor=CENTER)
    
    insect2x = Image.open("./img/insect_ruy2.png")
    insect2x = insect2x.resize((70, 70))
    insect2x = ImageTk.PhotoImage(insect2x)
    insect2s_id=canvas.create_image(638, 10, image=insect2x, anchor=CENTER)
    insect2s_id=canvas.create_image(638, 10, image=insect2x, anchor=CENTER)
#wall3
    insect1_wall3 = Image.open("./img/insect_kadob1.png")
    insect1_wall3 = insect1_wall3.resize((70, 70))
    insect1_wall3 = ImageTk.PhotoImage(insect1_wall3)
    insect1_wall3_id =canvas.create_image(1040, 700, image=insect1_wall3, anchor=CENTER)
    
    sward_wall3 = Image.open("./image/dav1.png")
    sward_wall3 = sward_wall3.resize((200, 200))
    sward_wall3 = ImageTk.PhotoImage(sward_wall3)
    sward_wall3_id=canvas.create_image(1050, 0, image=sward_wall3, anchor=CENTER)
    
    kondob_wall3 = Image.open("img/insect_kondop2.png")
    kondob_wall3 = kondob_wall3.resize((70, 70))
    kondob_wall3 = ImageTk.PhotoImage(kondob_wall3)
    kondob_wall3_id =canvas.create_image(955, 130, image=kondob_wall3, anchor=CENTER)
    
    lion_wall3 = Image.open("img/lion1.png")
    lion_wall3 = lion_wall3.resize((70, 70))
    lion_wall3 = ImageTk.PhotoImage(lion_wall3)
    lion_wall3_ds =canvas.create_image(1050, 300, image=lion_wall3, anchor=CENTER)
    
    lion2 = Image.open("img/lion2.png")
    lion2 = lion2.resize((70, 70))
    lion2 = ImageTk.PhotoImage(lion2)
    lion2s =canvas.create_image(635, 300, image=lion2, anchor=CENTER)
    
    lion1 = Image.open("img/lion1.png")
    lion1 = lion1.resize((70, 70))
    lion1 = ImageTk.PhotoImage(lion1)
    lion1s =canvas.create_image(720, 900, image=lion1, anchor=CENTER)

    insect2 = Image.open("./img/insect_ruy1.png")
    insect2 = insect2.resize((70, 70))
    insect2 = ImageTk.PhotoImage(insect2)
    # insect2_id=canvas.create_image(720, 700, image=insect2, anchor=CENTER)
    
    insect2x = Image.open("./img/insect_ruy2.png")
    insect2x = insect2x.resize((70, 70))
    insect2x = ImageTk.PhotoImage(insect2x)
    insect2s_id=canvas.create_image(638, 10, image=insect2x, anchor=CENTER)
    insect2s_id=canvas.create_image(638, 10, image=insect2x, anchor=CENTER)
    #clock

    # time1 = Image.open("./image/time_add.png")
    # time1 = time1.resize((50, 50))
    # time1 = ImageTk.PhotoImage(time1)
    # time1_id =canvas.create_image(500,-500, image=time1, anchor=CENTER)

    time2 = Image.open("./image/time_add.png")
    time2 = time2.resize((50, 50))
    time2 = ImageTk.PhotoImage(time2)
    time2_id =canvas.create_image(800, -500, image=time2, anchor=CENTER, tags="time")

    def lose_heart():
        canvas.delete(ball3)
    # heart images
    ball_image3 = Image.open("./ninja/heart.png")
    ball_image3 = ball_image3.resize((40, 40))
    ball_image3 = ImageTk.PhotoImage(ball_image3)
    ball3 = canvas.create_image(1280, 50, image=ball_image3, anchor=CENTER)

   
    wall_2 = canvas.create_rectangle(650, 0, 700, app_height, fill='green',tags='wall')
    wall_3 = canvas.create_rectangle(970, 0, 1020, app_height, fill='green',tags='wall')
  
    #button back
    button_back = tk.Button(frame, text='BACK', width=10, height=-20, bg='red', font=('BLOODY TYPE PERSONAL USE', 20), border=10, command=menu)
    button_back.pack()
    button_back.place(x=10, y=10) 
    #button play again
    button_back = tk.Button(frame, text='PLAY AGAIN', width=10, height=-20, bg='red', font=('BLOODY TYPE PERSONAL USE', 20), border=10, command=startGame)
    button_back.pack()
    button_back.place(x=10, y=100) 
    timer_text = canvas.create_text(1240, 100, text='Timer : ' + str(time) + "s", fill='red', font='212BabyGirl 20 bold')
    score_text = canvas.create_text(1180, 150, text=f"Score: {score}", anchor=W, font=("Arail", 20,'bold'),fill='red')
    def stop_and_help():
        stop_sound()
    stop_and_help()
    settime()
    score_game()
    change_bg()
    move_insects()
    move_insects1()
    window.bind("<Key>",key_press)
    window.mainloop()

#menu
def menu():
    global window
    window.destroy()
    window =Tk()
    def play_videos():
        video_path = './image/a.mp4'
        window1_width = app_width
        window1_height = app_height
        playback_fps = 200
        back_to_menu1 = Button(frame, text='BACK', width=5, height=1, bg='red', font=('BLOODY TYPE PERSONAL USE',30), border=2, cursor="spider", command=menu)
        back_to_menu1.place(x=10, y=20)
        play_video(video_path, window1_width, window1_height, playback_fps)

    def help():
        global background1
        help_window = tk.Toplevel(window)
        help_window.title('ab')
        help_window.geometry('2000x1000')

        frame = tk.Frame(help_window, width=2000, height=1000) 
        frame.pack()
        canvas = tk.Canvas(frame, width=2000, height=1000)
        canvas.pack()

        bg_image1 = Image.open("img/help.jpg")
        bg_image1 = bg_image1.resize((1400, 700))
        background1 = ImageTk.PhotoImage(bg_image1)
        canvas.create_image(0, 0, image=background1, anchor=NW)

        button_back = tk.Button(frame, text='BACK', width=10, height=-20, bg='red', font=('BLOODY TYPE PERSONAL USE', 20), border=10, command=help_window.destroy)
        button_back.pack()
        button_back.place(x=0, y=0)
    frame =Frame(window,width=1500,height=1000)
    frame.pack()
    canvas =Canvas(frame,width=1500,height=800)
    canvas.pack()
    bg_image = Image.open("img/bg.jpeg")
    bg_image = bg_image.resize((1700, 800))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)

   
    button_help = Button(frame, text='HELP!', width=10, height=-20,bg='red',font=('BLOODY TYPE PERSONAL USE',50),border=10,command=help)
 
    button_help.place(x=300,y=100)

    button_storygame = Button(frame, text='STORY GAME', width=10, height=-20,bg='red',font=('BLOODY TYPE PERSONAL USE',50),border=10,cursor="spider",command=play_videos)
    button_storygame.place(x=300,y=300)

    button_startgame = Button(frame, text='START GAME', width=10, height=-20,bg='red',font=('BLOODY TYPE PERSONAL USE',50),border=10,command=startGame)
    button_startgame.place(x=300,y=500)
    canvas.pack(expand=True, fill='both')
    frame.pack(expand=True, fill='both')
    sound_menu()
    # sound_menu_auto()
    window.mainloop()
def exitGame():
    window.quit() 
splash_window.after(5600, main)
sound_start()
splash_window.mainloop()