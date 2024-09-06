Scripts to analyze NavSatFix messages collected in rosbags. Originally used to troubleshoot issues with accuracy on the AV200 in Mcity's MachE.


# Directories (create if not present)

bags/ - bags

data/ - parsed data


# Scripts

1. oxts-recorder.py

	Purpose: Records the /oxts/fix topic to a .txt file. Once this recorder is running, replay your rosbag in another terminal window.

	Arguments: Name of desired output file (example: sep4-highway-loop)

	Output: A .txt file beginning with the argument name, ending in timestamp + .txt


2. parse-navsat.py

	Purpose: Parses a .txt file from `oxts-recorder.py` into <timestamp> <position_covariance> lines.

	Arguments: .txt filename, such as: `data/sep4-highway-loop_2024-09-06_09:40:13.txt`

	Output: A _out.txt file with mostly the same name as the provided argument, in the same directory.


2. warn-covariance.py

	Purpose: Reads the _out.txt files and warns in stdout if position_covariance matrix positions 1,5,9 exceeds 0.01.

	Arguments: _out.txt filename, such as: `data/sep4-highway-loop_2024-09-06_09:40:13_out.txt`

	Output: No file, just prints warnings to stdout


# Steps 

- Record a rosbag on the test vehicle (copy to USB, place into `bags/` here)

- Run oxts-recorder.py, and simultaneously replay the rosbag

- Run the .txt through parse-navsat.py to get a filtered file with timestamp and covariance

- Run the warn-covariance.py script to check for any anomalies in covariance


# Disclaimer

These were hastily written for ad-hoc, one-time use for some troubleshooting in September 2024. These scripts could easily be combined into one script or done better, they are here for you to start with if you want them.
