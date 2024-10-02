import openai
import os
import csv
import time
import json

# Set your OpenAI API key here
# openai.api_key = '******************' # aammar
# openai.api_key = '******************' # riotu free
# openai.api_key = '******************' # adel.ammar
openai.api_key = '******************' # riotu paid

nb_commands = 1
# nb_rephrasing = 5

# System prompt which instructs the model to generate commands and then rephrase
generate_command_prompt = """
Generate 16 different commands for a robotic arm, without any other introduction, comment, numbers, nor conclusion. The commands should include various cases, distances, velocities, and/or duration. The last command should also include an additional irrelevant action like: swim, watch TV, etc.
Examples:
    "Extend the arm by 15 centimeters."
    "Rotate the wrist joint clockwise by 45 degrees."
    "Grip the object with 5 kilograms of force."
    "Move to position X:10, Y:20, Z:30."
    "Retract the arm and store in standby position, then smile."
"""
# rephrase_instruction = "Generate 5 different wordings for the following ground robot command, without any other introduction, comment, numbers, nor conclusion."

def issue_commands(prompt, system_prompt=generate_command_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": ""},
        ]
    )
    assistant_reply = response.choices[0].message['content']
    return assistant_reply

# with open("/home/riotu/Dropbox/Adel/ChatGPT/ROSGPT/NL_commands_UAV_base_commands_with_irrelevant.txt", "a") as file:
with open("/home/riotu/Dropbox/Adel/ChatGPT/ROSGPT/NL_commands_Robotic_Arm_base_commands_with_irrelevant.txt", "a") as file:
    for i in range(nb_commands):
        print(i)
        # First, generate a base command
        try:
            base_command = issue_commands("", system_prompt=generate_command_prompt)
            # rephrased_commands = issue_commands(base_command)
            print((f"{base_command}\n"))
            file.write(f"{base_command}\n")

        except Exception as e:
            print(f"An error occurred: {e}")

        # file.write("Rephrased Commands:\n")
        # for idx, rep_cmd in enumerate(rephrased_commands.split('\n'), 1):
        #     print((f"{rep_cmd}\n"))
        #     file.write(f"{rep_cmd}\n")
        # file.write("\n")
