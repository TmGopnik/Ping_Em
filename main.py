from tkinter import *
import urllib.request
import urllib.parse
global site_entry, canvas1

# Tkinter Window Setup Continues line 59
root = Tk()
root.geometry("626x500")
root.title("Ping Em")
photo = PhotoImage(file="icons/ping_pong_icon.png")
root.iconphoto(False, photo)


# Faking browser agent [to prevent 403 errors]
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def ping_website():
    global canvas1, site_entry
    website = site_entry.get()
    try:
        # Secure Connection Attempt at URL
        url = 'https://www.' + website
        opener = AppURLopener()
        opener.open(url)

        # Displaying Result
        site_entry.destroy()
        site_entry = Entry(bg="#252424", fg="white")
        ping_message_pinged = Label(text=website + " Is Online!", bg="#252424", fg="green")
        canvas1.create_window(206, 256, anchor="nw", window=site_entry, width=230)
        canvas1.create_window(206, 306, anchor="nw", window=ping_message_pinged, width=230)
    except:
        try:
            # Insecure attempt at connection [Only tried if https fails]
            url = 'http://www.' + website
            opener = AppURLopener()
            opener.open(url)

            # Displaying Result
            site_entry.destroy()
            site_entry = Entry(bg="#252424", fg="white")
            ping_message_pinged = Label(text=website + " Is Online!", bg="#252424", fg="green")
            canvas1.create_window(206, 256, anchor="nw", window=site_entry, width=230)
            canvas1.create_window(206, 306, anchor="nw", window=ping_message_pinged, width=230)
        except:
            # Displaying Result of Not Active
            ping_message_pinged = Label(text=website + " Is Offline!", bg="#252424", fg="red")
            canvas1.create_window(206, 256, anchor="nw", window=site_entry, width=230)
            canvas1.create_window(206, 306, anchor="nw", window=ping_message_pinged, width=230)
            site_entry.destroy()
            site_entry = Entry(bg="#252424", fg="white")
            canvas1.create_window(206, 256, anchor="nw", window=site_entry, width=230)
            pass

# The Main Window
def start_box():
    global site_entry, canvas1
    bg = PhotoImage(file="icons/main_screen.png")  # Add image file
    canvas1 = Canvas(root, width=500, height=500)  # Create Canvas
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=bg, anchor="nw")  # Display image
    site_entry = Entry(bg="#252424", fg="white")
    ping_button = Button(bg="#252424", fg="white", text="Ping!", font="Helvetica 10 bold", command=ping_website)
    entry_site_canvas = canvas1.create_window(206, 256, anchor="nw", window=site_entry, width=230)
    button_canvas = canvas1.create_window(462, 243, anchor="nw", window=ping_button, width=50,height=35)
    mainloop()


if __name__ == '__main__':
    start_box()


