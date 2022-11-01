#extract metadata from webp images
from PIL import Image
from PIL.ExifTags import TAGS

image = Image.open("ImageGenerations/generation-0HxY8mvKWeH9Pj50P4Rcf2FQ.webp")
exifdata = image.getexif()

for tagid in exifdata:

    tagename = TAGS.get(tagid, tagid)
    value = exifdata.get(tagid)
    print(f"{tagname:25}: {value}")

'''
[{'id': 'generation-j2F2CY4QVYMbcTF7GFJlN7H7', 'object': 'generation', 'created': 1667321250, 'generation_type': 'ImageGeneration', 'generation': {'image_path': 'https://openailabsprodscus.blob.core.windows.net/private/user-hCRlhobLkh54a9o0DPxDEjSs/generations/generation-j2F2CY4QVYMbcTF7GFJlN7H7/image.webp?st=2022-11-01T15%3A48%3A33Z&se=2022-11-01T17%3A46%3A33Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-11-01T15%3A48%3A43Z&ske=2022-11-08T15%3A48%3A43Z&sks=b&skv=2021-08-06&sig=MBmP1HgtsIU0WnuqtmHFHHS1Q7%2BwKYa1NCsoU8gw45Q%3D'}, 'task_id': 'task-Z279gNbcIAuHlj5ucgdtuZlI', 'prompt_id': 'prompt-IgUEBpMSzfS4o7qDffNPo4YQ', 'is_public': False}, 
{'id': 'generation-OeJHqjYD8rWJCZ1NmCjt3Z7e', 'object': 'generation', 'created': 1667321250, 'generation_type': 'ImageGeneration', 'generation': {'image_path': 'https://openailabsprodscus.blob.core.windows.net/private/user-hCRlhobLkh54a9o0DPxDEjSs/generations/generation-OeJHqjYD8rWJCZ1NmCjt3Z7e/image.webp?st=2022-11-01T15%3A48%3A33Z&se=2022-11-01T17%3A46%3A33Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-11-01T15%3A48%3A43Z&ske=2022-11-08T15%3A48%3A43Z&sks=b&skv=2021-08-06&sig=vfyIA2130ugb%2B3iHg4HK1QoKzicSxXf1XQL7GoXl170%3D'}, 'task_id': 'task-Z279gNbcIAuHlj5ucgdtuZlI', 'prompt_id': 'prompt-IgUEBpMSzfS4o7qDffNPo4YQ', 'is_public': False}, 
{'id': 'generation-GCPOAPk3EZXp7GqWPeddPQiO', 'object': 'generation', 'created': 1667321250, 'generation_type': 'ImageGeneration', 'generation': {'image_path': 'https://openailabsprodscus.blob.core.windows.net/private/user-hCRlhobLkh54a9o0DPxDEjSs/generations/generation-GCPOAPk3EZXp7GqWPeddPQiO/image.webp?st=2022-11-01T15%3A48%3A33Z&se=2022-11-01T17%3A46%3A33Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-11-01T15%3A48%3A43Z&ske=2022-11-08T15%3A48%3A43Z&sks=b&skv=2021-08-06&sig=cfFWCXnzBltjLJN7MSXO62iWGgTQI49U1rHu6c98xQQ%3D'}, 'task_id': 'task-Z279gNbcIAuHlj5ucgdtuZlI', 'prompt_id': 'prompt-IgUEBpMSzfS4o7qDffNPo4YQ', 'is_public': False}, 
{'id': 'generation-aoaLmxMlOVw9miQUhTtVI112', 'object': 'generation', 'created': 1667321250, 'generation_type': 'ImageGeneration', 'generation': {'image_path': 'https://openailabsprodscus.blob.core.windows.net/private/user-hCRlhobLkh54a9o0DPxDEjSs/generations/generation-aoaLmxMlOVw9miQUhTtVI112/image.webp?st=2022-11-01T15%3A48%3A33Z&se=2022-11-01T17%3A46%3A33Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-11-01T15%3A48%3A43Z&ske=2022-11-08T15%3A48%3A43Z&sks=b&skv=2021-08-06&sig=anPdwB2NDBRWLRgBigEHjlO2L8kd%2BxePPwCVQcy3wfg%3D'}, 'task_id': 'task-Z279gNbcIAuHlj5ucgdtuZlI', 'prompt_id': 'prompt-IgUEBpMSzfS4o7qDffNPo4YQ', 'is_public': False}]
'''