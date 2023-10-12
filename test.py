# A simple Disaster Management System in Python

class DisasterIncident:
    def __init__(self, incident_id, incident_type, location, description):
        self.incident_id = incident_id
        self.incident_type = incident_type
        self.location = location
        self.description = description

class DisasterManagementSystem:
    def __init__(self):
        self.incidents = []

    def add_incident(self, incident_type, location, description):
        incident_id = len(self.incidents) + 1
        incident = DisasterIncident(incident_id, incident_type, location, description)
        self.incidents.append(incident)
        print(f"Incident {incident_id} added successfully.")

    def list_incidents(self):
        print("List of Disaster Incidents:")
        for incident in self.incidents:
            print(f"Incident ID: {incident.incident_id}")
            print(f"Incident Type: {incident.incident_type}")
            print(f"Location: {incident.location}")
            print(f"Description: {incident.description}")
            print("-----------------------------")

if __name__ == '__main__':
    dms = DisasterManagementSystem()

    while True:
        print("\nDisaster Management System Menu:")
        print("1. Add Disaster Incident")
        print("2. List Disaster Incidents")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            incident_type = input("Enter incident type: ")
            location = input("Enter location: ")
            description = input("Enter description: ")
            dms.add_incident(incident_type, location, description)
        elif choice == '2':
            dms.list_incidents()
        elif choice == '3':
            print("Exiting Disaster Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
