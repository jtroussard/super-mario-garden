import math


def degree_to_slope(degrees):
    radians = math.radians(degrees - 90)

    rise = math.sin(radians)
    run = math.cos(radians)

    return (rise, run)


# Test with various degree values
angle_values = [30, 45, 60, 90, 135, 180, 270, 360]
for angle in angle_values:
    slope_value = degree_to_slope(angle)
    print(
        f"Angle: {angle}°, Slope as fraction: {slope_value[0]:.4f}/{slope_value[1]:.4f}, \
            Slope as decimal: {slope_value[0]/slope_value[1]:.4f}"
    )


def calculate_face_midpoint(entity_surface_object):
    angle_radians = math.radians(entity_surface_object.rot - 90)
    face_length = entity_surface_object.rect.width
    face_midpoint_x = entity_surface_object.rect.centerx + (face_length / 2) * math.cos(
        angle_radians
    )
    face_midpoint_y = entity_surface_object.rect.centery - (face_length / 2) * math.sin(
        angle_radians
    )
    return face_midpoint_x, face_midpoint_y
