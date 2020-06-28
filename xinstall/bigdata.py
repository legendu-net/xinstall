"""Install big data related tools.
"""
import logging
from pathlib import Path
from .utils import (
    BASE_DIR,
    run_cmd,
    namespace,
    add_subparser,
    option_user,
)


def spark(**kwargs):
    """Install Spark.
    :param yes:
    :param install:
    :param config:
    :param uninstall:
    :param version:
    """
    args = namespace(kwargs)
    dir_ = Path(args.location)
    if args.install:
        dir_.mkdir(exist_ok=True)
        spark_hdp = f"spark-{args.version}-bin-hadoop2.7"
        url = f"{args.mirror}/spark-{args.version}/{spark_hdp}.tgz"
        cmd = f"""curl {url} -o /tmp/{spark_hdp}.tgz \
                && tar -zxvf /tmp/{spark_hdp}.tgz -C {dir_} \
                && ln -svf {dir_}/{spark_hdp} {dir_}/spark \
                && rm /tmp/{spark_hdp}.tgz
            """
        run_cmd(cmd)
    if args.config:
        metastore_db = dir_ / "spark/metastore_db"
        metastore_db.mkdir(parent=True, exist_ok=True)
        shutil.copy2(BASE_DIR / "spark/spark-defaults.conf", dir_ / "spark/conf/")
        logging.info(f"Spark is configured to use {metastore_db} as the metastore location.")
    if args.uninstall:
        cmd = f"rm -rf {dir_}/spark*"
        run_cmd(cmd)


def _spark_args(subparser):
    subparser.add_argument(
        "-m",
        "--mirror",
        dest="mirror",
        default="https://archive.apache.org/dist/spark",
        help="The mirror of Spark (default https://archive.apache.org/dist/spark) to use."
    )
    subparser.add_argument(
        "-v",
        "--version",
        dest="version",
        default="3.0.0",
        help="The version of Spark to install."
    )
    subparser.add_argument(
        "--loc",
        "--location",
        dest="location",
        default="/opt",
        help="The location to install Spark to."
    )


def _add_subparser_spark(subparsers):
    add_subparser(subparsers, "Spark", func=spark, add_argument=_spark_args)


def pyspark(**kwargs):
    """Install PySpark.
    :param yes:
    :param install:
    :param config:
    :param uninstall:
    :param version:
    """
    args = namespace(kwargs)
    if args.install:
        cmd = f"{args.pip} install {args.user_s} pyspark findspark"
        run_cmd(cmd)
    if args.config:
        pass
    if args.uninstall:
        cmd = f"{args.pip} uninstall pyspark findspark"
        run_cmd(cmd)


def _add_subparser_pyspark(subparsers):
    add_subparser(subparsers, "PySpark", func=pyspark, add_argument=option_user)


def optimuspyspark(**kwargs):
    """Install Optimus (a PySpark package for data profiling).
    :param yes:
    :param install:
    :param config:
    :param uninstall:
    :param version:
    """
    args = namespace(kwargs)
    if args.install:
        cmd = f"{args.pip} install {args.user_s} optimuspyspark"
        run_cmd(cmd)
    if args.config:
        pass
    if args.uninstall:
        cmd = f"{args.pip} uninstall optimuspyspark"
        run_cmd(cmd)


def _add_subparser_optimuspyspark(subparsers):
    add_subparser(subparsers, "Optimus", func=optimuspyspark, add_argument=option_user)


def dask(**kwargs):
    """Install the Python module dask.
    :param yes:
    :param install:
    :param config:
    :param uninstall:
    """
    args = namespace(kwargs)
    if args.install:
        cmd = f"{args.pip} install {args.user_s} dask[complete]"
        run_cmd(cmd)
    if args.config:
        pass
    if args.uninstall:
        cmd = f"{args.pip} uninstall dask"
        run_cmd(cmd)


def _add_subparser_dask(subparsers):
    add_subparser(subparsers, "dask", func=dask, add_argument=option_user)
