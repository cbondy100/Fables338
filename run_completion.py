# check out this for more info
# https://beta.openai.com/docs/guides/fine-tuning
# particularly, there's a command on there that shows you how to set your api key in the command line so that this script works

import os
import openai

input = "Fables-Story-Input: In a field one summer's day a Grasshopper was hopping about, chirping and singing to its heart's content.  An Ant passed by, bearing along with great toil an ear of corn he was taking to the nest. \"Why not come and chat with me,\" said the Grasshopper,\"instead of toiling and moiling in that way?\" \"I am helping to lay up food for the winter,\" said the Ant, \"and recommend you to do the same.\" \"Why bother about winter?\" said the Grasshopper; we have got plenty of food at present.\"  But the Ant went on its way and continued its toil.  When the winter came the Grasshopper had no food and found itself dying of hunger, while it saw the ants distributing every day corn and grain from the stores they had collected in the summer. ->"
#input = "Fables-Story-Input: Jared is a gamer. He loves playing video games with his friends, but he is also extremely competitive and doesn't like losing. One time, his friend beat him in Call of Duty, and he broke his friend's tv! ->"

input_tokens = len(input.split(' '))

openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Completion.create(
  model="davinci:ft-personal-2022-12-05-01-31-17",
  prompt=input,
  max_tokens=1000,
  temperature=0.9,
  top_p=0.3,
  stop="THEEND"
))