from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any

import pandas as pd
import streamlit as st

from cleaner import clean_excel, snapshot_excel
from llm_agent import analyze_with_llm


OUTPUT_DIR = Path("outputs")
RECORD_COLUMNS = [
    "student_no",
    "student_name",
    "course_name",
    "score",
    "score_raw",
    "source_sheet",
    "source_row",
    "confidence",
    "warnings",
]


def records_df(result: dict[str, Any]) -> pd.DataFrame:
    rows = result.get("records", [])
    if not rows:
        return pd.DataFrame(columns=RECORD_COLUMNS)
    df = pd.DataFrame(rows)
    for col in RECORD_COLUMNS:
        if col not in df.columns:
            df[col] = ""
    df["warnings"] = df["warnings"].apply(lambda x: ";".join(x) if isinstance(x, list) else x)
    return df[RECORD_COLUMNS]


def download_json(result: dict[str, Any]) -> bytes:
    return json.dumps(result, ensure_ascii=False, indent=2).encode("utf-8")


def download_csv(result: dict[str, Any]) -> bytes:
    return records_df(result).to_csv(index=False).encode("utf-8-sig")


def render_result(result: dict[str, Any]) -> None:
    if result["status"] == "success":
        st.success("清洗完成")
    elif result["status"] == "need_review":
        st.warning("需要人工确认")
    else:
        st.error("清洗失败")

    report = result.get("cleaning_report", {})
    cols = st.columns(6)
    cols[0].metric("status", result.get("status"))
    cols[1].metric("table_type", result.get("table_type"))
    cols[2].metric("records", len(result.get("records", [])))
    cols[3].metric("valid_rows", report.get("valid_rows", 0))
    cols[4].metric("skipped_rows", report.get("skipped_rows", 0))
    cols[5].metric("review", str(report.get("manual_review_required", False)))

    if result.get("status") == "need_review":
        st.info("提示：请在“警告与审核项”里查看详情。没有成绩列时不会伪装成成功结果。")

    tabs = st.tabs(["成绩明细预览", "警告与审核项", "字段与课程映射", "下载", "LLM 分析"])
    with tabs[0]:
        st.dataframe(records_df(result), use_container_width=True, height=450)
    with tabs[1]:
        st.write("review_items")
        st.json(result.get("review_items", []))
        st.write("warnings")
        st.json(result.get("warnings", []))
        st.write("errors")
        st.json(result.get("errors", []))
    with tabs[2]:
        left, right = st.columns(2)
        left.json(result.get("course_resolution", {}))
        right.json(result.get("field_mapping", {}))
    with tabs[3]:
        left, right = st.columns(2)
        left.download_button("下载 JSON", download_json(result), "cleaning_result.json", "application/json", use_container_width=True)
        right.download_button("下载 CSV", download_csv(result), "cleaning_result.csv", "text/csv", use_container_width=True)
    with tabs[4]:
        st.json(result.get("llm_analysis", {}))


def main() -> None:
    st.set_page_config(page_title="Excel 成绩清洗", layout="wide")
    st.title("Excel 成绩数据清洗")

    with st.sidebar:
        st.header("大模型设置")
        base_url = st.text_input("API Base URL", value="https://www.inroi.shop")
        api_key = st.text_input("API Key", type="password")
        model = st.text_input("模型名称", value="gpt-5.5")
        reasoning_effort = st.selectbox("推理强度", ["xhigh", "high", "medium", "low"], index=0)
        use_llm = st.checkbox("启用 LLM 分析", value=True)

    with st.form("form"):
        cols = st.columns([2, 1, 1])
        selected_course_name = cols[0].text_input("指定课程名称 selected_course_name（必填）")
        selected_course_id = cols[1].text_input("指定课程代码 selected_course_id（可选）")
        import_mode = cols[2].selectbox("导入模式 import_mode", ["single_course", "batch_multi_course"])
        uploaded_file = st.file_uploader("上传成绩 Excel 文件", type=["xlsx", "xlsm", "xls", "xlsb"])
        submitted = st.form_submit_button("开始清洗", use_container_width=True)

    if submitted:
        if not selected_course_name.strip():
            st.warning("请先输入课程名。")
            return
        if uploaded_file is None:
            st.warning("请先上传 Excel 文件。")
            return
        if use_llm and not api_key.strip():
            st.warning("启用 LLM 时必须输入 API Key。")
            return

        try:
            with tempfile.TemporaryDirectory(prefix="codex_excel_clean_") as temp_dir:
                upload_path = Path(temp_dir) / uploaded_file.name
                upload_path.write_bytes(uploaded_file.getbuffer())
                result = clean_excel(
                    file_path=upload_path,
                    selected_course_name=selected_course_name.strip(),
                    selected_course_id=selected_course_id.strip() or None,
                    import_mode=import_mode,
                    output_dir=OUTPUT_DIR,
                )
                if use_llm:
                    snapshot = snapshot_excel(upload_path)
                    llm_analysis = analyze_with_llm(
                        base_url=base_url.strip(),
                        api_key=api_key.strip(),
                        model=model.strip(),
                        reasoning_effort=reasoning_effort,
                        snapshot=snapshot,
                        python_result=result,
                    )
                    result["llm_analysis"] = llm_analysis
                    for item in llm_analysis.get("review_items", []) or []:
                        result["review_items"].append(item)
                    for warning in llm_analysis.get("warnings", []) or []:
                        result["warnings"].append(warning)
                    if result["review_items"] and result["status"] == "success":
                        result["status"] = "need_review"
                        result["cleaning_report"]["manual_review_required"] = True
                st.session_state["result"] = result
        except Exception as exc:
            st.error("清洗过程异常")
            st.exception(exc)

    if "result" in st.session_state:
        render_result(st.session_state["result"])


if __name__ == "__main__":
    main()
