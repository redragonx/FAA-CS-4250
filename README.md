NGenCACD
=========
Python based airplane collision avoidance system for the masses. Hardware to be made.

Navigation
=================
[NGenCACD](#ngencacd) |
[Purpose](#purpose) |
[Screenshot](#screenshot) |
[Team](#team) |
[Configuration](#configuration) |
[Folder Structure](#Folder Structure) |
[Running the program](#Running the program) |

Purpose
====================
This project aims to create collision-avoidance system for the cockpits of all aircraft. The system will receive real-time radar data and need to continuously calculate if a collision is likely, and give several different levels of warning. The system will need to deal with the entire range of fixed- and rotary-wing aircraft.

Team
=====================
<ul>
<li>Abel Amadou</li> 
<li>Dean Bailey</li>
<li>Chris Benda</li> 
<li>Ben Boudra</li>
<li>Stephen Chavez</li>
<li>Josh Coyle</li>
<li>Jesse Nelson</li>
<li>John Qualls</li>
</ul>

Screenshot
==============================
![Picture](http://i.imgur.com/vUA89JK.png)

Configuration
==============================
This project uses Python standards for folder stucturing and is recommended that you use an IDE like IntelliJ IDEA 15. You can use the import from existing sources to create a IntelliJ IDEA project for NGenCACD. This codebase will require Python 2.7. Not tested with higher versions. NGenCACD requires Pyglet (a Python audio library). Please install it via your IDE, unix/linux package manager or PIP tool.

Folder Structure
==============================
<pre>
.
├── computation_package
│   ├── collision_detection.py
│   └── __init__.py
├── Driver.py
├── FAA-CS-4250.iml
├── io_package
│   ├── ADS_ANTENNA.py
│   ├── ADS_io.py
│   ├── audio.py
│   ├── __init__.py
│   ├── Soundfiles
│   │   ├── adjustvert2.wav
│   │   ├── adjustvert.wav
│   │   ├── clear.wav
│   │   ├── climb2.wav
│   │   ├── climbcross.wav
│   │   ├── climbnow.wav
│   │   ├── climb.wav
│   │   ├── crossclimb.wav
│   │   ├── crossdescend.wav
│   │   ├── data error.wav
│   │   ├── descend2.wav
│   │   ├── descendcross.wav
│   │   ├── descendnow.wav
│   │   ├── descend.wav
│   │   ├── eight.wav
│   │   ├── five.wav
│   │   ├── four.wav
│   │   ├── incrclimb.wav
│   │   ├── incrdescend.wav
│   │   ├── incrdescent.wav
│   │   ├── __init__.py
│   │   ├── maintaincross.wav
│   │   ├── maintain.wav
│   │   ├── monitor.wav
│   │   ├── nine.wav
│   │   ├── noclimb.wav
│   │   ├── nodescend.wav
│   │   ├── one.wav
│   │   ├── seven.wav
│   │   ├── six.wav
│   │   ├── testfail.wav
│   │   ├── testok.wav
│   │   ├── three.wav
│   │   ├── traffic2.wav
│   │   ├── traffic.wav
│   │   ├── two.wav
│   │   ├── you_entered.wav
│   │   └── zero.wav
│   └── user_keypad.py
├── plane_controller
│   ├── data_verification.py
│   ├── __init__.py
│   ├── OurTest.py
│   ├── plane_ctrl.py
│   ├── plane.py
│   └── system_alert.py
└── test
    ├── CovertBack.py
    ├── __init__.py
    ├── SystemTest1
    ├── test_ADS_io.py
    ├── test_audio.py
    ├── test_collision_detection.py
    ├── test_data_verification.py
    ├── test_plane_controller.py
    ├── test_system_alert.py
    └── test_user_keypad.py

5 directories, 63 files
</pre>

This should be your folder structure before running any commands.


Running the Program
===================
<ol>
<li>Run the invidial tests in the test folder or Driver.py for a overall system test</li>
</ol>

The program should run now. Yay!
