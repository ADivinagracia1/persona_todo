# play aroun with libraries
# note down what kinds of libraries

from winotify import Notification

toast = Notification(app_id="this is the app ID",
                     title="This is the title",
                     msg="this is where a the description could be",
                     icon=r"C:\_projects\persona_todo\scrap_code\pics\yoshida.PNG", # must be absolute path
                     duration="long")

toast.add_actions(label="Go To Link", 
                  launch="https://github.com/versa-syahptr/winotify/")

toast.add_actions(label="Go To YouTube", 
                  launch="https://www.youtube.com/")

toast.show()

