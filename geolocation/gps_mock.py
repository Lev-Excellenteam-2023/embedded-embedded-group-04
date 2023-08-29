class LocationMock:
    def __init__(self):
        self.list_of_location = [
            "31.819977, 35.257502",
            "31.819781, 35.248903",
            "31.819589, 35.241886",
            "31.813822, 35.240500",
            "31.806344, 35.232465",
            "31.806856, 35.227144",
            "31.805908, 35.221135",
            "31.807879, 35.210921",
            "31.807077, 35.207059",
            "31.802044, 35.204827",
            "31.799272, 35.200192",
            "31.794895, 35.197961",
            "31.788476, 35.199592"
        ]
        self.index = 0

    def location_mock(self):
        location_str = self.list_of_location[self.index]
        latitude, longitude = map(float, location_str.split(','))
        self.index = (self.index + 1) % len(self.list_of_location)
        return latitude, longitude



# mocker = LocationMock()
# print(mocker.location_mock())
# print(mocker.location_mock())
