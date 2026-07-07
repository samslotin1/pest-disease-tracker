from datetime import datetime

SAVE_TO_FILE = False


tracker_records = []


def get_new_observations():
    today = datetime.today()
    today_as_text = str(today)

    plant = input("Type a plant: ").strip().lower()
    issue = input("Type issue: ").strip().lower()
    severity = int(input("Type severity: ").strip().lower())

    observation = {
        "date": today_as_text,
        "plant": plant,
        "issue": issue,
        "severity": severity,
    }

    return observation

def explain_severity(severity):
    if severity == 1:
        return "Severity 1: Mild"

    elif severity == 2:
        return "Severity 2: Noticeable "
    elif severity == 3:
        return "Severity 3: Moderate"
    elif severity == 4:
        return "Severity 4: Serious"
    elif severity == 5:
        return "Severity 5: Critical"
    else:
        return "Invalid severity"


while True:
    print("1. Add Observation")
    print("2. View Observations")
    print("3. Search by plant")
    print("4. Analyze Observations")
    print("5. Quit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        observation = get_new_observations()
        tracker_records.append(observation)
        print(tracker_records)

        if SAVE_TO_FILE == True:
            print("Saving is turned on")
        else:
            print("Testing mode: not saving to file")

    elif choice == "2":
        print("View observations")
        for tracker_record in tracker_records:
            print("Plant:", tracker_record["plant"])
            print("Issue:", tracker_record["issue"])
            print(explain_severity(tracker_record["severity"]))


    elif choice == "3":
        print("Search by plant")
        search_plant = input("Type plant: ").strip().lower()

        found_match = False

        for tracker_record in tracker_records:
            if search_plant == tracker_record["plant"]:
                found_match = True
                print("Match found:")
                print(tracker_record)

        if found_match == False:
            print("No match found")


    elif choice == "4":
        print("Analyze Observations")
        print("Total observations:", len(tracker_records))

        if len(tracker_records) == 0:
            print("No observations to analyze yet.")
            continue

        total_severity = 0
        most_severe_record = None
        issue_counts = {}
        plant_counts = {}


        for tracker_record in tracker_records:
            total_severity = total_severity + tracker_record["severity"]

            issue = tracker_record["issue"]
            plant = tracker_record["plant"]

            if issue not in issue_counts:
                issue_counts[issue] = 1
            else:
                issue_counts[issue] = issue_counts[issue] + 1

            if plant not in plant_counts:
                plant_counts[plant] = 1
            else:
                plant_counts[plant] = plant_counts[plant] + 1

            if most_severe_record == None:
                most_severe_record = tracker_record
            elif tracker_record["severity"] > most_severe_record["severity"]:
                most_severe_record = tracker_record



        average_severity = total_severity / len(tracker_records)

        print("Total severity:", total_severity)
        print("Average severity:", average_severity)
        print("Most severe observation:", most_severe_record)
        print("Issue counts:", issue_counts)
        print("Plant counts:", plant_counts)

    elif choice == "5":
        print("Quit")
        break

    else:
        print("Invalid choice")
