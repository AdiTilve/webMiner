from Kwic_Modules import *
from Model import db
class File_Upload:
    def __init__(self):
        self.web_link = ""
        self.dictionary={}
        self.full_list = []
        self.description_start = 0
        self.Web_links = []
        self.temp_Web_links=[]
        self.desc_list=[]
        self.Description = []
        self.final_decrip = []
        self.c = Circular_shift()
        self.alpha = Alphabetizer()
        self.noise_e = Noise_Eliminator()
    def upload_file(self, file_content):
        # Split the file content into sections using "$"
        sections = file_content.split('$')

        for section in sections:
            # Process each section (weblink and description)
            self.process_section(section.strip())
        self.process_db_section()
    def process_section(self,section):
        try:
            self.section = section
            self.alpha_list = []
            # In Below code we separate web link and description
            for i in range(0, len(self.section)):
                if self.section[i] == "\n":
                    self.description_start = i
                    break
                self.web_link += self.section[i]
            self.file_content = self.section[self.description_start + 1::]

            #In below code we split the description and then perform KWIC on description
            self.input_list = self.file_content.split(".")

            # Remove leading and trailing whitespaces from each sentence
            self.input_list = [sentence.strip() for sentence in self.input_list if sentence.strip()]

            for line in self.input_list:
                self.c.setline(line)
                self.cs_line=self.c.getline()
                self.noise_e.setline(self.cs_line)
                self.noise_eliminated_list=self.noise_e.getline()
                self.alpha.setline(self.noise_eliminated_list)
                self.alpha_list.extend(self.alpha.get_lines())
            self.alpha.setline(self.alpha_list)
            self.alpha_list=self.alpha.get_lines()
            self.dictionary={"Web_links":self.web_link,"Description":self.alpha_list}
            self.desc_list.extend(self.alpha_list)
            self.full_list.append(self.dictionary)
            self.web_link=""
            self.dictionary=dict()

        except Exception as e:
            print(f"An error occurred: {e}")

    def process_db_section(self):
        try:
            # Using the database file to get the data from database and then sort it and input the data again
            alpha = Alphabetizer()
            d=db.Database()
            self.rows=d.fetch_data()
            for row in self.rows:
                self.Description.append(row["Description"]) # Inserting Description from database into the list
            self.Description.extend(self.desc_list) # Adding new Description

            # Removing any duplicate description and this overrides the same data
            for item in self.Description:
                # Check if the item is not already in final_decrip
                if item not in self.final_decrip:
                    self.final_decrip.append(item)
            alpha.setline(self.final_decrip)
            self.final_decrip = alpha.get_lines()
            for line in self.final_decrip:
                if line in self.desc_list:
                    self.matching_web_links=[item['Web_links'] for item in self.full_list if line in item['Description']]
                    self.Web_links.extend(self.matching_web_links)
                else:
                    self.matching_web_links = [item['Web_links'] for item in self.rows if item['Description'] == line]
                    self.Web_links.extend(self.matching_web_links)

            # Zipping the Web links and description for inserting in database
            self.zipped_list=list(zip(self.Web_links,self.final_decrip))
            d.insert_data(self.zipped_list)
        except Exception as e:
            print(f"An error occurred: {e}")