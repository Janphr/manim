#!/usr/bin/env python

import sys
import getopt
import imp
import itertools as it
import inspect
import traceback
import imp

from helpers import *
from scene import Scene
from camera import Camera

HELP_MESSAGE = """
   Usage: 
   python extract_scene.py <module> [<scene name>]

   -p preview in low quality
   -s show and save picture of last frame
   -w write result to file [this is default if nothing else is stated]
   -l use low quality
   -m use medium quality
   -a run and save every scene in the script, or all args for the given scene
   -q don't print progress
"""
SCENE_NOT_FOUND_MESSAGE = """
   That scene is not in the script
"""
CHOOSE_NUMBER_MESSAGE = """
Choose number corresponding to desired scene/arguments.
(Use comma separated list for multiple entries)

Choice(s): """
INVALID_NUMBER_MESSAGE = "Fine then, if you don't want to give a valid number I'll just quit"

NO_SCENE_MESSAGE = """
   There are no scenes inside that module
"""


def get_configuration(sys_argv):
   try:
      opts, args = getopt.getopt(sys_argv[1:], 'hlmpwsqa')
   except getopt.GetoptError as err:
      print str(err)
      sys.exit(2)
   config = {
      "file"           : None,
      "scene_name"     : "",
      "camera_config"  : PRODUCTION_QUALITY_CAMERA_CONFIG,
      "frame_duration" : PRODUCTION_QUALITY_FRAME_DURATION,
      "preview"        : False,
      "write"          : False,
      "save_image"     : False,
      "quiet"          : False,
      "write_all"      : False,
   }
   for opt, arg in opts:
      if opt == '-h':
         print HELP_MESSAGE
         return
      if opt in ['-l', '-p']:
         config["camera_config"] = LOW_QUALITY_CAMERA_CONFIG
      if opt in ['-l', '-p', '-m']:
         config["frame_duration"] = DEFAULT_FRAME_DURATION
      if opt == '-p':
         config["preview"] = True
      if opt == '-m':
         config["camera_config"] = MEDIUM_QUALITY_CAMERA_CONFIG
      if opt == '-w':
         config["write"] = True
      if opt == '-s':
         config["save_image"] = True
      if opt in ['-q', '-a']:
         config["quiet"] = True
      if opt == '-a':
         config["write_all"] = True
   #By default, write to file
   actions = ["write", "preview", "save_image"]
   if not any([config[key] for key in actions]):
      config["write"] = True   
   config["skip_animations"] = config["save_image"] and not config["write"]

   if len(args) == 0:
      print HELP_MESSAGE
      sys.exit()
   config["file"] = args[0]
   if len(args) > 1:
      config["scene_name"] = args[1]
   return config

def handle_scene(scene, **config):
   name = str(scene)
   if config["quiet"]:
      curr_stdout = sys.stdout
      sys.stdout = open(os.devnull, "w")
      
   if config["preview"]:
      scene.preview()
   if config["save_image"]:
      if not config["write_all"]:
         scene.show_frame()
      path = os.path.join(MOVIE_DIR, config["movie_prefix"])
      scene.save_image(path, name)
   if config["write"]:
      scene.write_to_movie(os.path.join(config["movie_prefix"], name))

   if config["quiet"]:
      sys.stdout.close()
      sys.stdout = curr_stdout

def is_scene(obj):
   if not inspect.isclass(obj):
      return False
   if not issubclass(obj, Scene):
      return False
   if obj == Scene:
      return False
   return True

def prompt_user_for_choice(name_to_obj):
   num_to_name = {}
   names = sorted(name_to_obj.keys())
   for count, name in zip(it.count(1), names):
      print "%d: %s"%(count, name)
      num_to_name[count] = name
   try:
      user_input = raw_input(CHOOSE_NUMBER_MESSAGE)
      return [
         name_to_obj[num_to_name[int(num_str)]]
         for num_str in user_input.split(",")
      ]
   except:
      print INVALID_NUMBER_MESSAGE
      sys.exit()

def get_scene_classes(scene_names_to_classes, config):
   if len(scene_names_to_classes) == 0:
      print NO_SCENE_MESSAGE
      return []
   if len(scene_names_to_classes) == 1:
      return scene_names_to_classes.values()
   if config["scene_name"] in scene_names_to_classes:
      return [scene_names_to_classes[config["scene_name"]] ]
   if config["scene_name"] != "":
      print SCENE_NOT_FOUND_MESSAGE
      return []
   if config["write_all"]:
      return scene_names_to_classes.values()
   return prompt_user_for_choice(scene_names_to_classes)

def get_module(file_name):
   module_name = file_name.replace(".py", "")
   last_module = imp.load_module(".", *imp.find_module("."))
   for part in module_name.split(os.sep):
      load_args = imp.find_module(part, last_module.__path__)
      last_module = imp.load_module(part, *load_args)
   return last_module

def main():
   config = get_configuration(sys.argv)
   module = get_module(config["file"])
   scene_names_to_classes = dict(
      inspect.getmembers(module, is_scene)
   )
   config["movie_prefix"] = config["file"].replace(".py", "")
   scene_kwargs = {
      "camera_config" : config["camera_config"],
      "frame_duration" : config["frame_duration"],
      "skip_animations" : config["skip_animations"],
   }
   for SceneClass in get_scene_classes(scene_names_to_classes, config):
      try:
         handle_scene(SceneClass(**scene_kwargs), **config)
         play_finish_sound()
      except:
         print "\n\n"
         traceback.print_exc()
         print "\n\n"
         play_error_sound()


if __name__ == "__main__":
   main()




