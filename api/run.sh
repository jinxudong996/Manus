#!/bin/bash
###
 # @Author: jinxudong 18751241086@163.com
 # @Date: 2026-04-26 15:37:59
 # @LastEditors: jinxudong 18751241086@163.com
 # @LastEditTime: 2026-04-26 18:06:33
 # @FilePath: \Mauns\api\run.sh
 # @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
### 

# 启用uvicorn运行服务（使用exec让uvicorn成为主进程）
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --timeout-graceful-shutdown 5