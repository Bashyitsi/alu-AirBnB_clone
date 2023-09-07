alu-AirBnB_clone - Console Project
**Project Overview:**
This project is part of the ALU Software Engineering program. It marks the initial step in building a fully functional web application - an AirBnB clone. The primary focus here is to create a custom command-line interface for data management and establish the base classes for data storage.

**Environment:**
- This project is developed and tested on Ubuntu 20.04 using Python 3.4.3.
- Code editors used include Emacs, Vi, and Visual Studio Code.

**Installation:**
1. Clone this repository:
   ```
   git clone https://github.com/Bashyitsi/alu-AirBnB_clone.git
   ```
2. Access the AirBnb directory: `AirBnB_clone`
3. To run the console interactively, execute: `./console` and enter commands.
4. To run the console non-interactively, use: `echo "" | ./console.py`

**Functionalities of the Command Interpreter:**
- Create a new object (e.g., User or Place).
- Retrieve an object from a file, a database, etc.
- Perform operations on objects (e.g., count, compute stats).
- Update attributes of an object.
- Destroy an object.

**Console and Command Usage:**

The console operates like a Unix shell-like command line interface, powered by the Python `Cmd` module. It displays a prompt and awaits user input.

Commands:
- Display command help: `(hbnb) help`
- Create an object (prints its ID): `(hbnb) create`
- Destroy an object: `(hbnb) destroy` or `(hbnb) .destroy()`
- Show an object: `(hbnb) show` or `(hbnb) .show()`
- Show "all" objects or instances of a class: `(hbnb) all` or `(hbnb) all`
- Run the console: `./console.py`
- Quit the console: `(hbnb) quit`

**Documented Commands:**
- `EOF`
- `all`
- `count`
- `create`
- `destroy`
- `help`
- `quit`
- `show`
- `update`

**Class Models Used:**

| File           | Description                               | Attributes                                           |
| -------------- | ----------------------------------------- | ---------------------------------------------------- |
| `base_model.py`| The BaseModel class inherited by others  | `id`, `created_at`, `updated_at`                     |
| `user.py`      | User class storing user-related info     | `email`, `password`, `first_name`, `last_name`       |
| `city.py`      | City class storing city-specific info    | `state_id`, `name`                                   |
| `state.py`     | State class storing state-specific info  | `name`                                               |
| `place.py`     | Place class storing detailed unit info   | `city_id`, `user_id`, `name`, `description`, ...    |
| `review.py`    | Review class storing customer reviews    | `place_id`, `user_id`, `text`, `opinions`           |
| `amenity.py`   | Amenity class storing amenity info       | `name`                                               |

**Tests:**

All code is rigorously tested using the `unittest` module. The tests for the classes are located in the `test_models` folder, while the tests for the console script can be found in the main `tests` folder.

**Authors:**
- Ochan Lokidormoi (GitHub: Ochan-LOKIDORMOI], Email: o.lokidormo@alustudent.com)
- Shema Bashyitsi Pacifique (Github: [Bashyitsi], Email: p.shema1@alustudent.com)
