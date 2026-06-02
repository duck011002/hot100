# codex-version Excel 成绩清洗

这是一个单目录版本，不再单独抽象 `skill` 包。页面使用 Streamlit，核心流程是：

1. Python 读取 Excel（支持 `.xlsx/.xlsm/.xls/.xlsb`）。
2. Python 规则识别表头、课程列、成绩列并抽取原始成绩。
3. 可选调用 LLM 分析表头和风险项。
4. 页面展示 records、warnings、errors、review_items，并下载 JSON/CSV。

启动：

```powershell
cd D:\project\hot100\codexskill\course_excel_clean\codex-version
.\run.ps1
```

或：

```bat
run.bat
```

如果依赖缺失：

```powershell
conda activate excel
pip install -r requirements.txt
```

注意：API Key 只在页面密码框输入，不写入文件。成绩数值由 Python 从 Excel 原始单元格读取，LLM 不负责生成或修改成绩。
