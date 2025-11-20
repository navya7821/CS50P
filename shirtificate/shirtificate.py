from fpdf import FPDF

class PDF(FPDF):
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.add_page()

        self.set_font("helvetica", "B", 28)
        self.set_text_color(0, 0, 0)  
        self.set_y(20)
        self.cell(0, 15, "CS50 Shirtificate", align="C")

        image_width = 150
        x_center = (self.w - image_width) / 2
        self.image("shirtificate.png", x=x_center, y=40, w=image_width)
        self.set_font("helvetica", "B", 24)
        self.set_text_color(255, 255, 255)
        self.set_y(87)
        self.cell(0, 10, f"{self.name} took CS50", align="C")

def main():
    say = input("Name: ")
    pdf = PDF(say)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
