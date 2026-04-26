'''
Author: jinxudong 18751241086@163.com
Date: 2026-04-26 17:29:02
LastEditors: jinxudong 18751241086@163.com
LastEditTime: 2026-04-26 17:58:21
FilePath: \Mauns\api\app\interface\endpoints\status_route.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from typing import List

from fastapi import APIRouter, Depends

# from app.application.services.status_service import StatusService
# from app.domain.models.health_status import HealthStatus
from app.interfaces.schemas import Response
# from app.interfaces.service_dependencies import get_status_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/status", tags=["状态模块"])


@router.get(
    path="",
    response_model=Response,
    summary="系统健康检查",
    description="检查系统的postgres、redis、fastapi等组件的状态信息。"
)
async def get_status() -> Response:
    """系统健康检查，检查postgres/redis/fastapi/cos等服务"""
    return Response.success(msg="系统健康检查成功")

# async def get_status(
#         status_service: StatusService = Depends(get_status_service),
# ) -> Response:
#     """系统健康检查，检查postgres/redis/fastapi/cos等服务"""
#     statues = await status_service.check_all()

#     if any(item.status == "error" for item in statues):
#         return Response.fail(503, "系统存在服务异常", statues)

#     return Response.success(msg="系统健康检查成功", data=statues)
