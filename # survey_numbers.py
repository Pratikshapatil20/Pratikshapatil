# survey_numbers.py

class LandStatus:
    def __init__(self):
        # Define land status data structure
        self.land_status = {
            "District1": {
                "Mandal1": {
                    "Village1": ["Survey1", "Survey2", "Survey3"],
                    "Village2": ["Survey4", "Survey5", "Survey6"]
                },
                "Mandal2": {
                    "Village3": ["Survey7", "Survey8", "Survey9"],
                    "Village4": ["Survey10", "Survey11", "Survey12"]
                }
            },
            "District2": {
                "Mandal3": {
                    "Village5": ["Survey13", "Survey14", "Survey15"],
                    "Village6": ["Survey16", "Survey17", "Survey18"]
                },
                "Mandal4": {
                    "Village7": ["Survey19", "Survey20", "Survey21"],
                    "Village8": ["Survey22", "Survey23", "Survey24"]
                }
            }
            # Add more districts, mandals, villages, and survey numbers as needed
        }

    def get_survey_numbers(self, district, mandal, village):
        # Get survey numbers based on input
        if district in self.land_status and mandal in self.land_status[district] \
                and village in self.land_status[district][mandal]:
            return self.land_status[district][mandal][village]
        else:
            return []

# Example usage
if __name__ == "__main__":
    land_status = LandStatus()
    district = input("Enter district: ")
    mandal = input("Enter mandal: ")
    village = input("Enter village: ")
    survey_numbers = land_status.get_survey_numbers(district, mandal, village)
    if survey_numbers:
        print("Survey numbers for {}/{}/{}:".format(district, mandal, village))
        for survey_number in survey_numbers:
            print(survey_number)
    else:
        print("No survey numbers found for {}/{}/{}".format(district, mandal, village))
