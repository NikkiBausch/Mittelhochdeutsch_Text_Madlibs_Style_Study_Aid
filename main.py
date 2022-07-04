import os
import json


class create_German_Excerpt:
   path= "./templates"
   def __init__(self, parts_of_speech, template):
     self.template = template
     self.parts_of_speech = parts_of_speech
     self.user_input = []
     self.text = None
@classmethod
def from_json(cls, name, path=None):
    if not path:
      path = cls.path
    fpath = os.path.join(path, name)
    with open(fpath, "r") as f:
      data = json.load(f)
    excerpt = cls(**data)
    return excerpt

def user_answers(self):
    print("Please provide the following words: ")
    for desc in self.parts_of_speech:
      ui = input(desc + "")
      self.user_input.append(ui)
    return self.user_input

def build_text(self):
    self.text = self.template.format(*self.user_input)
    return self.text

def display_text(self):
    print(text)

def select_template():
  print("Select a text from the following list: ")
  templates = os.listdir(create_German_Excerpt)
  template = input(str(templates) + " ")
  return template

temp_name = select_template()
excerpt = create_German_Excerpt.from_json(temp_name)
words = excerpt.user_answers()
text = excerpt.build_text()
excerpt.display_text()



    
