# Marker

## Prerequisites
- install requirements as described in readme
- download and extract clips from [Kaggle](https://www.kaggle.com/competitions/dfl-bundesliga-data-shootout/data?select=clips) into `./input/clips/`
- create director `./output/markings/`

## Running Marker

```sh
python marker <VIDEO_ID>
```
where `<VIDEO_ID>` is `./input/clips/<VIDEO_ID>.mp4`

Below are the controls for the markings window

| Key     | Command                   |
|---------|---------------------------|
| ESC     | Exit the window           |
| 1       | Change to marking team 1 players |
| 2       | Change to marking team 2 players |
| g       | change to marking goalie for team 1 |
| h       | change to marking goalie for team 2 |
| b       | change to marking the ball |
| ,       | move to the previous frame |
| .       | move to the next frame |

This will generate a new file `./output/markings/<VIDEO_ID>.json` with the marking information

## TODO

- Add the ability to remove previous markings
- load the marking information that was previously saved
