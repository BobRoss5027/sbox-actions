#!/bin/bash

rm my_deployment_package.zip
zip -r ../my_deployment_package.zip ./package
zip my_deployment_package.zip lambda_function.py

