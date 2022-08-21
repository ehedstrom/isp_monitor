# Import speedtest.net's speedtest-cli module.
try:
    import speedtest
except ImportError as error:
    print(error)

# Import date time for human readable time.
try:
    import datetime
except ImportError as error:
    print(error)

# Import matplotlib to create visualizations of speed.
try:
    import matplotlib
except ImportError as error:
    print(error)

# This script will run for X hour blocks.
try:
    import time
except ImportError as error:
    print(error)

# This script will run for X hour blocks.
try:
    import logging
except ImportError as error:
    print(error)

# Local variables
run_time_hours = .1
log_path = "./log/"

# Logging basic config
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

# Start of epoc time.
logging.info("ISP Monitor START")
start_epoc = time.time()

# Convert run time into minutes.
run_time_seconds = run_time_hours * 60 * 60

# Run monitor until time has expired.
end_epoc = start_epoc + run_time_seconds

# Convert to local time.
datetime_time = datetime.datetime.fromtimestamp(end_epoc)

# Display stop time to terminal.
logging.info(f"ISP Monitor run until {datetime_time}")

# Main loop.
while time.time() <= end_epoc:

    # Remote speed test.
    speed = speedtest.Speedtest()

    # Upload / download in megabytes.
    upload = speed.upload() / 1024 / 1024
    download = speed.download() / 1024 / 1024

    # Clean the numbers up for a human to view.
    download = round(download, 1)
    upload = round(upload, 1)

    # Notify to terminal.
    logging.info(f"UP: {upload} MB DOWN: {download} MB")

    # We only want to check occasionally.
    time.sleep(30)



