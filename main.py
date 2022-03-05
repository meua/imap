# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Copyright 2021 daohu527 <daohu527@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import argparse
import matplotlib.pyplot as plt

import editor
import global_var
from map import Map

import lib.open_drive_utils as open_drive_utils

def draw(hdmap):
    lane_ids = []
    junction_ids = []
    hdmap.draw_lanes(ax, lane_ids)
    hdmap.draw_junctions(ax, junction_ids)
    hdmap.draw_crosswalks(ax)
    hdmap.draw_stop_signs(ax)
    hdmap.draw_yields(ax)

def show_map():
    hdmap=Map()
    hdmap.load(args.map)
    draw(hdmap)
    # max windows
    # manager=plt.get_current_fig_manager()
    # manager.window.showMaximized()
    # tight layout
    # todo(zero): why tight layout not work?
    plt.tight_layout()
    plt.axis('equal')
    plt.show()

def add_editor():
    fig.canvas.mpl_connect('button_press_event', editor.on_click)
    fig.canvas.mpl_connect('button_press_event', editor.on_press)
    fig.canvas.mpl_connect('button_release_event', editor.on_release)
    fig.canvas.mpl_connect('pick_event', editor.on_pick)
    fig.canvas.mpl_connect('motion_notify_event', editor.on_motion)


def convert_map_format():
    pb_map = open_drive_utils.get_map_from_xml_file(args.input)
    open_drive_utils.save_map_to_xml_file(pb_map, args.output)


def show_open_drive_map():
    pb_map = open_drive_utils.get_map_from_xml_file(args.map)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Mapshow is a tool to display hdmap info on a map.",
        prog="mapshow.py")

    parser.add_argument(
        "-m", "--map", action="store", type=str, required=False,
        help="Specify the map file in txt or binary format")

    parser.add_argument(
        "-f", "--format", action="store", type=str, required=False,
        nargs='?', const="0", help="Convert format")
    parser.add_argument(
        "-i", "--input", action="store", type=str, required=False,
        help="map input path")
    parser.add_argument(
        "-o", "--output", action="store", type=str, required=False,
        help="map output path")


    args = parser.parse_args()

    # 1. Init global var
    global_var._init()

    # 2. show map
    fig, ax = plt.subplots()

    if args.map is not None:
        # TODO(zero): fix two windows
        suffix = args.map.split(".")[1]
        if suffix == "bin" or suffix == "txt":
            add_editor()
            show_map()
        elif suffix == "xodr":
            show_open_drive_map()
        else:
            pass

    # 3. convert opendrive map to apllo
    if args.format is not None:
        convert_map_format()
