def GetAPIKey(index: int) -> str:
    """
    A function to retrieve an API key based on the provided index.

    Args:
        index (int): The index of the API key to retrieve from the list.

    Returns:
        str: The API key corresponding to the provided index.
    """

    # vishnupouley@gmail.com

    # api_key = [
    #     "AIzaSyACos2qLbo04Xcuuv8HplDg3TAOhQrwKtI",
    #     "AIzaSyC8g_OL7Fvjj-QWZKnv8A4AShN3yemiZ-E",
    #     "AIzaSyDCkqQfYOYQojSXw_AE4PQyH4tleJZlwps",
    # ]

    # vishnupouleymz@gmail.com

    api_key = [
        "AIzaSyAJNQq4qc-YTo9HJ8LRtF2UIG9TWntL8Bg",
        "AIzaSyAirgiWshMQNgOM1DGjtt1SaSn_yhJQCuU",
        "AIzaSyDRSW4UhDNynLJS9pHnA9BlovnMkr_EffY",
    ]
    return api_key[index - 1]
