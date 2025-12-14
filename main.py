import pygame
from pygame import mixer

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
black_2 = (30, 30, 30)
black_3 = (15, 15, 15)
light_black_2 = (60, 60, 60)
light_black_3 = (40, 40, 40)
light_black = (30, 30, 30)
dark_gray = (100, 100, 100)
gray = (127, 127, 127)
thistle = (216, 191, 216)
light_gray = (210, 210, 210)
light_gray_2 = (170, 170, 170)
red = (230, 0, 0)
yellow = (255, 215, 70)

# Screen setup
screen = pygame.display.set_mode((1300, 620))
pygame.display.set_caption("KEYBOARD MAESTRO")
icon = pygame.image.load('images\pianologo.jpg')
pygame.display.set_icon(icon)

# Key mappings
KEYBOARD_KEYS = {
    pygame.K_TAB: ('C', 2), pygame.K_1: ('C#', 2), pygame.K_q: ('D', 2), pygame.K_2: ('Eb', 2),
    pygame.K_w: ('E', 2), pygame.K_e: ('F', 2), pygame.K_4: ('F#', 2), pygame.K_r: ('G', 2),
    pygame.K_5: ('G#', 2), pygame.K_t: ('A', 2), pygame.K_6: ('Bb', 2), pygame.K_y: ('B', 2),
    pygame.K_u: ('C', 3), pygame.K_8: ('C#', 3), pygame.K_i: ('D', 3), pygame.K_9: ('Eb', 3),
    pygame.K_o: ('E', 3), pygame.K_p: ('F', 3), pygame.K_MINUS: ('F#', 3), pygame.K_LEFTBRACKET: ('G', 3),
    pygame.K_EQUALS: ('G#', 3), pygame.K_RIGHTBRACKET: ('A', 3), pygame.K_BACKSPACE: ('Bb', 3), pygame.K_BACKSLASH: ('B', 3),
    pygame.K_z: ('C', 4), pygame.K_s: ('C#', 4), pygame.K_x: ('D', 4), pygame.K_d: ('Eb', 4),
    pygame.K_c: ('E', 4), pygame.K_v: ('F', 4), pygame.K_g: ('F#', 4), pygame.K_b: ('G', 4),
    pygame.K_h: ('G#', 4), pygame.K_n: ('A', 4), pygame.K_j: ('Bb', 4), pygame.K_m: ('B', 4),
    pygame.K_COMMA: ('C', 5)
}

# Mouse click regions for white keys (x_min, x_max): note, octave
WHITE_KEY_REGIONS = [
    ((57, 88), 'C', 1), ((90, 121), 'D', 1), ((123, 154), 'E', 1), ((156, 187), 'F', 1),
    ((189, 220), 'G', 1), ((222, 253), 'A', 1), ((255, 286), 'B', 1),
    ((288, 319), 'C', 2), ((321, 352), 'D', 2), ((354, 385), 'E', 2), ((387, 418), 'F', 2),
    ((420, 451), 'G', 2), ((453, 484), 'A', 2), ((486, 517), 'B', 2),
    ((519, 550), 'C', 3), ((552, 583), 'D', 3), ((585, 616), 'E', 3), ((618, 649), 'F', 3),
    ((651, 682), 'G', 3), ((684, 715), 'A', 3), ((717, 748), 'B', 3),
    ((750, 781), 'C', 4), ((783, 814), 'D', 4), ((816, 847), 'E', 4), ((849, 880), 'F', 4),
    ((882, 913), 'G', 4), ((915, 946), 'A', 4), ((948, 979), 'B', 4),
    ((981, 1012), 'C', 5), ((1014, 1045), 'D', 5), ((1047, 1078), 'E', 5), ((1080, 1111), 'F', 5),
    ((1113, 1144), 'G', 5), ((1146, 1177), 'A', 5), ((1179, 1210), 'B', 5),
    ((1213, 1243), 'C', 6)
]

# Mouse click regions for black keys (x_min, x_max): note, octave
BLACK_KEY_REGIONS = [
    ((78, 94), 'C#', 1), ((117, 133), 'Eb', 1), ((177, 193), 'F#', 1), ((214, 230), 'G#', 1), ((249, 265), 'Bb', 1),
    ((309, 325), 'C#', 2), ((348, 364), 'Eb', 2), ((408, 424), 'F#', 2), ((445, 461), 'G#', 2), ((480, 496), 'Bb', 2),
    ((540, 556), 'C#', 3), ((579, 595), 'Eb', 3), ((639, 655), 'F#', 3), ((676, 692), 'G#', 3), ((711, 727), 'Bb', 3),
    ((771, 787), 'C#', 4), ((810, 826), 'Eb', 4), ((870, 886), 'F#', 4), ((907, 923), 'G#', 4), ((941, 958), 'Bb', 4),
    ((1002, 1018), 'C#', 5), ((1041, 1057), 'Eb', 5), ((1101, 1117), 'F#', 5), ((1138, 1154), 'G#', 5), ((1173, 1189), 'Bb', 5)
]

# White key positions for drawing
WHITE_KEY_POSITIONS = {
    ('C', 1): 57, ('D', 1): 90, ('E', 1): 123, ('F', 1): 156, ('G', 1): 189, ('A', 1): 222, ('B', 1): 255,
    ('C', 2): 288, ('D', 2): 321, ('E', 2): 354, ('F', 2): 387, ('G', 2): 420, ('A', 2): 453, ('B', 2): 486,
    ('C', 3): 519, ('D', 3): 552, ('E', 3): 585, ('F', 3): 618, ('G', 3): 651, ('A', 3): 684, ('B', 3): 717,
    ('C', 4): 750, ('D', 4): 783, ('E', 4): 816, ('F', 4): 849, ('G', 4): 882, ('A', 4): 915, ('B', 4): 948,
    ('C', 5): 981, ('D', 5): 1014, ('E', 5): 1047, ('F', 5): 1080, ('G', 5): 1113, ('A', 5): 1146, ('B', 5): 1179,
    ('C', 6): 1212
}

# Black key positions for drawing
BLACK_KEY_POSITIONS = {
    ('C#', 1): 76, ('Eb', 1): 115, ('F#', 1): 175, ('G#', 1): 212, ('Bb', 1): 247,
    ('C#', 2): 307, ('Eb', 2): 346, ('F#', 2): 406, ('G#', 2): 443, ('Bb', 2): 478,
    ('C#', 3): 538, ('Eb', 3): 577, ('F#', 3): 637, ('G#', 3): 674, ('Bb', 3): 709,
    ('C#', 4): 769, ('Eb', 4): 808, ('F#', 4): 868, ('G#', 4): 905, ('Bb', 4): 940,
    ('C#', 5): 1000, ('Eb', 5): 1039, ('F#', 5): 1099, ('G#', 5): 1136, ('Bb', 5): 1171
}


def Keyboard_body():
    pygame.draw.rect(screen, light_black, (13, 97, 1280, 460))
    pygame.draw.rect(screen, light_black_3, (10, 100, 1280, 460))
    pygame.draw.rect(screen, light_black_2, (10, 100, 1280, 190))
    pygame.draw.rect(screen, light_black_2, (10, 320, 45, 220), 0, 0, 0, 0, 3, 2)
    pygame.draw.rect(screen, light_black_2, (1245, 320, 45, 220), 0, 0, 0, 0, 2, 3)
    pygame.draw.rect(screen, black, (55, 320, 1190, 220))
    
    # White keys
    X = 57
    for i in range(36):
        pygame.draw.rect(screen, white, (X, 335, 31, 205), 0, 4, 0, 0, -1, -1)
        X += 33
    
    # Black keys
    X = 78
    for i in range(5):
        for j in range(2):
            pygame.draw.rect(screen, black, (X - 2, 335, 20, 130))
            pygame.draw.rect(screen, black_2, (X, 336, 16, 125), 0)
            X += 35
        X += 28
        for j in range(3):
            pygame.draw.rect(screen, black, (X - 2, 335, 20, 130))
            pygame.draw.rect(screen, black_2, (X, 336, 16, 125), 0)
            X += 35
        X += 28
    
    # Speaker body (left)
    x = 190
    Y = 120
    y = 0.1
    pygame.draw.rect(screen, light_black, (30, 120, 160, 121), 0)
    while Y < 235:
        for i in range(5):
            pygame.draw.line(screen, light_black, (x, Y), (x, 240), 1)
            x += 1
            Y += y
        y += 0.3
    
    # Speaker body (right)
    x = 1110
    Y = 120
    y = 0.1
    pygame.draw.rect(screen, light_black, (1110, 120, 160, 121), 0)
    while Y < 235:
        for i in range(5):
            pygame.draw.line(screen, light_black, (x, Y), (x, 240), 1)
            x -= 1
            Y += y
        y += 0.3
    
    # Display Screen
    pygame.draw.rect(screen, dark_gray, (500, 130, 300, 130), 0)
    pygame.draw.rect(screen, black, (510, 140, 280, 110), 0)
    pygame.draw.rect(screen, white, (530, 150, 240, 90), 0)
    pygame.draw.rect(screen, light_gray, (536, 156, 228, 78), 0)
    pygame.draw.polygon(screen, dark_gray, ((530, 150), (536, 156), (536, 234), (530, 240)))
    pygame.draw.polygon(screen, dark_gray, ((770, 150), (765, 155), (765, 235), (770, 240)))
    pygame.draw.polygon(screen, dark_gray, ((530, 150), (532, 152), (768, 152), (770, 150)))
    pygame.draw.polygon(screen, dark_gray, ((530, 240), (533, 237), (767, 237), (770, 240)))
    
    # Title
    pygame.draw.polygon(screen, gray, ((335, 30), (435, 30), (435, 90), (335, 90), (294, 77.5), (335, 60), (294, 47.5)), 3)
    pygame.draw.polygon(screen, light_gray, ((335, 30), (435, 30), (435, 90), (335, 90), (295, 77.5), (335, 60), (295, 47.5)))
    pygame.draw.polygon(screen, gray, ((925, 30), (825, 30), (825, 90), (925, 90), (964, 77.5), (925, 60), (964, 47.5)), 3)
    pygame.draw.polygon(screen, light_gray, ((925, 30), (825, 30), (825, 90), (925, 90), (965, 77.5), (925, 60), (965, 47.5)))
    pygame.draw.rect(screen, gray, (394, 4, 472, 67))
    pygame.draw.rect(screen, light_gray, (395, 5, 470, 65))
    pygame.draw.polygon(screen, gray, ((395, 70), (435, 90), (435, 70)))
    pygame.draw.polygon(screen, gray, ((865, 70), (825, 90), (825, 70)))
    
    Title_font = pygame.font.SysFont("Arial", 62)
    Title_font.set_underline(True)
    Title = Title_font.render("Keyboard  Maestro", True, black)
    screen.blit(Title, (417, -6))
    
    # Home Button
    pygame.draw.rect(screen, black, (1187, 567, 110, 50))
    pygame.draw.rect(screen, thistle, (1190, 570, 104, 44))
    home_font = pygame.font.SysFont("freesansbold", 44)
    home = home_font.render("Home", True, black)
    screen.blit(home, (1204, 578))


def Voice(Voice_btn, Voice_No):
    pygame.draw.rect(screen, black, (877, 197, 36, 36), 0)
    pygame.draw.rect(screen, light_gray, (880, 200, 30, 30), 0)
    Minus_font = pygame.font.SysFont('freesansbold.ttf', 55, bold=True)
    Display_Minus = Minus_font.render('-', True, black)
    screen.blit(Display_Minus, (888, 195))
    
    pygame.draw.rect(screen, light_gray, (927, 197, 36, 36), 0)
    pygame.draw.rect(screen, black, (930, 200, 30, 30), 0)
    Plus_Font = pygame.font.SysFont('freesansbold.ttf', 50, bold=False)
    Display_Plus = Plus_Font.render('+', True, white)
    screen.blit(Display_Plus, (935, 195))
    
    pygame.draw.rect(screen, light_gray, (877, 137, 96, 41), 0)
    pygame.draw.rect(screen, black, (880, 140, 90, 35), 0)
    
    voice_font = pygame.font.SysFont('freesansbold.ttf', 32)
    voice_color = red if Voice_btn else white
    voice = voice_font.render("Voice", True, voice_color)
    screen.blit(voice, (895, 148))
    
    display_font = pygame.font.SysFont('freesansbold.ttf', 28)
    voice_texts = {1: "1. PIANO", 2: "2. SAXOPHONE", 3: "3. VIOLIN"}
    display_voice = display_font.render(voice_texts.get(Voice_No, " "), True, red)
    screen.blit(display_voice, (540, 158))


def Show_Notes(Show_note):
    pygame.draw.rect(screen, dark_gray, (277, 137, 76, 36), 0, 18, -1, -1, -1, -1)
    pygame.draw.rect(screen, light_black, (280, 140, 70, 30), 0, 15, -1, -1, -1, -1)
    
    notes_font = pygame.font.SysFont("freesansbold", 22)
    notes_color = red if Show_note else white
    notes = notes_font.render("NOTES", True, notes_color)
    screen.blit(notes, (290, 149))
    
    if Show_note:
        Note_Font = pygame.font.SysFont('freesansbold', 20)
        No_Font = pygame.font.SysFont('freesandbold', 15)
        Notes = "CDEFGAB"
        x = 66
        for i in range(1, 6):
            for ch in Notes:
                Note = Note_Font.render(ch, True, black)
                screen.blit(Note, (x, 472))
                No = No_Font.render(str(i), True, black)
                screen.blit(No, (x + 10, 477))
                x += 33
        Note = Note_Font.render("C", True, black)
        screen.blit(Note, (x, 472))
        No = No_Font.render('6', True, black)
        screen.blit(No, (x + 10, 477))
        
        SNote_Font = pygame.font.SysFont('Arial)', 12)
        X = 80
        for i in range(1, 6):
            sharp = SNote_Font.render("C#", True, white)
            screen.blit(sharp, (X, 340))
            flat = SNote_Font.render('Db', True, white)
            screen.blit(flat, (X, 370))
            X += 38
            sharp = SNote_Font.render("D#", True, white)
            screen.blit(sharp, (X, 340))
            flat = SNote_Font.render('Eb', True, white)
            screen.blit(flat, (X, 370))
            X += 61
            sharp = SNote_Font.render("F#", True, white)
            screen.blit(sharp, (X, 340))
            flat = SNote_Font.render('Gb', True, white)
            screen.blit(flat, (X-1, 370))
            X += 36
            sharp = SNote_Font.render("G#", True, white)
            screen.blit(sharp, (X, 340))
            flat = SNote_Font.render('Ab', True, white)
            screen.blit(flat, (X, 370))
            X += 35
            sharp = SNote_Font.render("A#", True, white)
            screen.blit(sharp, (X, 340))
            flat = SNote_Font.render('Bb', True, white)
            screen.blit(flat, (X, 370))
            X += 61


def Show_Keys(Show_key):
    pygame.draw.rect(screen, dark_gray, (377, 137, 76, 36), 0, 18, -1, -1, -1, -1)
    pygame.draw.rect(screen, light_black, (380, 140, 70, 30), 0, 15, -1, -1, -1, -1)
    
    notes_font = pygame.font.SysFont("freesansbold", 22)
    notes_color = red if Show_key else white
    notes = notes_font.render("KEYS", True, notes_color)
    screen.blit(notes, (395, 149))
    
    if Show_key:
        Key_Font = pygame.font.SysFont('freesansbold.ttf', 24)
        Key_list = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', ' [', ' ]', ' \\', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ,']
        x = 290
        key = Key_Font.render("Tab", True, black)
        screen.blit(key, (x, 510))
        x += 40
        for ele in Key_list:
            Key = Key_Font.render(ele, True, black)
            screen.blit(Key, (x, 510))
            x += 33
        
        Key_Font = pygame.font.SysFont('freesansbold.ttf', 18)
        Key_list = ['1','2','4','5','6','8','9','-','=','<-','S','D','G','H','J']
        x = 314
        ind=0
        for i in range(3):
            key = Key_Font.render(Key_list[ind], True, white)
            screen.blit(key, (x, 430))
            ind+=1
            x += 38
            key = Key_Font.render(Key_list[ind], True, white)
            screen.blit(key, (x, 430))
            ind+=1
            x += 61
            key = Key_Font.render(Key_list[ind], True, white)
            screen.blit(key, (x, 430))
            ind+=1
            x += 37
            key = Key_Font.render(Key_list[ind], True, white)
            screen.blit(key, (x, 430))
            ind+=1
            x += 34
            key = Key_Font.render(Key_list[ind], True, white)
            screen.blit(key, (x, 430))
            ind+=1
            x += 61-(i==1)


def play_sound(note, octave, voice_no):
    voice_names = {1: "Piano", 2: "Saxophone", 3: "Violin"}
    filename = f"sounds\{voice_names[voice_no]}\{voice_names[voice_no]}{note}{octave}.wav"
    sound = mixer.Sound(filename)
    loops = 0 if voice_no == 1 else -1
    sound.play(loops)
    return sound


def Main_Keyboard():
    note_font = pygame.font.SysFont('freesandbold.ttf', 60)
    note_name = " C3"
    
    pressed_keys = {}
    active_sounds = {}
    Voice_btn = False
    Show_note = False
    Show_key = True
    Voice_No = 1
    
    while True:
        screen.fill(yellow)
        Keyboard_body()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN and event.key in KEYBOARD_KEYS:
                note, octave = KEYBOARD_KEYS[event.key]
                note_name = f"{note:>3}{octave}"
                pressed_keys[(note, octave)] = True
                active_sounds[(note, octave)] = play_sound(note, octave, Voice_No)
            
            if event.type == pygame.KEYUP and event.key in KEYBOARD_KEYS:
                note, octave = KEYBOARD_KEYS[event.key]
                pressed_keys[(note, octave)] = False
                if (note, octave) in active_sounds:
                    active_sounds[(note, octave)].fadeout(800)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                A, B = pygame.mouse.get_pos()
                
                if 1190 < A < 1294 and 570 < B < 614:
                    return
                
                key_clicked = False
                
                # Check black keys first (they're on top)
                if 336 < B < 461:
                    for (x_range, note, octave) in BLACK_KEY_REGIONS:
                        if x_range[0] < A < x_range[1]:
                            note_name = f"{note:>3}{octave}"
                            pressed_keys[(note, octave)] = True
                            active_sounds[(note, octave)] = play_sound(note, octave, Voice_No)
                            key_clicked = True
                            break
                
                # Check white keys
                if not key_clicked and 335 < B < 540:
                    for (x_range, note, octave) in WHITE_KEY_REGIONS:
                        if x_range[0] < A < x_range[1]:
                            note_name = f"{note:>3}{octave}"
                            pressed_keys[(note, octave)] = True
                            active_sounds[(note, octave)] = play_sound(note, octave, Voice_No)
                            break
                
                if 282 < A < 348 and 142 < B < 168:
                    Show_note = not Show_note
                if 382 < A < 448 and 142 < B < 168:
                    Show_key = not Show_key
                if 880 < A < 970 and 140 < B < 175:
                    Voice_btn = not Voice_btn
                
                if Voice_btn and 200 < B < 230:
                    if 880 < A < 910:
                        Voice_No = 3 if Voice_No == 1 else Voice_No - 1
                    elif 930 < A < 960:
                        Voice_No = 1 if Voice_No == 3 else Voice_No + 1
            
            if event.type == pygame.MOUSEBUTTONUP:
                pressed_keys.clear()
                pygame.mixer.fadeout(800)
        
        # Draw white keys
        for (note, octave), x_pos in WHITE_KEY_POSITIONS.items():
            color = light_gray if pressed_keys.get((note, octave), False) else white
            pygame.draw.rect(screen, color, (x_pos, 335, 31, 205), 0, 4, 0, 0, -1, -1)
        
        # Draw black keys
        for (note, octave), x_pos in BLACK_KEY_POSITIONS.items():
            if pressed_keys.get((note, octave), False):
                pygame.draw.rect(screen, light_black, (x_pos, 335, 20, 130))
            else:
                pygame.draw.rect(screen, black, (x_pos, 335, 20, 130))
                pygame.draw.rect(screen, black_2, (x_pos+2, 336, 16, 125), 0)
        
        Voice(Voice_btn, Voice_No)
        Show_Notes(Show_note)
        Show_Keys(Show_key)
        
        notation = note_font.render(str(note_name), True, black)
        screen.blit(notation, (610, 182))
        
        pygame.display.update()


def HOME():
    while True:
        screen.fill(yellow)
        pygame.draw.rect(screen, black, (100, 80, 1050, 300))
        background = pygame.image.load('images\piano bg.jpg')
        background.set_alpha(150)
        screen.blit(background, (30, 0))
        
        Name_font = pygame.font.SysFont("constantia", 130)
        Name_font.set_underline(True)
        Name_btn = Name_font.render("KEYBOARD", True, white)
        screen.blit(Name_btn, (300, 100))
        Name_btn = Name_font.render("MAESTRO", True, white)
        screen.blit(Name_btn, (335, 230))
        
        pygame.draw.rect(screen, black, (246, 446, 258, 83))
        pygame.draw.rect(screen, thistle, (250, 450, 250, 75))
        play_font = pygame.font.SysFont("freesansbold.ttf", 75)
        play_btn = play_font.render("PLAY", True, light_black)
        screen.blit(play_btn, (312, 465))
        
        pygame.draw.rect(screen, black, (696, 446, 258, 83))
        pygame.draw.rect(screen, thistle, (700, 450, 250, 75))
        exit_font = pygame.font.SysFont("freesansbold.ttf", 75)
        exit_btn = exit_font.render("EXIT", True, light_black)
        screen.blit(exit_btn, (765, 465))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                A, B = pygame.mouse.get_pos()
                if 250 < A < 500 and 450 < B < 525:
                    pygame.mouse.set_pos(0, 0)
                    Main_Keyboard()
                elif 700 < A < 950 and 450 < B < 525:
                    pygame.quit()
                    return
        
        pygame.display.update()


if __name__ == "__main__":
    HOME()