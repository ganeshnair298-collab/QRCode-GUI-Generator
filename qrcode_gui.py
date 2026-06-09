from customtkinter import *
from PIL import Image
from PIL import ImageColor
import traceback
import qrcode
import os
import sys
from pyzbar.pyzbar import decode
from tkinter import filedialog
import webbrowser
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import *
from qrcode.image.styles.colormasks import *

# variable core function
title = "QR Code gui generator"
geometry = "800x600"
is_qrcode_round = False
is_qrcode_gap_square_shape = False
is_qrcode_round_corner = False
is_qrcode_horizontal_code = False
is_qrcode_vertical_code = False
image_on_qrcode = None
front_color_qrcode = ImageColor.getrgb("black")  # for qrcode
back_color_qrcode = ImageColor.getrgb("white")  # for qrcode

#resource manager for assets
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# app config code here
app = CTk()
app.title(title)
app.after(200, lambda: app.iconbitmap(resource_path("assets/favicon.ico")))
app._set_appearance_mode("dark")
app.geometry(geometry)

# App layout grid configure code here
app.grid_columnconfigure(0, weight=8)
app.grid_columnconfigure(1, weight=2)
app.grid_rowconfigure(0, weight=0)
app.grid_rowconfigure(1, weight=1)

# toolbár layout cođe here
toolbar_frame = CTkFrame(app, height=80, fg_color="black", corner_radius=0)
toolbar_frame.grid(column=0, row=0, sticky="new", columnspan=9)


# toolbar layout grid configure layout
toolbar_frame.grid_columnconfigure(0, weight=1)
toolbar_frame.grid_columnconfigure(1, weight=1)
toolbar_frame.grid_rowconfigure(0, weight=1)

# toolbar title name layout code here
toolbar_frame_title = CTkLabel(
    toolbar_frame, text=title, font=("Arial", 25), text_color="white"
)
toolbar_frame_title.grid(padx=20, pady=20, column=0, row=0, sticky="nsw")

# qrcode image framework code here
qrcode_img_frame = CTkFrame(app)
qrcode_img_frame.grid(padx=20, pady=20, column=0, row=1, sticky="nsew")

# qrcode img frame grid configuration code
qrcode_img_frame.grid_columnconfigure(0, weight=1)
qrcode_img_frame.grid_rowconfigure(0, weight=1)
qrcode_img_frame.grid_rowconfigure(1, weight=1)
qrcode_img_frame.grid_rowconfigure(2, weight=1)
qrcode_img_frame.grid_rowconfigure(3, weight=1)

# filling detail frame code
filling_img_frame = CTkFrame(app)
filling_img_frame.grid(padx=20, pady=20, column=1, row=1, sticky="nsew")

# filling detail frame grid config code here
filling_img_frame.grid_columnconfigure(0, weight=1)
filling_img_frame.grid_rowconfigure(0, weight=0)
filling_img_frame.grid_rowconfigure(1, weight=1)


# generate qrcode function code here
def generate_qr(event=None):
    try:
        global is_qrcode_round, is_qrcode_gap_square_shape, is_qrcode_round_corner, is_qrcode_horizontal_code, image_on_qrcode
        global is_qrcode_vertical_code
        global front_color_qrcode, back_color_qrcode
        data = txt_filling.get("1.0", "end-1c").strip()
        qr_data = qrcode.QRCode(
            version=1, box_size=10, border=4, error_correction=qrcode.ERROR_CORRECT_H
        )
        qr_data.add_data(data)
        qr_data.make(fit=True)

        if is_qrcode_round == True:
            print(image_on_qrcode)
            pil_img = qr_data.make_image(
                image_factory=StyledPilImage,
                module_drawer=CircleModuleDrawer(),
                color_mask=SolidFillColorMask(
                    front_color=front_color_qrcode, back_color=back_color_qrcode
                ),
                embedded_image_path=image_on_qrcode,
            )._img
            qr_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(250, 250))

            qrcode_img = CTkLabel(qrcode_img_frame, image=qr_img, text="")
            qrcode_img.grid(padx=20, pady=(20, 10), column=0, row=0, sticky="ew")
        elif is_qrcode_gap_square_shape == True:
            pil_img = qr_data.make_image(
                image_factory=StyledPilImage,
                module_drawer=GappedSquareModuleDrawer(size_ratio=0.8),
                color_mask=SolidFillColorMask(
                    front_color=front_color_qrcode, back_color=back_color_qrcode
                ),
                embedded_image_path=image_on_qrcode,
            )._img
            qr_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(250, 250))

            qrcode_img = CTkLabel(qrcode_img_frame, image=qr_img, text="")
            qrcode_img.grid(padx=20, pady=(20, 10), column=0, row=0, sticky="ew")

        elif is_qrcode_round_corner == True:
            pil_img = qr_data.make_image(
                image_factory=StyledPilImage,
                module_drawer=RoundedModuleDrawer(),
                color_mask=SolidFillColorMask(
                    front_color=front_color_qrcode, back_color=back_color_qrcode
                ),
                embedded_image_path=image_on_qrcode,
            )._img
            qr_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(250, 250))

            qrcode_img = CTkLabel(qrcode_img_frame, image=qr_img, text="")
            qrcode_img.grid(padx=20, pady=(20, 10), column=0, row=0, sticky="ew")

        elif is_qrcode_horizontal_code == True:
            pil_img = qr_data.make_image(
                image_factory=StyledPilImage,
                module_drawer=HorizontalBarsDrawer(),
                color_mask=SolidFillColorMask(
                    front_color=front_color_qrcode, back_color=back_color_qrcode
                ),
                embedded_image_path=image_on_qrcode,
            )._img
            qr_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(250, 250))

            qrcode_img = CTkLabel(qrcode_img_frame, image=qr_img, text="")
            qrcode_img.grid(padx=20, pady=(20, 10), column=0, row=0, sticky="ew")

        elif is_qrcode_vertical_code == True:
            pil_img = qr_data.make_image(
                image_factory=StyledPilImage,
                module_drawer=VerticalBarsDrawer(),
                color_mask=SolidFillColorMask(
                    front_color=front_color_qrcode, back_color=back_color_qrcode
                ),
                embedded_image_path=image_on_qrcode,
            )._img
            qr_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(250, 250))

            qrcode_img = CTkLabel(qrcode_img_frame, image=qr_img, text="")
            qrcode_img.grid(padx=20, pady=(20, 10), column=0, row=0, sticky="ew")
        else:

            print(image_on_qrcode)
            pil_img = qr_data.make_image(
                image_factory=StyledPilImage,  # ← required
                fill_color=front_color_qrcode,
                back_color=back_color_qrcode,
                embedded_image_path=image_on_qrcode,
            )._img

            qr_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(250, 250))

            qrcode_img = CTkLabel(qrcode_img_frame, image=qr_img, text="")
            qrcode_img.grid(padx=20, pady=(20, 10), column=0, row=0, sticky="ew")

    except ValueError as e:
        custom_dialog(
            "Content data is too huge",
            f"content is too large to fit in qrcode. Aborting it \n Error: {e}",
        )
    except Exception as e:
        g = traceback.format_exc()
        custom_dialog("Oopsie", f"{e} and {g}")


# change qr design style
def change_style(choice):
    global is_qrcode_round, is_qrcode_gap_square_shape, front_color_qrcode, back_color_qrcode, is_qrcode_round_corner, is_qrcode_horizontal_code, is_qrcode_vertical_code

    data = txt_filling.get("1.0", "end-1c").strip()
    qr_data = qrcode.QRCode(
        version=1, box_size=10, border=4, error_correction=qrcode.ERROR_CORRECT_H
    )
    qr_data.add_data(data)
    qr_data.make(fit=True)

    if choice == "Square boring lines":
        pil_img = qr_data.make_image(
            fill_color=front_color_qrcode,
            back_color=back_color_qrcode,
            embedded_image_path=image_on_qrcode,
        )._img
        qr_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(250, 250))

        qrcode_img = CTkLabel(qrcode_img_frame, image=qr_img, text="")
        qrcode_img.grid(padx=20, pady=(20, 10), column=0, row=0, sticky="ew")
        is_qrcode_round = False
        is_qrcode_gap_square_shape = False
        is_qrcode_round = False
        is_qrcode_gap_square_shape = False
        is_qrcode_round_corner = False
        is_qrcode_horizontal_code = False
        is_qrcode_vertical_code = False

    elif choice == "Circle dot modern":
        pil_img = qr_data.make_image(
            image_factory=StyledPilImage,
            module_drawer=CircleModuleDrawer(),
            color_mask=SolidFillColorMask(
                front_color=front_color_qrcode, back_color=back_color_qrcode
            ),
            embedded_image_path=image_on_qrcode,
        )._img

        qr_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(250, 250))

        qrcode_img = CTkLabel(qrcode_img_frame, image=qr_img, text="")
        qrcode_img.grid(padx=20, pady=(20, 10), column=0, row=0, sticky="ew")

        is_qrcode_round = False
        is_qrcode_gap_square_shape = False
        is_qrcode_round = True
        is_qrcode_gap_square_shape = False
        is_qrcode_round_corner = False
        is_qrcode_horizontal_code = False
        is_qrcode_vertical_code = False

    elif choice == "Stylish gapped square dot":
        pil_img = qr_data.make_image(
            image_factory=StyledPilImage,
            module_drawer=GappedSquareModuleDrawer(size_ratio=0.8),
            color_mask=SolidFillColorMask(
                front_color=front_color_qrcode, back_color=back_color_qrcode
            ),
            embedded_image_path=image_on_qrcode,
        )._img
        qr_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(250, 250))

        qrcode_img = CTkLabel(qrcode_img_frame, image=qr_img, text="")
        qrcode_img.grid(padx=20, pady=(20, 10), column=0, row=0, sticky="ew")

        is_qrcode_round = False
        is_qrcode_gap_square_shape = False
        is_qrcode_round = False
        is_qrcode_gap_square_shape = True
        is_qrcode_round_corner = False
        is_qrcode_horizontal_code = False
        is_qrcode_vertical_code = False

    elif choice == "Normal shape with rounded edge":
        pil_img = qr_data.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            color_mask=SolidFillColorMask(
                front_color=front_color_qrcode, back_color=back_color_qrcode
            ),
            embedded_image_path=image_on_qrcode,
        )._img
        qr_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(250, 250))

        qrcode_img = CTkLabel(qrcode_img_frame, image=qr_img, text="")
        qrcode_img.grid(padx=20, pady=(20, 10), column=0, row=0, sticky="ew")

        is_qrcode_round = False
        is_qrcode_gap_square_shape = False
        is_qrcode_round = False
        is_qrcode_gap_square_shape = False
        is_qrcode_round_corner = True
        is_qrcode_horizontal_code = False
        is_qrcode_vertical_code = False
        print(is_qrcode_round_corner)
    elif choice == "Horizontal line":
        pil_img = qr_data.make_image(
            image_factory=StyledPilImage,
            module_drawer=HorizontalBarsDrawer(),
            color_mask=SolidFillColorMask(
                front_color=front_color_qrcode, back_color=back_color_qrcode
            ),
            embedded_image_path=image_on_qrcode,
        )._img
        qr_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(250, 250))

        qrcode_img = CTkLabel(qrcode_img_frame, image=qr_img, text="")
        qrcode_img.grid(padx=20, pady=(20, 10), column=0, row=0, sticky="ew")

        is_qrcode_round = False
        is_qrcode_gap_square_shape = False
        is_qrcode_round = False
        is_qrcode_gap_square_shape = False
        is_qrcode_round_corner = False
        is_qrcode_horizontal_code = True
        is_qrcode_vertical_code = False

    elif choice == "Vertical line":
        pil_img = qr_data.make_image(
            image_factory=StyledPilImage,
            module_drawer=VerticalBarsDrawer(),
            color_mask=SolidFillColorMask(
                front_color=front_color_qrcode, back_color=back_color_qrcode
            ),
            embedded_image_path=image_on_qrcode,
        )._img
        qr_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(250, 250))

        qrcode_img = CTkLabel(qrcode_img_frame, image=qr_img, text="")
        qrcode_img.grid(padx=20, pady=(20, 10), column=0, row=0, sticky="ew")

        is_qrcode_round = False
        is_qrcode_gap_square_shape = False
        is_qrcode_round = False
        is_qrcode_gap_square_shape = False
        is_qrcode_round_corner = False
        is_qrcode_horizontal_code = False
        is_qrcode_vertical_code = True


# Advance level qrcode customisation code function
def customise_qrcode():
    app.update()
    popup = CTkToplevel(app)
    popup.title("Customise QRCode")
    popup.geometry("700x400")
    popup.grab_set()
    popup.after(200, lambda: popup.iconbitmap(resource_path("assets/favicon.ico")))
    popup.grid_rowconfigure(0, weight=0)
    popup.grid_columnconfigure(0, weight=0)
    popup.grid_columnconfigure(1, weight=1)
    popup.grid_columnconfigure(2, weight=1)
    popup.grid_rowconfigure(1, weight=0)
    popup.grid_rowconfigure(2, weight=0)
    popup.grid_rowconfigure(3, weight=0)
    popup.grid_rowconfigure(4, weight=1)
    popup.grid_rowconfigure(5, weight=1)

    title_label = CTkFrame(popup, height=80, fg_color="black", corner_radius=0)
    title_label.grid_columnconfigure(1, weight=1)
    title_label.grid(padx=0, pady=0, column=0, row=0, columnspan=4, sticky="new")
    CTkLabel(
        title_label, text="Customise QRCode", text_color="white", font=("Arial", 25)
    ).grid(padx=20, pady=20, column=0, row=1, sticky="nsew")

    CTkLabel(popup, text="QR Code design", font=("Arial", 15)).grid(
        padx=20, pady=(20, 0), column=0, row=1, sticky="nw"
    )

    combo = CTkComboBox(
        popup,
        values=[
            "Square boring lines",
            "Circle dot modern",
            "Stylish gapped square dot",
            "Normal shape with rounded edge",
            "Horizontal line",
            "Vertical line",
        ],
        command=change_style,
    )
    combo.grid(padx=20, pady=(20, 0), column=1, row=1, columnspan=4, sticky="new")

    def color_front(event):
        global front_color_qrcode
        txt = front_entry.get()
        front_color_qrcode = ImageColor.getrgb(txt)
        print(front_color_qrcode)
        generate_qr()

    def color_back(event):
        global back_color_qrcode
        txt5 = back_entry.get()
        if txt5 == "black":
            back_color_qrcode = (1, 1, 1)
        else:
            back_color_qrcode = ImageColor.getrgb(txt5)
        print(back_color_qrcode)
        generate_qr()

    CTkLabel(
        popup, text="QR Code front design color", font=("Arial", 15)
    ).grid(padx=20, pady=(10, 0), column=0, row=2, sticky="nw")

    front_entry = CTkEntry(
        popup,
        placeholder_text="Enter hex color or simple color word such as (red,green,blue)",
    )

    front_entry.grid(padx=20, pady=(10, 0), column=1, row=2, columnspan=4, sticky="new")
    front_entry.bind("<KeyRelease>", color_front)

    CTkLabel(
        popup, text="QR Code back design color", font=("Arial", 15)
    ).grid(padx=20, pady=10, column=0, row=3, sticky="nw")

    back_entry = CTkEntry(
        popup,
        placeholder_text="Enter hex color or simple color word such as (red,green,blue)",
    )
    back_entry.grid(padx=20, pady=(10, 0), column=1, row=3, columnspan=4, sticky="new")
    back_entry.bind("<KeyRelease>", color_back)

    CTkLabel(
        popup, text="QR Code embeded image icon", font=("Arial", 15)
    ).grid(padx=20, pady=0, column=0, row=4, sticky="nw")

    def read_open_file():
        global image_on_qrcode
        file_name = filedialog.askopenfilename(
            title="Select QRCode image", filetypes=[("Image files", "*png *jpg *jpeg")]
        )
        image_on_qrcode = file_name
        btn_entry.configure(text="Image added, now just generate")
        generate_qr()
    
    def remove_open_file():
        global image_on_qrcode
        image_on_qrcode = None
        btn_entry_remove.configure(text="Image removed")
        btn_entry.configure(text="Choose image")
        generate_qr()

    btn_entry = CTkButton(popup, text="Choose image", command=lambda: read_open_file())
    btn_entry.grid(padx=(20,0), pady=0, column=1, row=4, sticky="new")

    btn_entry_remove = CTkButton(popup, text="Remove image", command=lambda: remove_open_file())
    btn_entry_remove.grid(padx=(8,20), pady=0, column=2, row=4, columnspan=4, sticky="new")

    CTkLabel(
        popup, text="QRCode preview cannpt shown here. Please check on main app", font=("Arial", 10)
    ).grid(padx=20, pady=0, column=0, row=5, sticky="nw")

# custom đialog for any purpose
def custom_dialog_read(title, message):
    app.update()
    popup = CTkToplevel(app)
    popup.overrideredirect(True)
    popup.geometry("+300+200")
    popup.after(200, lambda: popup.iconbitmap(resource_path("assets/favicon.ico")))
    popup.grab_set()
    popup.grid_rowconfigure(0, weight=0)
    popup.grid_columnconfigure(0, weight=1)
    popup.grid_rowconfigure(2, weight=1)

    # go browser redirect
    def go_browser(url):
        try:
            webbrowser.open(url)
            btn.configure(text="Redirecting...")
        except Exception as e:
            custom_dialog("Error to redirect", e)

    def move_popup(event):
        if event.type == "4":
            popup.x, popup.y = event.x, event.y
        elif event.type == "6":
            popup.geometry(
                f"+{popup.winfo_x()+(event.x-popup.x)}+{popup.winfo_y()+(event.y-popup.y)}"
            )

    def copy_txt(txt):
        popup.clipboard_clear()
        popup.clipboard_append(txt)
        popup.update()
        btn.configure(text="Copied")

    title_label = CTkFrame(popup, height=35, fg_color="black", corner_radius=0)
    title_label.grid_columnconfigure(1, weight=1)
    title_label.grid(padx=0, pady=0, column=0, row=0, columnspan=4, sticky="new")
    CTkLabel(title_label, text=title, text_color="white").grid(
        padx=10, pady=10, column=0, row=0, sticky="nsew"
    )
    CTkButton(
        title_label,
        width=10,
        text="X",
        text_color="white",
        fg_color="transparent",
        command=popup.destroy,
    ).grid(padx=10, pady=10, column=1, row=0, sticky="nse")
    title_label.bind("<ButtonPress-1>", move_popup)
    title_label.bind("<B1-Motion>", move_popup)

    if message.startswith("http") or message.startswith("https"):
        btn = CTkButton(
            popup,
            text="Go to url",
            command=lambda: go_browser(message),
            fg_color="black",
            hover_color="black",
            corner_radius=50,
        )
        btn.grid(padx=10, pady=10, column=0, row=2, sticky="sew")
    else:
        btn = CTkButton(
            popup,
            text="Copy content",
            command=lambda: copy_txt(message),
            fg_color="black",
            hover_color="black",
            corner_radius=50,
        )
        btn.grid(padx=10, pady=10, column=0, row=2, sticky="sew")

    CTkLabel(popup, text=message, text_color="black").grid(
        padx=10, pady=10, column=0, row=1, sticky="nsew"
    )


# custom dialog for ver 2
def custom_dialog(title, message):
    app.update()
    popup = CTkToplevel(app)
    popup.overrideredirect(True)
    popup.geometry("+300+200")
    popup.grab_set()
    popup.after(200, lambda: popup.iconbitmap(resource_path("assets/favicon.ico")))
    popup.grid_rowconfigure(0, weight=0)
    popup.grid_columnconfigure(0, weight=1)
    popup.grid_rowconfigure(2, weight=1)

    def move_popup(event):
        if event.type == "4":
            popup.x, popup.y = event.x, event.y
        elif event.type == "6":
            popup.geometry(
                f"+{popup.winfo_x()+(event.x-popup.x)}+{popup.winfo_y()+(event.y-popup.y)}"
            )

    title_label = CTkFrame(popup, height=35, fg_color="black", corner_radius=0)
    title_label.grid_columnconfigure(1, weight=1)
    title_label.grid(padx=0, pady=0, column=0, row=0, columnspan=4, sticky="new")
    CTkLabel(title_label, text=title, text_color="white").grid(
        padx=10, pady=10, column=0, row=0, sticky="nsew"
    )
    CTkButton(
        title_label,
        width=10,
        text="X",
        text_color="white",
        fg_color="transparent",
        command=popup.destroy,
    ).grid(padx=10, pady=10, column=1, row=0, sticky="nse")
    title_label.bind("<ButtonPress-1>", move_popup)
    title_label.bind("<B1-Motion>", move_popup)

    CTkButton(
        popup,
        text="OK",
        command=popup.destroy,
        corner_radius=50,
        fg_color="black",
        hover_color="black",
    ).grid(padx=10, pady=10, column=0, row=2, sticky="sew")

    CTkLabel(popup, text=message, text_color="black").grid(
        padx=10, pady=10, column=0, row=1, sticky="nsew"
    )


# saving qrcode image function
def save_qr_code():
    global is_qrcode_round, is_qrcode_gap_square_shape, is_qrcode_round_corner, is_qrcode_horizontal_code
    global is_qrcode_vertical_code
    global front_color_qrcode, back_color_qrcode
    try:
        data = txt_filling.get("1.0", "end-1c").strip()
        qr_data = qrcode.QRCode(
            version=None, box_size=10, border=4, error_correction=qrcode.ERROR_CORRECT_H
        )
        qr_data.add_data(data)
        qr_data.make(fit=False)

        if is_qrcode_round == True:
            pil_img = qr_data.make_image(
                image_factory=StyledPilImage,
                module_drawer=CircleModuleDrawer(),
                color_mask=SolidFillColorMask(
                    front_color=front_color_qrcode, back_color=back_color_qrcode
                ),
                embedded_image_path=image_on_qrcode,
            )._img

            file_path = filedialog.asksaveasfilename(
                title="Save QRcode image",
                defaultextension=".png",
                filetypes=[("PNG file", "*.png")],
            )

            if file_path:
                pil_img.save(file_path)
                custom_dialog("Success", f"your file saved at {file_path}")

        elif is_qrcode_gap_square_shape == True:
            pil_img = qr_data.make_image(
                image_factory=StyledPilImage,
                module_drawer=GappedSquareModuleDrawer(size_ratio=0.8),
                color_mask=SolidFillColorMask(
                    front_color=front_color_qrcode, back_color=back_color_qrcode
                ),
                embedded_image_path=image_on_qrcode,
            )._img

            file_path = filedialog.asksaveasfilename(
                title="Save QRcode image",
                defaultextension=".png",
                filetypes=[("PNG file", "*.png")],
            )

            if file_path:
                pil_img.save(file_path)
                custom_dialog("Success", f"your file saved at {file_path}")

        elif is_qrcode_round_corner == True:
            pil_img = qr_data.make_image(
                image_factory=StyledPilImage,
                module_drawer=RoundedModuleDrawer(),
                color_mask=SolidFillColorMask(
                    front_color=front_color_qrcode, back_color=back_color_qrcode
                ),
                embedded_image_path=image_on_qrcode,
            )._img

            file_path = filedialog.asksaveasfilename(
                title="Save QRcode image",
                defaultextension=".png",
                filetypes=[("PNG file", "*.png")],
            )

            if file_path:
                pil_img.save(file_path)
                custom_dialog("Success", f"your file saved at {file_path}")

        elif is_qrcode_horizontal_code == True:
            pil_img = qr_data.make_image(
                image_factory=StyledPilImage,
                module_drawer=HorizontalBarsDrawer(),
                color_mask=SolidFillColorMask(
                    front_color=front_color_qrcode, back_color=back_color_qrcode
                ),
                embedded_image_path=image_on_qrcode,
            )._img

            file_path = filedialog.asksaveasfilename(
                title="Save QRcode image",
                defaultextension=".png",
                filetypes=[("PNG file", "*.png")],
            )

            if file_path:
                pil_img.save(file_path)
                custom_dialog("Success", f"your file saved at {file_path}")

        elif is_qrcode_vertical_code == True:
            pil_img = qr_data.make_image(
                image_factory=StyledPilImage,
                module_drawer=VerticalBarsDrawer(),
                color_mask=SolidFillColorMask(
                    front_color=front_color_qrcode, back_color=back_color_qrcode
                ),
                embedded_image_path=image_on_qrcode,
            )._img

            file_path = filedialog.asksaveasfilename(
                title="Save QRcode image",
                defaultextension=".png",
                filetypes=[("PNG file", "*.png")],
            )

            if file_path:
                pil_img.save(file_path)
                custom_dialog("Success", f"your file saved at {file_path}")

        else:
            pil_img = qr_data.make_image(
                fill_color=front_color_qrcode,
                back_color=back_color_qrcode,
                embedded_image_path=image_on_qrcode,
            )._img
            file_path = filedialog.asksaveasfilename(
                title="Save QRcode image",
                defaultextension=".png",
                filetypes=[("PNG file", "*.png")],
            )

            if file_path:
                pil_img.save(file_path)
                custom_dialog("Success", f"your file saved at {file_path}")
    except ValueError as e:
        custom_dialog(
            "Sorry",
            f"Content data is too huge to fit in qrcode image.It cannot be saved\n Error: {e}",
        )
    except Exception as e:
        custom_dialog("Oopsie", e)


# change hover text color
def on_move(event=None):
    qrcode_img.configure(fg_color="white", text_color="black")


def on_leave(event=None):
    qrcode_img.configure(fg_color="black", text_color="white")


def on_move_read(event=None):
    read_qrcode_image.configure(fg_color="white", text_color="black")


def on_leave_read(event=None):
    read_qrcode_image.configure(fg_color="black", text_color="white")

def on_move_custom(event=None):
    customise_qrcode.configure(fg_color="white", text_color="black")


def on_leave_custom(event=None):
    customise_qrcode.configure(fg_color="black", text_color="white")

# read qrcode images
def read_qrcode_image():
    file_name = filedialog.askopenfilename(
        title="Select QRCode image", filetypes=[("Image files", "*png *jpg *jpeg")]
    )
    pil_img_read = Image.open(file_name)

    for qr in decode(pil_img_read):
        custom_dialog_read("Content", qr.data.decode("utf-8"))


# qrcode image after create code
qrcode_img = CTkFrame(qrcode_img_frame, fg_color="transparent")
qrcode_img.grid(padx=20, pady=20, column=0, row=0, sticky="ew")

# button for saving qr code image
qrcode_img = CTkButton(
    qrcode_img_frame,
    text="Save this qrcode",
    command=save_qr_code,
    fg_color="black",
    corner_radius=10,
    height=60,
    hover_color="white",
)
qrcode_img.grid(padx=20, column=0, row=1, sticky="new")
read_qrcode_image = CTkButton(
    qrcode_img_frame,
    text="Read QrCode from image",
    command=read_qrcode_image,
    fg_color="black",
    corner_radius=10,
    height=60
)
read_qrcode_image.grid(padx=20, column=0, row=2, sticky="new")

qrcode_img.bind("<Enter>", on_move)
qrcode_img.bind("<Leave>", on_leave)

read_qrcode_image.bind("<Enter>", on_move_read)
read_qrcode_image.bind("<Leave>", on_leave_read)



# placeholder text code here
txt_placeholder = CTkLabel(filling_img_frame, text="Enter text to generate")
txt_placeholder.grid(padx=20, pady=(10, 0), column=0, row=0, sticky="new")

# textbox for entering text
txt_filling = CTkTextbox(filling_img_frame)
txt_filling.grid(padx=20, pady=(5, 20), column=0, row=1, sticky="nsew")
txt_filling.bind("<KeyRelease>", generate_qr)

generate_qr()

customise_qrcode = CTkButton(
    qrcode_img_frame,
    text="Customise QRCode image",
    command=customise_qrcode,
    fg_color="black",
    corner_radius=10,
    height=60
)
customise_qrcode.grid(padx=20, column=0, row=3, sticky="new")

customise_qrcode.bind("<Enter>", on_move_custom)
customise_qrcode.bind("<Leave>", on_leave_custom)

# app mainloop code end here
app.mainloop()
