
# import numpy as np
# import streamlit as st
# import plotly.express as px
# import plotly.graph_objects as go
# import pandas as pd

# # Soccer field dimensions (in meters)
# WIDTH = 80  # Width of the field
# LENGTH = 120  # Length of the field
# GOAL_HEIGHT = 2.44  # Standard goal height
# PENALTY_AREA_WIDTH = 40.3
# PENALTY_AREA_DEPTH = 16.5
# GOAL_AREA_WIDTH = 18.32
# GOAL_AREA_DEPTH = 5.5
# GOAL_WIDTH = 7.32  # Standard width of a soccer goal

# def create_field_df():
#     """Create dataframes for different parts of the soccer field."""
#     # Field perimeter bounds
#     field_perimeter_bounds = [[0, 0, 0], [WIDTH, 0, 0], [WIDTH, LENGTH, 0], [0, LENGTH, 0], [0, 0, 0]]
#     field_df = pd.DataFrame(field_perimeter_bounds, columns=['x', 'y', 'z'])
#     field_df['line_group'] = 'field_perimeter'
#     field_df['color'] = 'field'

#     # Halfway line
#     half_field_bounds = [[0, LENGTH / 2, 0], [WIDTH, LENGTH / 2, 0]]
#     half_df = pd.DataFrame(half_field_bounds, columns=['x', 'y', 'z'])
#     half_df['line_group'] = 'half_field'
#     half_df['color'] = 'field'

#     # Penalty areas and goal areas
#     left_penalty_df = create_rectangle_df((WIDTH - PENALTY_AREA_WIDTH) / 2, 0, PENALTY_AREA_WIDTH, PENALTY_AREA_DEPTH, 'left_penalty_area')
#     right_penalty_df = create_rectangle_df((WIDTH - PENALTY_AREA_WIDTH) / 2, LENGTH - PENALTY_AREA_DEPTH, PENALTY_AREA_WIDTH, PENALTY_AREA_DEPTH, 'right_penalty_area')
#     left_goal_df = create_rectangle_df((WIDTH - GOAL_AREA_WIDTH) / 2, 0, GOAL_AREA_WIDTH, GOAL_AREA_DEPTH, 'left_goal_area')
#     right_goal_df = create_rectangle_df((WIDTH - GOAL_AREA_WIDTH) / 2, LENGTH - GOAL_AREA_DEPTH, GOAL_AREA_WIDTH, GOAL_AREA_DEPTH, 'right_goal_area')

#     # Combine all DataFrames
#     return pd.concat([field_df, half_df, left_penalty_df, right_penalty_df, left_goal_df, right_goal_df])

# def create_rectangle_df(start_x, start_y, width, height, line_group):
#     """Create a dataframe representing a rectangle on the field."""
#     rectangle_bounds = [
#         [start_x, start_y, 0],
#         [start_x + width, start_y, 0],
#         [start_x + width, start_y + height, 0],
#         [start_x, start_y + height, 0],
#         [start_x, start_y, 0]
#     ]
#     df = pd.DataFrame(rectangle_bounds, columns=['x', 'y', 'z'])
#     df['line_group'] = line_group
#     df['color'] = 'field'
#     return df

# def create_center_circle():
#     """Create a 3D line trace for the center circle."""
#     theta = np.linspace(0, 2 * np.pi, 100)
#     x = [(WIDTH / 2) + (9.15 * np.cos(t)) for t in theta]
#     y = [(LENGTH / 2) + (9.15 * np.sin(t)) for t in theta]
#     z = [0] * 100
#     return go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='white', width=2))

# def create_goalposts():
#     """Create goalpost lines for both ends of the field."""
#     goalposts = []

#     # Right goalpost (at x = length)
#     goalposts.extend([
#         go.Scatter3d(x=[(WIDTH / 2) - (GOAL_WIDTH / 2), (WIDTH / 2) - (GOAL_WIDTH / 2)], y=[LENGTH, LENGTH], z=[0, GOAL_HEIGHT], mode='lines', line=dict(color='black', width=4)),
#         go.Scatter3d(x=[(WIDTH / 2) + (GOAL_WIDTH / 2), (WIDTH / 2) + (GOAL_WIDTH / 2)], y=[LENGTH, LENGTH], z=[0, GOAL_HEIGHT], mode='lines', line=dict(color='black', width=4)),
#         go.Scatter3d(x=[(WIDTH / 2) - (GOAL_WIDTH / 2), (WIDTH / 2) + (GOAL_WIDTH / 2)], y=[LENGTH, LENGTH], z=[GOAL_HEIGHT, GOAL_HEIGHT], mode='lines', line=dict(color='black', width=4))
#     ])

#     # Left goalpost (at x = 0)
#     goalposts.extend([
#         go.Scatter3d(x=[(WIDTH / 2) - (GOAL_WIDTH / 2), (WIDTH / 2) - (GOAL_WIDTH / 2)], y=[0, 0], z=[0, GOAL_HEIGHT], mode='lines', line=dict(color='black', width=4)),
#         go.Scatter3d(x=[(WIDTH / 2) + (GOAL_WIDTH / 2), (WIDTH / 2) + (GOAL_WIDTH / 2)], y=[0, 0], z=[0, GOAL_HEIGHT], mode='lines', line=dict(color='black', width=4)),
#         go.Scatter3d(x=[(WIDTH / 2) - (GOAL_WIDTH / 2), (WIDTH / 2) + (GOAL_WIDTH / 2)], y=[0, 0], z=[GOAL_HEIGHT, GOAL_HEIGHT], mode='lines', line=dict(color='black', width=4))
#     ])

#     return goalposts

# def generate_trajectory(start_point, end_point, peak_height=10, num_coords=100):
#     """Generate a parabolic trajectory between start and end points."""
#     shot_start_x, shot_start_y, _ = start_point
#     hoop_x, hoop_y, _ = end_point

#     distance_x = hoop_x - shot_start_x
#     a = -4 * peak_height / (distance_x ** 2)

#     shot_path_coords = []
#     for index, x in enumerate(np.linspace(shot_start_x, hoop_x, num_coords + 1)):
#         z = a * (x - (shot_start_x + hoop_x) / 2) ** 2 + peak_height
#         y = shot_start_y + (hoop_y - shot_start_y) * (index / num_coords)
#         shot_path_coords.append([x, y, z])

#     shot_path_coords[0][2] = 0  # Ensure start z is 0
#     # shot_path_coords[-1][2] = 0  # Ensure end z is 0

#     return pd.DataFrame(shot_path_coords, columns=['x', 'y', 'z'])

# def plot_trajectories(fig, start_points, end_points, peak_height=10, num_coords=100):
#     """Plot multiple trajectories on the field."""
#     for start_point, end_point in zip(start_points, end_points):
#         trajectory_df = generate_trajectory(start_point, end_point, peak_height, num_coords)
#         fig.add_trace(go.Scatter3d(
#             y=trajectory_df['x'],
#             x=trajectory_df['y'],
#             z=trajectory_df['z'],
#             mode='lines',
#             line=dict(color='red', width=4)
#         ))
#         fig.add_trace(go.Scatter3d(
#             y=[trajectory_df['x'].iloc[0], trajectory_df['x'].iloc[-1]],
#             x=[trajectory_df['y'].iloc[0], trajectory_df['y'].iloc[-1]],
#             z=[trajectory_df['z'].iloc[0], trajectory_df['z'].iloc[-1]],
#             mode='markers',
#             marker=dict(size=3, color='red')
#         ))

# def create_soccer_field_plot():
#     """Create a 3D soccer field plot with trajectories."""
#     field_df = create_field_df()

#     # Plot the field lines
#     fig = px.line_3d(
#         data_frame=field_df, x='x', y='y', z='z', line_group='line_group', color='color',
#         color_discrete_map={'field': '#FFFFFF'}  # White color for field lines
#     )

#     # Add the green field area
#     fig.add_trace(go.Mesh3d(
#         x=[0, WIDTH, WIDTH, 0],
#         y=[0, 0, LENGTH, LENGTH],
#         z=[0, 0, 0, 0],
#         color='rgb(0, 128, 0)',  # Semi-transparent green color for the field
#         opacity=0.5
#     ))

#     # Add the center circle and goalposts
#     fig.add_trace(create_center_circle())
#     for goalpost in create_goalposts():
#         fig.add_trace(goalpost)

#     # Adjust the layout with correct aspect ratio and camera settings
#     max_dimension = max(WIDTH, LENGTH, GOAL_HEIGHT)
#     fig.update_layout(
#         scene=dict(
#             aspectmode="manual",
#             aspectratio=dict(x=1, y=1, z=0.125),  # Reduce z aspect ratio for better visual appearance
#             xaxis=dict(
#                 range=[-10, max_dimension + 10],  # Set range for x-axis
#                 visible=False
#             ),
#             yaxis=dict(
#                 range=[-10, max_dimension + 10],  # Set range for y-axis
#                 visible=False
#             ),
#             zaxis=dict(
#                 range=[0, 15],  # Adjust the Z-axis range
#                 visible=False
#             ),
#             camera=dict(
#                 eye=dict(x=0.34, y=0, z=0.45)  # Closer position for zoom
#             ),
#         ),
#         paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
#         plot_bgcolor='rgba(0,0,0,0)',
#         showlegend=False,
#     )

#     return fig

# def main_3D_pitch(start_points,end_points):
#     # st.title("3D Soccer Field Trajectory Visualization")

#     fig = create_soccer_field_plot()

#     # Plot the trajectories
#     plot_trajectories(fig, start_points, end_points, peak_height=5, num_coords=100)

#     # Display the plot
#     st.plotly_chart(fig)


import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Soccer field dimensions (in meters)
WIDTH = 80  # Width of the field
LENGTH = 120  # Length of the field
GOAL_HEIGHT = 2.44  # Standard goal height
PENALTY_AREA_WIDTH = 40.3
PENALTY_AREA_DEPTH = 16.5
GOAL_AREA_WIDTH = 18.32
GOAL_AREA_DEPTH = 5.5
GOAL_WIDTH = 7.32  # Standard width of a soccer goal

def create_field_df():
    """Create dataframes for different parts of the soccer field."""
    field_perimeter_bounds = [[0, 0, 0], [WIDTH, 0, 0], [WIDTH, LENGTH, 0], [0, LENGTH, 0], [0, 0, 0]]
    field_df = pd.DataFrame(field_perimeter_bounds, columns=['x', 'y', 'z'])
    field_df['line_group'] = 'field_perimeter'
    field_df['color'] = 'field'

    half_field_bounds = [[0, LENGTH / 2, 0], [WIDTH, LENGTH / 2, 0]]
    half_df = pd.DataFrame(half_field_bounds, columns=['x', 'y', 'z'])
    half_df['line_group'] = 'half_field'
    half_df['color'] = 'field'

    left_penalty_df = create_rectangle_df((WIDTH - PENALTY_AREA_WIDTH) / 2, 0, PENALTY_AREA_WIDTH, PENALTY_AREA_DEPTH, 'left_penalty_area')
    right_penalty_df = create_rectangle_df((WIDTH - PENALTY_AREA_WIDTH) / 2, LENGTH - PENALTY_AREA_DEPTH, PENALTY_AREA_WIDTH, PENALTY_AREA_DEPTH, 'right_penalty_area')
    left_goal_df = create_rectangle_df((WIDTH - GOAL_AREA_WIDTH) / 2, 0, GOAL_AREA_WIDTH, GOAL_AREA_DEPTH, 'left_goal_area')
    right_goal_df = create_rectangle_df((WIDTH - GOAL_AREA_WIDTH) / 2, LENGTH - GOAL_AREA_DEPTH, GOAL_AREA_WIDTH, GOAL_AREA_DEPTH, 'right_goal_area')

    return pd.concat([field_df, half_df, left_penalty_df, right_penalty_df, left_goal_df, right_goal_df])

def create_rectangle_df(start_x, start_y, width, height, line_group):
    """Create a dataframe representing a rectangle on the field."""
    rectangle_bounds = [
        [start_x, start_y, 0],
        [start_x + width, start_y, 0],
        [start_x + width, start_y + height, 0],
        [start_x, start_y + height, 0],
        [start_x, start_y, 0]
    ]
    df = pd.DataFrame(rectangle_bounds, columns=['x', 'y', 'z'])
    df['line_group'] = line_group
    df['color'] = 'field'
    return df

def create_center_circle():
    """Create a 3D line trace for the center circle."""
    theta = np.linspace(0, 2 * np.pi, 100)
    x = [(WIDTH / 2) + (9.15 * np.cos(t)) for t in theta]
    y = [(LENGTH / 2) + (9.15 * np.sin(t)) for t in theta]
    z = [0] * 100
    return go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='white', width=2))

def create_goalposts():
    """Create goalpost lines for both ends of the field."""
    goalposts = []

    goalposts.extend([
        go.Scatter3d(x=[(WIDTH / 2) - (GOAL_WIDTH / 2), (WIDTH / 2) - (GOAL_WIDTH / 2)], y=[LENGTH, LENGTH], z=[0, GOAL_HEIGHT], mode='lines', line=dict(color='black', width=4)),
        go.Scatter3d(x=[(WIDTH / 2) + (GOAL_WIDTH / 2), (WIDTH / 2) + (GOAL_WIDTH / 2)], y=[LENGTH, LENGTH], z=[0, GOAL_HEIGHT], mode='lines', line=dict(color='black', width=4)),
        go.Scatter3d(x=[(WIDTH / 2) - (GOAL_WIDTH / 2), (WIDTH / 2) + (GOAL_WIDTH / 2)], y=[LENGTH, LENGTH], z=[GOAL_HEIGHT, GOAL_HEIGHT], mode='lines', line=dict(color='black', width=4))
    ])

    goalposts.extend([
        go.Scatter3d(x=[(WIDTH / 2) - (GOAL_WIDTH / 2), (WIDTH / 2) - (GOAL_WIDTH / 2)], y=[0, 0], z=[0, GOAL_HEIGHT], mode='lines', line=dict(color='black', width=4)),
        go.Scatter3d(x=[(WIDTH / 2) + (GOAL_WIDTH / 2), (WIDTH / 2) + (GOAL_WIDTH / 2)], y=[0, 0], z=[0, GOAL_HEIGHT], mode='lines', line=dict(color='black', width=4)),
        go.Scatter3d(x=[(WIDTH / 2) - (GOAL_WIDTH / 2), (WIDTH / 2) + (GOAL_WIDTH / 2)], y=[0, 0], z=[GOAL_HEIGHT, GOAL_HEIGHT], mode='lines', line=dict(color='black', width=4))
    ])

    return goalposts

def generate_trajectory(start_point, end_point, peak_height=10, num_coords=100, trajectory_type='parabolic'):
    """Generate a trajectory (parabolic or linear) between start and end points."""
    shot_start_x, shot_start_y, start_z = start_point
    hoop_x, hoop_y, end_z = end_point

    if trajectory_type == 'parabolic':
        distance_x = hoop_x - shot_start_x
        a = -4 * peak_height / (distance_x ** 2)

        shot_path_coords = []
        for index, x in enumerate(np.linspace(shot_start_x, hoop_x, num_coords + 1)):
            z = a * (x - (shot_start_x + hoop_x) / 2) ** 2 + peak_height
            y = shot_start_y + (hoop_y - shot_start_y) * (index / num_coords)
            shot_path_coords.append([x, y, z])

        shot_path_coords[0][2] = start_z  # Ensure start z is as specified
        shot_path_coords[-1][2] = end_z  # Ensure end z is as specified

    elif trajectory_type == 'linear':
        shot_path_coords = []
        for index, x in enumerate(np.linspace(shot_start_x, hoop_x, num_coords + 1)):
            y = shot_start_y + (hoop_y - shot_start_y) * (index / num_coords)
            z = start_z + (end_z - start_z) * (index / num_coords)
            shot_path_coords.append([x, y, z])

    return pd.DataFrame(shot_path_coords, columns=['x', 'y', 'z'])

def plot_trajectories(fig, start_points, end_points, trajectory_type='parabolic', peak_height=10, num_coords=100):
    """Plot multiple trajectories on the field."""
    for start_point, end_point in zip(start_points, end_points):
        trajectory_df = generate_trajectory(start_point, end_point, peak_height, num_coords, trajectory_type)
        fig.add_trace(go.Scatter3d(
            y=trajectory_df['x'],
            x=trajectory_df['y'],
            z=trajectory_df['z'],
            mode='lines',
            line=dict(color='red', width=4)
        ))
        fig.add_trace(go.Scatter3d(
            y=[trajectory_df['x'].iloc[0], trajectory_df['x'].iloc[-1]],
            x=[trajectory_df['y'].iloc[0], trajectory_df['y'].iloc[-1]],
            z=[trajectory_df['z'].iloc[0], trajectory_df['z'].iloc[-1]],
            mode='markers',
            marker=dict(size=3, color='red')
        ))

def create_soccer_field_plot():
    """Create a 3D soccer field plot with trajectories."""
    field_df = create_field_df()

    fig = px.line_3d(
        data_frame=field_df, x='x', y='y', z='z', line_group='line_group', color='color',
        color_discrete_map={'field': '#FFFFFF'}
    )

    fig.add_trace(go.Mesh3d(
        x=[0, WIDTH, WIDTH, 0],
        y=[0, 0, LENGTH, LENGTH],
        z=[0, 0, 0, 0],
        color='rgb(0, 128, 0)',
        opacity=0.5
    ))

    fig.add_trace(create_center_circle())
    for goalpost in create_goalposts():
        fig.add_trace(goalpost)

    max_dimension = max(WIDTH, LENGTH, GOAL_HEIGHT)
    fig.update_layout(
        scene=dict(
            aspectmode="manual",
            aspectratio=dict(x=1, y=1, z=0.125),
            xaxis=dict(
                range=[-10, max_dimension + 10],
                visible=False
            ),
            yaxis=dict(
                range=[-10, max_dimension + 10],
                visible=False
            ),
            zaxis=dict(
                range=[0, 15],
                visible=False
            ),
            camera=dict(
                eye=dict(x=0.34, y=0, z=0.45)
            ),
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
    )

    return fig

def main_3D_pitch(start_points, end_points, trajectory_type='linear'):
    st.title("3D Soccer Field Trajectory Visualization")

    fig = create_soccer_field_plot()

    plot_trajectories(fig, start_points, end_points, trajectory_type=trajectory_type, peak_height=5, num_coords=100)

    st.plotly_chart(fig)
