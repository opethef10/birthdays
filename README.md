# birthdays
- Copy or rename _birthdays.json.example_ to _birthdays.json_ to be able to use your personal data
- Edit _birthdays.json_ file (You can open the file with Notepad) with names and birthdates of your beloved friends with the given format.
- Remember to comply with JSON file format rules. Even if you don't know anything about the JSON format; if you mimic the example file format, you won't have a problem. But pay attention to now have a comma after the last date entry.
- Use **YYYY-MM-DD** iso format while editing. 
- Run `python __main__.py` to print how old your friends are.

## Command Line Arguments
- `python __main__.py -h` for the help text
- `python __main__.py -t` for the information how many days do people have until their 10000th day. 
- `python __main__.py -f [FILE]` for using any other path other than the default path `birthdays.json`. It can be useful if you would like to keep two separate source of birthday information. (Maybe a file called `anniversaries.json` for the anniversary information). Both relative and absolute paths are allowed.
 
## Example Output
Here is an example output from the `birthdays.json.example` file at 12 Oct 2024
![](./screenshot.png)

