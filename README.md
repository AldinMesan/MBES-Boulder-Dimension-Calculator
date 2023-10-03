# Project Documentation: MBES Boulder Dimension Calculation

## Table of Contents

1. [Introduction](#1-introduction)
2. [Folder Structure](#2-folder-structure)
3. [Dependencies](#3-dependencies)
4. [Methodology](#4-methodology)
5. [Project Workflow](#5-project-workflow)
6. [Usage](#6-usage)
7. [Customization](#7-customization)
8. [Contributors](#8-contributors)

## 1. Introduction

### Purpose of the Project

The purpose of the project is to automate the calculation of three key dimensions (length, width, and height) for boulders detected in Multibeam Echo Sounder (MBES) data. This project streamlines the process of boulder analysis and measurements, saving time and ensuring accuracy in marine surveys.

### Project Overview

This project focuses on the automatic measurement of boulder dimensions in MBES data, enhancing the efficiency of quality control processes and improving the accuracy of boulder analysis.

## 2. Folder Structure

### Description of Folders and Files

- **Input:** Contains the input vector polygons representing boulder shapes in Shapefile format (`*.shp`, `*.shx`, `*.dbf`, `*.prj`).
- **Output:** The results of boulder measurements, including centroids and dimensions, are stored in this folder as a shapefile (`output_boulder_measurements.shp`).
- **Helpers:** Contains utility scripts for boulder dimension measurement and bathymetry data conversion.
- **run.py:** The main script responsible for coordinating the boulder dimension calculation workflow.

## 3. Dependencies

### Required Software and Libraries

- Python 3.x
- GDAL library for geospatial data processing
- Shapely library for geometry operations

## 4. Methodology

### Steps Taken to Create the Script

1. **Input Data Preparation:**
   - Acquired input vector polygons representing boulder shapes (Shapefile format).
   - Optional: Obtained bathymetry data in GeoTIFF format (not mandatory for boulder dimension calculations but could help with more accurate readings).

2. **Script Development:**
   - Created the `run.py` script as the main entry point for the workflow.
   - Developed utility functions in the "Helpers" folder for boulder dimension measurement (bathymetry data conversion (currently not available, therefore it's not included)).

3. **Boulder Dimension Calculation:**
   - Loaded the input vector polygons representing boulders.
   - Calculated the centroids and dimensions (length, width, and height) of the boulders.
   - Saved the results, including attributes, as a shapefile in the "Output" folder.

4. **User Customization:**
   - Provided customization options in `run.py` for users to adjust input and output paths and other parameters to fit specific project requirements.

## 5. Project Workflow

### Explanation of How the Project Works

The project workflow involves the following steps:
1. Prepare the input data by placing the boulder detection polygons in the "Input" folder.
2. Open the `run.py` script and configure input and output paths, and block name.
3. Run the `run.py` script to initiate the boulder dimension calculation.

## 6. Usage

### How to Run the Project

1. Prepare the input data by placing the boulder detection polygons in the "Input" folder.
2. Open the `run.py` script and configure input and output paths, and block name.
3. Run the `run.py` script to initiate the boulder dimension calculation.

## 7. Customization

### How to Customize the Project for Different Inputs or Requirements

Users can customize the project by:
- Replacing the input vector polygons in the "Input" folder with their own boulder detection data.
- Adjusting script parameters in `run.py` for specific project requirements.

## 8. Contributors

### List of Contributors and Roles

- [Aldin Mešan]: Project lead and developer.
