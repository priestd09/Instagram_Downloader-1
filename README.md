# Command-Line Instagram Downloader (NO API)
A multithreaded Python script that will download all photos from a public Instagram account **without** their (now bogus) API.

#### Version
    1.0
    
#### Usage
1. Extract the three files into one folder for easier use.
2. From the command line, go to above_folder/src. **Example:**
```sh
cd desktop/instagram_downloader/src
````
3. Run the following command, replacing username with the Instagram username to download from

```sh
python instagram_downloader.py username
````
4. Photos are saved to above_folder/photos/**username**

#### Dependencies
* requests - http://docs.python-requests.org/en/latest/
```sh
$ pip install requests
````

#### Future
* Option to select how many pictures to download.

#### LICENSE

The MIT License (MIT)

Copyright (c) 2016
