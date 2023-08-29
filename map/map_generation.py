import folium
import base64


def embedded_image_icon(img_path):
    encoded = base64.b64encode(open(img_path, 'rb').read()).decode()
    return f"data:image/png;base64,{encoded}"


def generate_map(hazards_data):
    base_map = folium.Map(location=[hazards_data[0][0], hazards_data[0][1]], zoom_start=13)
    for lat, lon, hazard_type, img_path in hazards_data:
        icon_data = embedded_image_icon(img_path)
        custom_icon = folium.CustomIcon(icon_image=icon_data, icon_size=(28, 30))
        folium.Marker([lat, lon], tooltip=hazard_type, icon=custom_icon).add_to(base_map)
    return base_map


if __name__ == "__main__":
    hazards_data = [
        (31.7683, 35.2137, 'Pothole', 'icon.png'),
        (31.7684, 35.2138, 'Construction', 'icon.png'),
    ]
    m = generate_map(hazards_data)
    m.save("maps/hazards_map.html")
