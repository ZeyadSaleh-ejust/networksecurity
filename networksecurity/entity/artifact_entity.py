from dataclasses import dataclass # for class varialbes only

@dataclass
class DataIngestionArtifacts:
    trained_file_path: str
    test_file_path: str