# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pattern import Checker, Circle, Spectrum

def main():
    a = Checker(100, 10)
    a.draw()
    a.show()

    b = Circle(512, 20, (50, 50))
    b.draw()
    b.show()

    c = Spectrum(100)
    c.draw()
    c.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
