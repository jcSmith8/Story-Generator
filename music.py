### HOPING TO HAVE MUBERT HERE, IF NOT WE WILL HAVE TO ADD A BUNCH OF .MP3 FILES

import replicate
import os
from dotenv import load_dotenv

load_dotenv()

REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

output = replicate.run(
    "riffusion/riffusion:8cf61ea6c56afd61d8f5b9ffd14d7c216c0a93844ce2d82ac1c9ecc9c7f24e05",
    input={"prompt_a": "soothing piano solo"}

)
print(output)