import fitz  # PyMuPDF
import os
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
import io
from PIL import Image


import fitz  # PyMuPDF
import os
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
import io
from PIL import Image


def create_booklet3(input_pdf, output_pdf):
    # Open the input PDF
    input_document = fitz.open(input_pdf)
    num_pages = input_document.page_count

    # Calculate the number of pages needed for the booklet (must be a multiple of 4)
    num_pages_booklet = (
        num_pages if num_pages % 4 == 0 else num_pages + (4 - num_pages % 4)
    )
    # num_pages_booklet = num_pages

    left = list(range(0, num_pages_booklet // 2))
    left = list(reversed(left))
    right = list(range(num_pages_booklet // 2, num_pages_booklet))
    # right = list(reversed(right))
    output_pdf_writer = PdfWriter()
    flip = False  # page direction flip

    for i in range(max(len(left) // 2, len(right) // 2)):
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=landscape(A4))
        if flip:
            # Add the left page (if exists)
            leftNum1 = left.pop()
            leftNum2 = left.pop()
            if leftNum1 < num_pages:
                page = input_document.load_page(leftNum1)
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                img.save("temp_left_page.png")
                can.drawImage(
                    "temp_left_page.png", 0, 0, width=A4[1] / 2, height=A4[0] / 2
                )
            if leftNum2 < num_pages:
                page = input_document.load_page(leftNum2)
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                img.save("temp_left_page.png")
                can.drawImage(
                    "temp_left_page.png",
                    0,
                    A4[0] / 2,
                    width=A4[1] / 2,
                    height=A4[0] / 2,
                )

            # Add the right page (if exists)
            rightNum1 = right.pop()
            rightNum2 = right.pop()
            if rightNum1 < num_pages:
                page = input_document.load_page(rightNum1)
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                img.save("temp_right_page.png")
                can.drawImage(
                    "temp_right_page.png", A4[1] / 2, 0, width=A4[1] / 2, height=A4[0]
                )
            if rightNum2 < num_pages:
                page = input_document.load_page(rightNum2)
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                img.save("temp_right_page.png")
                can.drawImage(
                    "temp_right_page.png",
                    A4[1] / 2,
                    A4[0] / 2,
                    width=A4[1] / 2,
                    height=A4[0] / 2,
                )
            flip = False
        else:
            # Add the left page (if exists)
            leftNum1 = left.pop()
            leftNum2 = left.pop()
            if leftNum1 < num_pages:
                page = input_document.load_page(leftNum1)
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                img.save("temp_right_page.png")
                can.drawImage(
                    "temp_right_page.png", A4[1] / 2, 0, width=A4[1] / 2, height=A4[0]
                )

            if leftNum2 < num_pages:
                page = input_document.load_page(leftNum2)
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                img.save("temp_right_page.png")
                can.drawImage(
                    "temp_right_page.png",
                    A4[1] / 2,
                    A4[0] / 2,
                    width=A4[1] / 2,
                    height=A4[0] / 2,
                )

            # Add the right page (if exists)
            rightNum1 = right.pop()
            rightNum2 = right.pop()
            if rightNum1 < num_pages:
                page = input_document.load_page(rightNum1)
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                img.save("temp_left_page.png")
                can.drawImage(
                    "temp_left_page.png", 0, 0, width=A4[1] / 2, height=A4[0] / 2
                )

            if rightNum2 < num_pages:
                page = input_document.load_page(rightNum2)
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                img.save("temp_left_page.png")
                can.drawImage(
                    "temp_left_page.png",
                    0,
                    A4[0] / 2,
                    width=A4[1] / 2,
                    height=A4[0] / 2,
                )

            flip = True
        can.save()

        # Move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfReader(packet)
        output_pdf_writer.add_page(new_pdf.pages[0])

    # Save the new PDF
    with open(output_pdf, "wb") as f:
        output_pdf_writer.write(f)

    input_document.close()

    # Clean up temporary images
    if os.path.exists("temp_left_page.png"):
        os.remove("temp_left_page.png")
    if os.path.exists("temp_right_page.png"):
        os.remove("temp_right_page.png")


def create_booklet(input_pdf, output_pdf):
    # Open the input PDF
    input_document = fitz.open(input_pdf)
    num_pages = input_document.page_count

    # Calculate the number of pages needed for the booklet (must be a multiple of 4)
    num_pages_booklet = (
        num_pages if num_pages % 4 == 0 else num_pages + (4 - num_pages % 4)
    )
    num_pages_booklet = num_pages

    left = list(range(0, num_pages_booklet // 2))
    left = list(reversed(left))
    right = list(range(num_pages_booklet // 2, num_pages_booklet))
    # right = list(reversed(right))
    output_pdf_writer = PdfWriter()
    flip = False  # page direction flip

    for i in range(len(left)):
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=landscape(A4))
        if flip:
            # Add the left page (if exists)
            page = input_document.load_page(left.pop())
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes()))
            img.save("temp_left_page.png")
            can.drawImage("temp_left_page.png", 0, 0, width=A4[1] / 2, height=A4[0])

            # Add the right page (if exists)
            page = input_document.load_page(right.pop())
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes()))
            img.save("temp_right_page.png")
            can.drawImage(
                "temp_right_page.png", A4[1] / 2, 0, width=A4[1] / 2, height=A4[0]
            )
            flip = False
        else:
            # Add the left page (if exists)
            page = input_document.load_page(right.pop())
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes()))
            img.save("temp_left_page.png")
            can.drawImage("temp_left_page.png", 0, 0, width=A4[1] / 2, height=A4[0])

            # Add the right page (if exists)
            page = input_document.load_page(left.pop())
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes()))
            img.save("temp_right_page.png")
            can.drawImage(
                "temp_right_page.png", A4[1] / 2, 0, width=A4[1] / 2, height=A4[0]
            )

            flip = True
        can.save()

        # Move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfReader(packet)
        output_pdf_writer.add_page(new_pdf.pages[0])

    # Save the new PDF
    with open(output_pdf, "wb") as f:
        output_pdf_writer.write(f)

    input_document.close()

    # Clean up temporary images
    if os.path.exists("temp_left_page.png"):
        os.remove("temp_left_page.png")
    if os.path.exists("temp_right_page.png"):
        os.remove("temp_right_page.png")


def create_booklet2(input_pdf, output_pdf):
    # Open the input PDF
    input_document = fitz.open(input_pdf)
    num_pages = input_document.page_count

    # Calculate the number of pages needed for the booklet (must be a multiple of 4)
    num_pages_booklet = (
        num_pages if num_pages % 4 == 0 else num_pages + (4 - num_pages % 4)
    )

    # Create a list to store booklet pages order
    booklet_order = []
    left = 0
    right = num_pages_booklet

    while left < right:
        booklet_order.append(right)
        booklet_order.append(left)
        left += 1
        right -= 1

    # Create a new PDF to store the booklet
    output_pdf_writer = PdfWriter()
    flip = False  # page direction flip
    # Add pages to the new PDF in booklet order, two pages per landscape A4 sheet
    for i in range(1, len(booklet_order) + 1, 2):
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=landscape(A4))
        if flip:
            # Add the left page (if exists)
            if i < len(booklet_order) and booklet_order[i] < num_pages:
                page = input_document.load_page(booklet_order[i])
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                img.save("temp_left_page.png")
                can.drawImage("temp_left_page.png", 0, 0, width=A4[1] / 2, height=A4[0])

            # Add the right page (if exists)
            if i + 1 < len(booklet_order) and booklet_order[i + 1] < num_pages:
                page = input_document.load_page(booklet_order[i + 1])
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                img.save("temp_right_page.png")
                can.drawImage(
                    "temp_right_page.png", A4[1] / 2, 0, width=A4[1] / 2, height=A4[0]
                )
            flip = False
        else:
            # Add the left page (if exists)
            if i < len(booklet_order) and booklet_order[i] < num_pages:
                page = input_document.load_page(booklet_order[i])
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                img.save("temp_right_page.png")
                can.drawImage(
                    "temp_right_page.png", A4[1] / 2, 0, width=A4[1] / 2, height=A4[0]
                )

            # Add the right page (if exists)
            if i + 1 < len(booklet_order) and booklet_order[i + 1] < num_pages:
                page = input_document.load_page(booklet_order[i + 1])
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                img.save("temp_left_page.png")
                can.drawImage("temp_left_page.png", 0, 0, width=A4[1] / 2, height=A4[0])

            flip = True

        can.save()

        # Move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfReader(packet)
        output_pdf_writer.add_page(new_pdf.pages[0])

    # Save the new PDF
    with open(output_pdf, "wb") as f:
        output_pdf_writer.write(f)

    input_document.close()

    # Clean up temporary images
    if os.path.exists("temp_left_page.png"):
        os.remove("temp_left_page.png")
    if os.path.exists("temp_right_page.png"):
        os.remove("temp_right_page.png")


def main():
    input_pdf = (
        "/Users/ryanpelchat/Downloads/math.pdf"  # Replace with your input PDF path
    )
    output_pdf = "/Users/ryanpelchat/Downloads/mathBooklet2.pdf"  # Replace with your desired output PDF path

    input_pdf = (
        "/Users/ryanpelchat/Downloads/heapq.pdf"  # Replace with your input PDF path
    )
    output_pdf = "/Users/ryanpelchat/Downloads/heapq.pdf"  # Replace with your desired output PDF path

    input_pdf = (
        "/Users/ryanpelchat/Downloads/solution2.pdf"  # Replace with your input PDF path
    )
    output_pdf = "/Users/ryanpelchat/Downloads/solution2Booklet.pdf"  # Replace with your desired output PDF path

    # if not os.path.exists(input_pdf):
    #     print(f"Error: The file '{input_pdf}' does not exist.")
    #     return

    input_pdf = "/Users/ryanpelchat/Downloads/collections.pdf"  # Replace with your input PDF path
    output_pdf = "/Users/ryanpelchat/Downloads/collectionsBooklet.pdf"  # Replace with your desired output PDF path
    create_booklet(input_pdf, output_pdf)
    print(f"Booklet created successfully: '{output_pdf}'")

    input_pdf = (
        "/Users/ryanpelchat/Downloads/bisect.pdf"  # Replace with your input PDF path
    )
    output_pdf = "/Users/ryanpelchat/Downloads/bisectBooklet.pdf"  # Replace with your desired output PDF path
    create_booklet(input_pdf, output_pdf)
    print(f"Booklet created successfully: '{output_pdf}'")

    input_pdf = (
        "/Users/ryanpelchat/Downloads/math.pdf"  # Replace with your input PDF path
    )
    output_pdf = "/Users/ryanpelchat/Downloads/mathBooklet.pdf"  # Replace with your desired output PDF path
    create_booklet(input_pdf, output_pdf)
    print(f"Booklet created successfully: '{output_pdf}'")


if __name__ == "__main__":
    main()
