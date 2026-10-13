import fastf1 as f1
# ---- Data Collection -----
def get_racedata(year, round_no):
    # ---- Loading Session Data ----
    session = f1.get_session(year, round_no, "R")
    session.load()
    # ---- Getting data from the loaded session ----
    r_data = session.laps
    return r_data

# ---- Data Preprocessing ----
def preprocess(r_data):
    #---- Selecting only wanted columns ----
    cr_data = r_data[["Driver", "LapTime", "LapNumber", "Stint", "PitInTime", "PitOutTime", "Sector1Time", "Sector2Time", "Sector3Time", "IsPersonalBest", "Compound", "TyreLife", "FreshTyre", "Team", "TrackStatus", "Position"]]
    #---- Converting all Times into seconds(s)
    time_cols = cr_data.select_dtypes(include=['timedelta64']).columns
    for col in time_cols:
        cr_data[col] = cr_data[col].dt.total_seconds()
    # ---- Adding required columns ----
    if cr_data["PitInTime"].notna():
        cr_data["InLap"] = True
    else:
        cr_data["InLap"] = False
    return cr_data

if __name__ == "__main__":
    year = int(input("Enter the year of the race: "))
    round_no = int(input("Enter the round no of the race: "))
    session= get_racedata(year, round_no)
    clean_rdata = preprocess(session)
    print(clean_rdata)