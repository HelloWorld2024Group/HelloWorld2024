from app_settings import *

def process_sources(file_path):

    # Open and read the file
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split(":")
            if parts:
                processed_part = parts[0].replace("'", "").strip()
                sources_list.append(processed_part)

    return sources_list

# Example usage
result = process_sources(file_path)
print(result)


icon_names_list = [
    "images/nytimes.png","images/cnn.png","images/bbc.png","images/fox.png","images/washingtonpost.png",
    "images/abcnews.png","images/nbcnews.png", "images/cbsnews.png","images/buzzfeed.png",
    "images/vice.png","images/slate.png","images/vox.png","images/salon.png", "images/theintercept.png",
    "images/theatlantic.png","images/thenewyorker.png","images/time.png","images/businessinsider.png",
    "images/fortune.png","images/cnbc.png","images/latimes.png","images/democracynow.png","images/commondreams.png",
    "images/aljazeera.png","images/propublica.png","images/novaramedia.png","images/guardian.png",
]
