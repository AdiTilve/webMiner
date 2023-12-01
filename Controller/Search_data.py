from Model import db

class Search:
    def search_data(self,keywords):
        try:
            self.Web_links = []
            self.matching_web_links = []
            self.Description = []
            self.Web_links = []
            self.excluded_web_links = []
            self.keywords = keywords

            # Getting the Description from the database
            d=db.Database()
            self.rows=d.fetch_data()
            for row in self.rows:
                self.Description.append(row["Description"])

            # Condition for AND Based Search
            if any(keyword.lower() == "and" for keyword in self.keywords): # To check if and exists in search

                """
                Below logic matches all the keyword in all the specific Description and then getting
                the Web links for those description.
                
                The last if removes any duplicate Web Links which are matched.
                """
                self.keywords = [keyword for keyword in self.keywords if keyword.lower() != "and"]
                for line in self.Description:
                    if all(keyword in line for keyword in self.keywords):
                        self.matching_web_links = [item['Web_links'] for item in self.rows if item["Description"]==line]
                    if not any(link in self.Web_links for link in self.matching_web_links):
                        self.Web_links.extend(self.matching_web_links)
                return self.Web_links

            # Condition for NOT Based Search
            elif any(keyword.lower() == "not" for keyword in self.keywords):
                self.keywords = [keyword for keyword in self.keywords if keyword.lower() != "not"]

                # Looping through description
                for line in self.Description:
                    self.first_word = line.split()[0] # Getting first word of each description
                    """
                    Checking if the keyword matches the first word of description and then getting their Web Links.
                    
                    Another if condition to get the Web Links which were not matched.
                    
                    Creating the list to set then again list to remove the duplicate entry.
                    """

                    if self.first_word in self.keywords:
                        self.matching_web_links = [item['Web_links'] for item in self.rows if item['Description'] == line]
                        if not any(link in self.Web_links for link in self.matching_web_links):
                            self.Web_links.extend(self.matching_web_links)
                        self.excluded_web_links = [item['Web_links'] for item in self.rows if item['Web_links'] not in self.Web_links]
                        self.excluded_set=list(set(self.excluded_web_links))
                return self.excluded_set

            # Condition for OR Based Search
            else:
                """
                Looping through description and matching the first word with keywords and then getting the
                matching web links.
                
                Second if condition to remove duplicate entries.
                """
                for line in self.Description:
                    s=line.split()[0]
                    if s in self.keywords:
                        self.matching_web_links = [item['Web_links'] for item in self.rows if item['Description'] == line]
                        if not any(link in self.Web_links for link in self.matching_web_links):
                            self.Web_links.extend(self.matching_web_links)
                return self.Web_links
        except Exception as e:
            print(f"An error occurred: {e}")
            return []