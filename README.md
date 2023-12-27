# facial-recognition-project
Facial recognition Python project that can assist with finding missing persons.

v1 of simple facial recognition.
* Currently displaying a known and unknown face to compare if they are the same person
* Using image of Ryan Reynolds and Ryan Gosling for comparison
* Landmark points are added to show facial structure differences

### Virtual Environment Setup
```commandline
pip3 install virtualenv
python3 -m venv venv
source venv/bin/activate
```

### Running the project
Note: the installation command may take a while as dlib is a very large library
```commandline
pip install -r requirements.txt
python main.py
```

### Future Expansion
If this project is expanded in the future, a v2 will be implemented and updated in the README.

This project current serves as a simple facial recognition software. However, this project can serve as a tool to assist
when provided with a missing persons database and video footage / images in order to help locate missing persons.