# Globalmark
A Text-based CPU benchmark aimed to be multiplatform with every Python-compatible device with shared scores.

<b>Features</b>

- Perform basic integer operations as sums, subtractions and multiplications as well as floating point.
- Single-Core and Multi-Core modes to up to 8 cores of utilization.
- A stress test mode.
- Online scoreboard of tests uploaded.

<b>Usage</b>

By default it would launch with Kivy framework graphics unless specified with the nogui argument on the CMD.

Example: ~./main.py nogui

<hr>

![Captura desde 2023-03-21 12-02-44](https://user-images.githubusercontent.com/84983282/226587688-89725754-e0a8-49ff-a682-df492b26ea26.png)

![Screenshot_20221221_005213](https://user-images.githubusercontent.com/84983282/208788188-1a79e474-1906-41c5-b76b-424a7b0bf00b.png)

![Captura](https://user-images.githubusercontent.com/84983282/208789754-c5373f65-f165-4e1d-a1ef-906fbb9cb8b9.PNG)

| ![Screenshot_20221221-010612](https://user-images.githubusercontent.com/84983282/208790639-5c2a4a47-70c8-4c5b-b02b-99fbbf686fed.png) | ![Screenshot_20221221-010542](https://user-images.githubusercontent.com/84983282/208790643-b56511ee-d00e-42da-9cf0-750269b89606.png) |
| :-----------: | :-----------: |

# Changelog

<h2>v4.2.0</h2>

<b>Features</b>

- Added database uploads as a guest for GUI mode.
- Code optimizations.

<b>Bugs</b>

- Database not working on android.

<hr>

<h2>v4.1.10</h2>

<b>Features</b>

- Now the stress test won't let run the test without adding more than 0 cores.
- Code optimizations.

<b>Bugs</b>

- TBD

<hr>

<h2>v4.1.9</h2>

<b>Features</b>

- GUI improvements.
- Code optimizations.

<b>Bugs</b>

- TBD

<hr>

<h2>v4.1.8</h2>

<b>Features</b>

- Rounded the amount of time presented for the tests.

<b>Bugs</b>

- TBD

<hr>

<h2>v4.1.7</h2>

<b>Features</b>

- GUI improvements.
- Added argument for CMD only mode.

<b>Bugs</b>

- TBD

<hr>

<h2>v4.1.6</h2>

<b>Features</b>

- Fixed last GUI bug after doing stress test.

<b>Bugs</b>

- TBD

<hr>

<h2>v4.1.5</h2>

<b>Features</b>

- Fixed a bug where the app would crash when opening and closing the single and multicore benchmark without running the test.

<b>Bugs</b>

- GUI bug after running stress test.

<hr>

<h2>v4.1.4</h2>

<b>Features</b>

- GUI improvements.

<b>Bugs</b>

- Bug where the app would crash when opening and closing the single and multicore benchmark without running the test.
- GUI bug after running stress test.

<hr>

<h2>v4.1.3</h2>

<b>Features</b>

- GUI improvements.

<b>Bugs</b>

- TBD

<hr>

<h2>v4.1.2</h2>

<b>Features</b>

- GUI improvements.
- Fixed last bug on stress test mode where threads would not end.

<b>Bugs</b>

- TBD

<hr>

<h2>v4.1.1</h2>

<b>Features</b>

- GUI improvements.
- Fixed blank scoreboard screen and disabled due to WiP.

<b>Bugs</b>

- On GUI mode every stress test would make the amount of threads introduced execute without ending.

<hr>

<h2>v4.1.0</h2>

<b>Features</b>

- Renamed project from Globalbench to Globalmark.
- GUI added (WiP).

<b>Bugs</b>

- On GUI mode every stress test would make the amount of threads introduced execute without ending.
- Blank screen every time the Scoreboard is selected.

<hr>

<h2>v4.0.4</h2>

<b>Features</b>

- UI improvements.

<b>Bugs</b>

- TBD

<hr>

<h2>v4.0.3</h2>

<b>Features</b>

- Added a legacy mode to be able to use the benchmark without having the needed libraries.
- Fixed last bug where the prompt would keep asking for saving the score.
- UI improvements.

<b>Bugs</b>

- TBD

<hr>

<h2>v4.0.2</h2>

<b>Features</b>

- UI improvements.

<b>Bugs</b>

- The prompt to save the score will do it no matter the input.

<hr>

<h2>v4.0.1</h2>

<b>Features</b>

- Fixed last bug where the client won't submit the architecture type to the database.
- UI improvements.

<b>Bugs</b>

- The prompt to save the score will do it no matter the input.

<hr>

<h2>v4.0.0</h2>

<b>Features</b>

- Added integration with cloud database for score uploading!

<b>Bugs</b>

- On every system that it is not x86 it would upload an empty string to the architecture data on the server.
- The prompt to save the score will do it no matter the input.

<hr>

<h2>v3.2.3</h2>

<b>Features</b>

- Fixed the last bug where it is not possible to select any other mode than Single-Core.

<b>Bugs</b>

- TBD

<hr>

<h2>v3.2.2</h2>

<b>Features</b>

- UI improvements.

<b>Bugs</b>

- Bug appears where it doesn't select the correct mode.

<hr>

<h2>v3.2.1</h2>

<b>Features</b>

- Multi core operations disabled on windows systems as they are not handled correctly.
- UI improvements.

<b>Bugs</b>

- Bug appears where it doesn't select the correct mode.

<hr>

<h2>v3.2.0</h2>

<b>Features</b>

- Added support for custom number of cores on the stress test (The more the number of cores introduced the more the load it would have on the system).
- UI improvements.

<b>Bugs</b>

- Multi core modes on windows systems would lead to crash.

<hr>

<h2>v3.1.1</h2>

<b>Features</b>

- Fixed the last bug where the program would not function properly once you do a stress test.

<b>Bugs</b>

- Multi core modes on windows systems would lead to crash.

<hr>

<h2>v3.1.0</h2>

<b>Features</b>

- Added a stress test that utilizes up to 8 cores.
- UI improvements.

<b>Bugs</b>

- Wrong behaviour of the program once you finish a stress test.
- Multi core modes on windows systems would lead to crash.

<hr>

<h2>v3.0.0</h2>

<b>Features</b>

- Now with added support of up to 8 cores.
- UI improvements.

<b>Bugs</b>

- Multi core modes on windows systems would lead to crash.

<hr>

<h2>v2.0.0</h2>

<b>Features</b>

- Multiprocessing implemented! Now it is possible to use a multicore mode to use up to 3 cores at the same time.

<b>Bugs</b>

- Multi core modes on windows systems would lead to crash.

<hr>

<h2>v1.0.0</h2>

<b>Features</b>

- Added more load on the floating point operation.

<b>Bugs</b>

- TBD

<hr>

<h2>v0.3.1</h2>

<b>Features</b>

- UI upgrades (Now everytime the system doesn't provide CPU info it would state "Undisclosed"

<b>Bugs</b>

- TBD

<hr>

<h2>v0.3.0</h2>

<b>Features</b>

- Added some basic system info such as CPU (Sometimes the actual model or just the architecture) and the python version and compiler.

<b>Bugs</b>

- TBD

<hr>

<h2>v0.2.1</h2>

<b>Features</b>

- Added Bash direct support for executing the script.

<b>Bugs</b>

- TBD

<hr>

<h2>v0.2.0</h2>

<b>Features</b>

- Integer and Floating Point operations.
- Shows score and time needed with each type of operation.

<b>Bugs</b>

- TBD
