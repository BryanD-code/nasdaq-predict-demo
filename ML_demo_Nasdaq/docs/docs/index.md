# Nasdaq-predict documentation!

## Description

Entrenamiento de modelo para predecir el precio del nasdaq como practica para introducirme en las diferentes tegnologias de da

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `az storage blob upload-batch -d` to recursively sync files in `data/` up to `nasdaq-container/data/`.
* `make sync_data_down` will use `az storage blob upload-batch -d` to recursively sync files from `nasdaq-container/data/` to `data/`.


