#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: jinxudong 18751241086@163.com
Date: 2026-04-26 17:43:33
LastEditors: jinxudong 18751241086@163.com
LastEditTime: 2026-04-26 17:57:47
FilePath: \Mauns\api\app\interface\endpoints\route.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''


from fastapi import APIRouter

from . import status_route
# , app_config_routes, file_routes, session_routes


def create_api_routes() -> APIRouter:
    """创建API路由，涵盖整个项目的所有路由管理"""
    # 1.创建APIRouter实例
    api_router = APIRouter()

    # 2.将各个模块添加到api_router中
    api_router.include_router(status_route.router)
    # api_router.include_router(app_config_routes.router)
    # api_router.include_router(file_routes.router)
    # api_router.include_router(session_routes.router)

    # 3.返回api路由实例
    return api_router


router = create_api_routes()
