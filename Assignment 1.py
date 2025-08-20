import os
import sys
from collections import Counter

class Process_on_file:
    def Read(self,filepath):
        if self.ispresent(filepath):
            file=open(filepath,"r")
            content=file.read()
            print(content)
            file.close()
            return "\n\n ------------CONTENT READ SUCCESSFULLY----------"
        else:
            return "\n Invalid file path"
        
    def Write(self,filepath):
        if self.ispresent(filepath):
            file=open(filepath,"w")
            print("Write from here (Enter ctrl^z in last line for stop): ")
            file.write(sys.stdin.read())
            file.close()
            return "\n\n ------------CONTENT Overwrite SUCCESSFULLY----------"
        else:
            return "\n Invalid file path"
        
    def Append(self,filepath):
        if self.ispresent(filepath):
            file=open(filepath,"a")
            print("Append more information: (Enter ctrl^z in last line for stop): ")
            file.write(sys.stdin.read())
            file.close()
            return "\n\n ------------CONTENT ADDED SUCCESSFULLY----------"
        else:
            return "\n Invalid file path"
        
    def Delete(self,filepath):
        if self.ispresent(filepath):
            os.remove(filepath)
            return "------File Deleted Successfully------"
        else:
            return "\n Invalid file path"
        
    def Lines(self,filepath):
        if self.ispresent(filepath):
            file=open(filepath,"r")
            lines=file.readlines()
            file.close()
            return f"\nNo of Lines: {len(lines)}"
        else:
            return "\n Invalid file path"
    
    def Paragraph(self,filepath):
        if self.ispresent(filepath):
            file=open(filepath,"r")
            paragraphs=len(file.read().strip().split("\n\n"))
            file.close()
            return f"\nNo of Paragraph: {paragraphs}"
        else:
            return "\n Invalid file path"
        
    def CommonWord(self,filepath):
        if self.ispresent(filepath):
            file=open(filepath,"r")
            word_list=file.read().lower().split()
            words=[word.strip(",./[]{}()!`~;?<>'\"*^%#@:") for word in word_list]
            freq_words=Counter(words)
            most_common_word,freq=freq_words.most_common(1)[0]

            file.close()
            return f"\nMost Common Word is {most_common_word} with frequency {freq} "
        else:
            return "\n Invalid file path"


    def ispresent(self,filepath):
        return os.path.exists(filepath)
    

if __name__=="__main__":
    process=Process_on_file()
    filepath=input("Drop your file path: ").strip('"')
    
    operation=input("\nOperation to be perform : \nRead[R]\tOverwite[OW]\tAppend more information[A]\tDelete[D]\tCount Lines[L]\tCount Paragraph[p]\tCount Most common word[MCW]\nChoose one: ")
    match operation:
        case "R": print(process.Read(filepath))
        case "OW":print(process.Write(filepath))
        case "A":print(process.Append(filepath))
        case "D":process.Delete(filepath)
        case "L":print(process.Lines(filepath))
        case "P":print(process.Paragraph(filepath))
        case "MCW":print(process.CommonWord(filepath))
        case _:print("\n\n..........Please choose a valid option.....")
            
