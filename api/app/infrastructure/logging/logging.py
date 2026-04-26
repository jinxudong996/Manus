#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: jinxudong 18751241086@163.com
Date: 2026-04-26 17:09:32
LastEditors: jinxudong 18751241086@163.com
LastEditTime: 2026-04-26 17:10:05
FilePath: /Mauns/api/app/infrastructure/logging/logging.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''


import logging
import sys

from core.config import get_settings


def setup_logging():
    """配置Manus项目的日志系统，涵盖日志等级、输出格式、输出渠道等"""
    # 1.获取项目配置
    settings = get_settings()

    # 2.获取根日志处理器
    root_logger = logging.getLogger()

    # 3.清除已有的handlers，避免uvicorn的dictConfig重配置后产生冲突或重复
    root_logger.handlers.clear()

    # 4.设置根日志处理器等级
    log_level = getattr(logging, settings.log_level)
    root_logger.setLevel(log_level)

    # 5.日志输出格式定义
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 6.创建控制台日志输出处理器(使用stderr，stderr在Python中始终无缓冲，Docker中更可靠)
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log_level)

    # 7.将控制台日志处理器添加到根日志处理器中
    root_logger.addHandler(console_handler)

    root_logger.info("日志系统初始化完成")
