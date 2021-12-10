"""Config file"""

config_store = {
    "data": [
        {
            "file_regex": "Asia\sProd.*"
        },
        {
            "file_regex": "NA\sProd.*"
        },
        {
            "file_regex": "NA\sPreview.*"
        }
    ],
    "put": "store/destination/Combined.csv"
}


bad_config = {}

COMBINED_CSV = "store/destination/Combined.csv"
FILE_DIRECTORY = "store/test_files/Engineering_Test_Files"
