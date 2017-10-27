def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        side_area += 2 * top_area
        return side_area
    else:
        return "nothing"
test1=cylinder_surface_area(10,3,4)
print(test1)
