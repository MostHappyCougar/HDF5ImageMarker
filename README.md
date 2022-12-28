# HDF5ImageMarker
Util to marking key objects of the images and write it to the DHF5 as dataset in real time
### Architecture:
![hl_architecture](https://user-images.githubusercontent.com/104580123/209446611-b075d657-fa96-4ac8-b23f-6c005d78dedf.jpg)

### Error codes:
#### Code Convention
> [error_type]_[error_severity][code]
#### error_types
> `conf` - config error

> `imp` - import error
#### error severity
> `err` - error
#### Config Errors
>imh_h or img_w is lower than zero: `conf_err01`

>imh_h or img_w is not integer: `conf_err011`

>imh_h or img_w is not filled: `conf_err012`

>window_size_h or window_size_w is lower than zero: `conf_err02`

>source_folder begins with space: `conf_err04`

>source_folder doesn't exist: `conf_err05`

>output_folder begins with space: `conf_err06`

>output_folder doesn't exist: `conf_err07`

>file_name is empty or starts with space: `conf_err11`

>dataset_name is empty or starts with space: `conf_err12`

>write_mode is empty or equals no 'a' or 'w': `conf_err13`
#### Importing Errors
>no subdirectory in source_folder of no content there: `imp_err01`
