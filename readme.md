## 开发框架

- PyME [pyme](https://www.py-me.com/)

## Reference

- [Gomoku RL](https://github.com/hesic73/gomoku_rl.git)

## 打包

```shell
# 最好先创建虚拟环境
python -m PyInstaller --onefile --console --add-data "model;model" --add-data "static;static" gomoku_with_ai.py
```