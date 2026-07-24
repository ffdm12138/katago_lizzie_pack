CHCP 65001
@echo 此窗口将会尝试运行引擎并请求落子,最后将会显示字符组成的棋盘,棋盘上有1-2个棋子.如不能显示棋盘则运行过程中有错误或引擎不支持标准的GTP命令
"katago_tensorRT\katago.exe" gtp -model "weights\kata1-b28c512nbt-s7709128960-d4462231357.bin.gz" -config "katago_configs\default_gtp.cfg" < test_commands.txt
pause
