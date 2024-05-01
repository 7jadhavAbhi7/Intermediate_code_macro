# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:43:05 2024

@author: Abhishek
"""

class MacroProcessor:
    def __init__(self):
        self.macro_definitions = {}
        self.pass_1_output = []
        self.pass_2_output = []

    def pass_1(self, code):
        lines = code.split('\n')
        macro_name = None
        macro_content = []

        for line in lines:
            if line.strip().startswith("MACRO"):
                macro_name = line.split()[1]
            elif line.strip().startswith("MEND"):
                self.macro_definitions[macro_name] = macro_content[:]
                macro_name = None
                macro_content = []
            elif macro_name:
                macro_content.append(line)
            else:
                self.pass_1_output.append(line)
                
    def pass_2(self):
        for line in self.pass_1_output:
            tokens = line.split()
            if tokens:
                if tokens[0] in self.macro_definitions:
                    macro_content = self.macro_definitions[tokens[0]]
                    parameters = tokens[1:]
                    for macro_line in macro_content:
                        for i, param in enumerate(parameters):
                            macro_line = macro_line.replace(f'PAR{i+1}', param)
                        self.pass_2_output.append(macro_line)
                else:
                    self.pass_2_output.append(line)
            else:
                self.pass_2_output.append(line)
    def generate_intermediate_code(self):
        code = '\n'.join(self.pass_2_output)
        print("Intermediate Code:")
        print(code)

if __name__ == "__main__":
    code = """
    STORE P
    LOAD Q
    MACRO PCG
    LOAD m
    ADD n
    MEND
    LOAD H
    LOAD K
    MACRO ADDi PAR
    LOAD A
    STORE PAR
    MEND
    DIV R
    MACRO ADDii V1, V2, V3
    STORE V2
    ADDi 12
    ADDi 7
    LOAD V1
    LOAD V3
    MEND
    PCG
    ADDii Q1, Q2, Q3
    ADDi w
    END
    """

    processor = MacroProcessor()
    processor.pass_1(code)
    processor.pass_2()
    processor.generate_intermediate_code()
