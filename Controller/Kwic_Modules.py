import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
class Input:

    def read_input(self):
        self.n = input("Enter number of lines:")# Enter number of input lines
        self.input_list = []  # List to store the input lines
        # Below loop takes input and stores in list
        for i in range(int(self.n)):
            self.input_list.append(input())

    def get_input(self):
        return self.input_list
class Circular_shift:
    # setline function is used to get input lines and to call circular shift methods
    def setline(self, input_line):
        self.input_line = input_line
        self.__circular_shft(self.input_line)

    # Provate method which circularly shifts line
    def __circular_shft(self,input_line):
        self.line=self.input_line.split() # Split string to list containing each word
        self.shift_lines=[]
        for i in range(len(self.line)): # n-1 loop for circular shift
            self.shift_lines.append(" ".join(self.line)) # Appending to new list
            pop_elem=self.line.pop(0) # Popping first element
            self.line.append(pop_elem) # appending at last

    # Getter method to get the circularly shifted lines
    def getline(self):
        return self.shift_lines
class Alphabetizer:
    # setline function is used to get Circularly shifted lines and to call circular shift methods
    def setline(self, cs_line):
        self.cs_line = cs_line
        self.__alphabetize(self.cs_line)

    # In below function the lines would be alphabetically sorted
    def __alphabetize(self,cs_lines):
        self.__merge_sort(self.cs_line)

    def __merge_sort(self, lines):
        if len(lines) > 1:
            middle = len(lines) // 2
            left_half = lines[:middle]
            right_half = lines[middle:]

            self.__merge_sort(left_half)  # Recursively sort the left half
            self.__merge_sort(right_half)  # Recursively sort the right half

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i].lower() < right_half[j].lower():
                    lines[k] = left_half[i]
                    i += 1
                else:
                    lines[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                lines[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                lines[k] = right_half[j]
                j += 1
                k += 1


    def get_lines(self):
        return self.cs_line

class Noise_Eliminator:
    def setline(self, cs_line):
        self.input_line=cs_line
        self.__eliminate_noise(self.input_line)

    def __eliminate_noise(self,text_list):
        self.stop_words = set(stopwords.words('english'))
        self.cleaned_text_list = []

        for text in text_list:
            self.lines = text.split('\n')
            self.clean_lines = []

            for line in self.lines:
                self.words = line.split()
                if not self.words or self.words[0].lower() not in self.stop_words:
                    self.clean_lines.append(line)

            if self.clean_lines:
                self.cleaned_text = '\n'.join(self.clean_lines)
                self.cleaned_text_list.append(self.cleaned_text)
                self.clean_lines.clear()

    def getline(self):
        return self.cleaned_text_list