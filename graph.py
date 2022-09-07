
import datetime
import matplotlib.pyplot as plt

# Current date/time for log name. If today exists it will append.
current_date = str(datetime.datetime.today().strftime('%Y-%m-%d'))

# Find today's log
log_name = str("ispmon_" + current_date)
log_path = "./log/" + log_name

# Dictionary to hold speed information
speed = {}


def plot_speed(speed):
    new_plot = plt.plot()
    print("Graph start")
    plt.title('ISP Monitor')
    x = []
    y = []

    # plot
    i = 0
    for time in speed:
        i += 1
        # Time holds (timestamp, (x, y))
        this_x = i

        #
        this_y = speed[time][1].split(" ")[1]

        #
        x.append(this_x)
        y.append(this_y)
        print(f"x:{this_x}, y{this_y}")
        plt.show()
    print("Plot graph.")
    new_plot.plot(x, y, linewidth=2.0)


with open(log_path, "r") as log:
    lines = log.readlines()
    for line in lines:
        if line.find("ispmon"):

            time_stamp = (line.split(" ")[1]).split(".")[0]

            up = line.split(",")[1]
            down = (line.split(",")[2]).replace("\n", "")

            speed[time_stamp] = (up, down)
            print(f"Up:{up}, Down:{down}")

plot_speed(speed)
