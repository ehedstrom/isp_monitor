# ISP speed monitor
# Samples and logs upload and download speeds over a fixed time period to csv.
# 2022 Eric Hedstrom

# Import date time for human-readable time.
try:
    import datetime
except ImportError as error:
    print(error)

# Import time for seconds calculation and sleep.
try:
    import time
except ImportError as error:
    print(error)

# Import matplotlib to create visualizations of speed.
try:
    import matplotlib.pyplot as plt
except ImportError as error:
    print(error)

# Use logging to display info messages to terminal.
try:
    import logging
except ImportError as error:
    print(error)

# Import speedtest.net's speedtest-cli module.
try:
    import speedtest
except ImportError as error:
    print(error)

# Local variables
run_time_hours = .1     # This script will run for X hours.
variable_delay = 30    # Seconds between tests.

# Current date/time for log name. If today exists it will append.
current_date = str(datetime.datetime.today().strftime('%Y-%m-%d'))

# Log information and configuration
log_name = str("ispmon_" + current_date)
log_path = "./log/" + log_name
log_enabled = True


# Main loop.
def main():
    # Open an existing log or create a new one.
    if log_enabled:
        with open(log_path, "a+") as speed_log:
            text = str(log_name + "[LOG START] UP, DOWN \n")
            speed_log.write(text)

    # Logging basic config.
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    # Start of epoc time.
    logging.info("ISP Monitor START")
    start_epoc = time.time()

    # Convert run time into minutes.
    run_time_seconds = run_time_hours * 3600

    # Run monitor until time has expired.
    end_epoc = start_epoc + run_time_seconds

    # Convert to local time.
    datetime_time = datetime.datetime.fromtimestamp(end_epoc)

    # Display stop time to terminal.
    logging.info(f"ISP Monitor run until {datetime_time}")

    while time.time() <= end_epoc:
        # Remote speed test.
        try:
            speed = speedtest.Speedtest()
            # Upload / download in megabytes.
            upload = speed.upload() / 1024 / 1024
            download = speed.download() / 1024 / 1024

        except IndexError:
            print(f"NO CONNECTION")
            speed.upload = 0
            speed.download = 0

        # Clean the numbers up for a human to view.
        download = str(round(download, 1))
        upload = str(round(upload, 1))

        # Notify to terminal.
        logging.info(f"UP: {upload} MB DOWN: {download} MB")

        # Write to log.
        if log_enabled:
            with open(log_path, "a+") as speed_log:
                current_time = str(datetime.datetime.now())
                text = current_time + ", " + upload + ", " + download + "\n"
                speed_log.write(text)

        # We only want to check occasionally.
        time.sleep(variable_delay)


# Run if not imported.
if __name__ == "__main__":
    main()


