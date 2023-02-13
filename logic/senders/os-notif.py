# send notifications

from winotify import Notification

TRELLO_LINK = "https://trello.com/b/HhO71Prd/tesla"
P5_HEADER = "Task Reminder!"
ICON_LINK = r"C:\_projects\persona_todo\scrap_code\pics\yoshida.PNG"
CONFIDANT = "Josh"


def setup_os_notif(notif_header, task_name, task_desc, task_icon = None, notif_dur = "short"):
                                                                        # Note: "short", or "long"
    toast = Notification(app_id=notif_header,
                        title=task_name,
                        msg=task_desc,
                        icon=task_icon,  # must be absolute path
                        duration=notif_dur)

    return toast
    
def add_button(toast, button_label, button_link):
    toast.add_actions(label=button_label, launch=button_link)

def send_notif(toast):
    toast.show()









# Testing this wrapper
w10_notif = setup_os_notif( notif_header=P5_HEADER, 
            task_name="Do your work!",
            task_desc=f"Finish the list of items {CONFIDANT} gave you!",
            task_icon=ICON_LINK
            )

add_button(w10_notif, button_label="Check tasks", button_link=TRELLO_LINK)
add_button(w10_notif, button_label="Or don't...", button_link="https://www.youtube.com/")
send_notif(w10_notif)

