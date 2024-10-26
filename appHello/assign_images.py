from app_settings import *
import sys

#sources_list = []


def process_sources(file_path):

    # Open and read the file
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split(":")
            if parts:
                processed_part = parts[0].replace("'", "").strip()
                sources_list.append(processed_part)

    return sources_list


#infinite scroll repeative forever


# Example usage
result = process_sources(file_path)
print(result)


icon = [
    "nytimes.png","cnn.png","bbc.png","fox.png","washingtonpost.png",
    "abcnews.png","nbcnews.png", "cbsnews.png","buzzfeed.png",
    "vice.png","slate.png","vox.png","salon.png", "theintercept.png",
    "theatlantic.png","thenewyorker.png","time.png","businessinsider.png",
    "fortune.png","cnbc.png","latimes.png","democracynow.png","commondreams.png",
    "aljazeera.png","propublica.png","novaramedia.png","guardian.png",
]
