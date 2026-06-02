from __future__ import annotations

import json
from typing import Any

import requests


SYSTEM_PROMPT = """
你是 Excel 成绩数据清洗智能体。你只负责根据 Excel 摘要判断表头、字段和风险。
成绩数值必须由 Python 从 Excel 原始单元格读取，不能由模型生成或修改。
返回严格 JSON：{"analysis":"...","table_type":"...","field_mapping":{},"warnings":[],"review_items":[]}
"""


def endpoint(base_url: str) -> str:
    clean = base_url.rstrip("/")
    if clean.endswith("/v1"):
        return f"{clean}/responses"
    return f"{clean}/v1/responses"


def response_text(payload: dict[str, Any]) -> str:
    if isinstance(payload.get("output_text"), str):
        return payload["output_text"]
    texts: list[str] = []
    for item in payload.get("output", []) or []:
        for content in item.get("content", []) or []:
            if isinstance(content.get("text"), str):
                texts.append(content["text"])
    return "\n".join(texts) if texts else json.dumps(payload, ensure_ascii=False)


def parse_json(text: str) -> dict[str, Any]:
    clean = text.strip()
    start = clean.find("{")
    end = clean.rfind("}")
    if start >= 0 and end >= start:
        clean = clean[start : end + 1]
    return json.loads(clean)


def analyze_with_llm(
    *,
    base_url: str,
    api_key: str,
    model: str,
    reasoning_effort: str,
    snapshot: dict[str, Any],
    python_result: dict[str, Any],
) -> dict[str, Any]:
    request_payload = {
        "model": model,
        "input": [
            {"role": "system", "content": [{"type": "input_text", "text": SYSTEM_PROMPT}]},
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": json.dumps(
                            {
                                "excel_snapshot": snapshot,
                                "python_result_summary": {
                                    "status": python_result.get("status"),
                                    "table_type": python_result.get("table_type"),
                                    "records": len(python_result.get("records", [])),
                                    "field_mapping": python_result.get("field_mapping", {}),
                                    "review_items": python_result.get("review_items", []),
                                    "errors": python_result.get("errors", []),
                                },
                            },
                            ensure_ascii=False,
                        ),
                    }
                ],
            },
        ],
        "reasoning": {"effort": reasoning_effort},
        "store": False,
    }
    response = requests.post(
        endpoint(base_url),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json=request_payload,
        timeout=120,
    )
    response.raise_for_status()
    return parse_json(response_text(response.json()))
