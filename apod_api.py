'''
Library for interacting with NASA's Astronomy Picture of the Day API.
'''
import requests
def main():
    # TODO: Add code to test the functions in this module
    return

URL= "kttps://spi.nasa.gov/planetary/apod"
API_KEY = "qMHfy2eBeX21XIm3F7W76dq5auCApcR53b5fr41x"

def get_apod_info(apod_date):
    """Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.

    Args:
        apod_date (date): APOD date (Can also be a string formatted as YYYY-MM-DD)

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """
    query_params = {
        'api_key': API_KEY,
        'date': apod_date,
        'thumbs': True
    }
    resp_msg = requests.get(URL, params=query_params)
    
    if resp_msg.status_code == requests.codes.ok:
        apod_data = resp_msg.json()
        print("Getting " + apod_date + "APOD information from NASA...success")
        return apod_data
        

def get_apod_image_url(apod_info_dict):
    """Gets the URL of the APOD image from the dictionary of APOD information.

    If the APOD is an image, gets the URL of the high definition image.
    If the APOD is a video, gets the URL of the video thumbnail.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    if apod_info_dict['media_type'] == 'image':
        url = apod_info_dict['hdurl']
    else:
        url = apod_info_dict['thumbnail_url']
    return url

if __name__ == '__main__':
    main()