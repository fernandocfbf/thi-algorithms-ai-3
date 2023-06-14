class Reader():

    def read_text_file(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.read()
            return lines
    
    def txt_to_matrix(self, lines):
        lines = lines.split('\n')
        matrix = []
        for line in lines:
            row = [int(character) for character in line]
            matrix.append(row)
        return matrix
    
