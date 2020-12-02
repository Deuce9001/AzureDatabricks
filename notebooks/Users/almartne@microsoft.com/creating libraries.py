# Databricks notebook source
# MAGIC %python
# MAGIC import pkg_resources
# MAGIC pkg_resources.get_distribution('scipy').version

# COMMAND ----------

dbutils.library.list()

# COMMAND ----------

dbutils.library.installPyPI('scipy','1.2.0')
dbutils.library.restartPython()
dbutils.library.list()

# COMMAND ----------

dbutils.library.restartPython()