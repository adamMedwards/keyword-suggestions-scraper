thonimport json

class Exporter:
    def export(self, data, output_file):
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)