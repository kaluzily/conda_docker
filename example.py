import geopandas as gpd
import os
import glob
import re
import sys

# from gridded_data_visualize import load_velocity_data
from datetime import datetime
import geopandas as gpd
import numpy as np
from shapely.geometry import LineString
import rasterstats
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from collections.abc import Iterable
from sklearn import linear_model
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.colors import LogNorm
import matplotlib.colors as mcolors
from matplotlib.ticker import LogFormatter, FixedLocator
import rasterio

print('working')