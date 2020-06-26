#!/usr/bin/python3

import os
import sys

substitute_dict = {}
substitute_dict["a"] = ["á", "ấ", "ā́", "ắ", "ǻ", "ą́", "ǽ"]
substitute_dict["b"] = ["b́"]
substitute_dict["c"] = ["ć", "ć̣", "ḉ"]
substitute_dict["d"] = ["d́"]
substitute_dict["e"] = ["é","ế","ḗ","ė́","ę́","é̩","ɚ́"]
substitute_dict["f"] = ["f́"]
substitute_dict["g"] = ["ǵ"]
substitute_dict["h"] = ["h́"]
substitute_dict["i"] = ["í","ī́","i̇́","į̇́","ḯ"]
substitute_dict["j"] = ["ȷ́"]
substitute_dict["k"] = ["ḱ"]
substitute_dict["l"] = ["ĺ"]
substitute_dict["m"] = ["ḿ"]
substitute_dict["n"] = ["ń"]
substitute_dict["o"] = ["ó","ố","ớ","ṍ","ṓ","ó̩","ǫ́","ǿ","ɔ́"]
substitute_dict["p"] = ["ṕ"]
substitute_dict["q"] = ["q́"]
substitute_dict["r"] = ["ŕ"]
substitute_dict["s"] = ["ś","ṥ"]
substitute_dict["t"] = ["t́"]
substitute_dict["u"] = ["ú","ǘ","ứ","ṹ","ū́","ų́"]
substitute_dict["v"] = ["v́","ʌ́"]
substitute_dict["w"] = ["ẃ"]
substitute_dict["x"] = ["x́"]
substitute_dict["y"] = ["ý","ȳ́"]
substitute_dict["z"] = ["ź"]

substitute_dict["A"] = ["Á", "Ấ", "Ā́", "Ắ", "Ǻ", "Ą́", "Ǽ"]
substitute_dict["B"] = ["B́"]
substitute_dict["C"] = ["Ć", "Ć̣ ", "Ḉ"]
substitute_dict["D"] = ["D́"]
substitute_dict["E"] = ["É","Ế","Ḗ","Ė́","Ę́","É̩","ə́"]
substitute_dict["F"] = ["F́"]
substitute_dict["G"] = ["Ǵ"]
substitute_dict["H"] = ["H́"]
substitute_dict["I"] = ["Í","Ī́","Į́","Ḯ"]
substitute_dict["J"] = ["J́"]
substitute_dict["K"] = ["Ḱ"]
substitute_dict["L"] = ["Ĺ"]
substitute_dict["M"] = ["Ḿ"]
substitute_dict["N"] = ["Ń"]
substitute_dict["O"] = ["Ó","Ố","Ớ","Ṍ","Ṓ","Ó̩","Ǫ́","Ǿ"]
substitute_dict["P"] = ["Ṕ"]
substitute_dict["Q"] = ["Q́"]
substitute_dict["R"] = ["Ŕ"]
substitute_dict["S"] = ["Ṥ", "Ś"]
substitute_dict["T"] = ["T́"]
substitute_dict["U"] = ["Ú","Ǘ","Ứ","Ṹ","Ū́","Ų́"]
substitute_dict["V"] = ["V́", "Ʌ́"]
substitute_dict["W"] = ["Ẃ"]
substitute_dict["X"] = ["X́"]
substitute_dict["Y"] = ["Ý", "Ȳ́"]
substitute_dict["Z"] = ["Ź"]

def main():
    stringToWeirdUp = str(sys.argv[1])
    
    for char in stringToWeirdUp:
        if char in substitute_dict:
            for weirdChar in substitute_dict[char]:
                print(stringToWeirdUp.replace(char, weirdChar, 1))
    
if __name__ == "__main__":
    main()