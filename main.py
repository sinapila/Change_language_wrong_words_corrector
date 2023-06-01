import keyboard 

# get datas
persian_words = open("pe.txt","r+")
english_words = open("en.txt","r+")
now_text = ""

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def action():
    """
    this function should replace wrong word to Ok
    """
    pass

def check(now_text):
    """
    this function check and find wrong word
    """
    for i in persian_words:
        d = { "i": "ه", "dog": "pig"}
        replace_all(i, d)
        if now_text == i:
            action()

def callback(event):
    """
    this function get keybord events
    """
    global now_text
    name = event.name      
    if len(name) == 1:
        now_text += name
    else:
        now_text = ""
    print(now_text)
    if len(now_text) > 2:
        check(now_text)

keyboard.on_release(callback=callback)
keyboard.wait()
