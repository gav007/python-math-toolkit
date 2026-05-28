import matplotlib.pyplot as plt


def graph_linear_equation(linear):
    
    # gets the users x and y
    user_x = linear.get_x()
    user_y = linear.get_y()
    
    # static range for now
    x_values = list(range(-10, 11))
    
    # create y using the linear equation
    y_vals = []
    
    for x in x_values:
        y = linear.calculate_y(x)
        y_vals.append(y)
        
    # creates the figure and graph
    fig, ax = plt.subplots()
    
    # plot the line on graph
    ax.plot(x_values, y_vals)
    
    # mark the users calculated point
    ax.scatter(user_x, user_y)
    
    # details for graph
    ax.set_title(str(linear)) # --> object __str__
    ax.set_xlabel("X Val")
    ax.set_ylabel("Y Val")
    ax.grid(True)
    ax.grid(True)
    
    plt.show()
    