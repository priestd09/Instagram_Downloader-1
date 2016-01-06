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

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
