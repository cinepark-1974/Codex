import json
from typing import Any, Dict, List
from urllib import error, request


NOTION_VERSION = "2022-06-28"


class NotionClient:
    def __init__(self, token: str, database_id: str):
        self.token = token
        self.database_id = database_id
        self.base_url = "https://api.notion.com/v1"

    def _request(self, method: str, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        body = json.dumps(payload).encode("utf-8") if payload else None
        req = request.Request(
            url,
            data=body,
            method=method,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Notion-Version": NOTION_VERSION,
                "Content-Type": "application/json",
            },
        )
        try:
            with request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except error.HTTPError as exc:
            message = exc.read().decode("utf-8")
            raise RuntimeError(f"Notion API error ({exc.code}): {message}") from exc

    def fetch_idea_records(self, limit: int = 10) -> List[Dict[str, Any]]:
        payload = {
            "filter": {
                "property": "Status",
                "status": {"equals": "idea"},
            },
            "page_size": min(limit, 10),
        }
        data = self._request("POST", f"/databases/{self.database_id}/query", payload)
        return data.get("results", [])

    def update_record(
        self,
        page_id: str,
        prompt_pack: str,
        top_prompts: str,
        score: float,
        status: str = "generated",
    ) -> Dict[str, Any]:
        payload = {
            "properties": {
                "Prompt Pack": {
                    "rich_text": [
                        {"type": "text", "text": {"content": prompt_pack[:2000]}}
                    ]
                },
                "Top Prompts": {
                    "rich_text": [
                        {"type": "text", "text": {"content": top_prompts[:2000]}}
                    ]
                },
                "Score": {"number": float(score)},
                "Status": {"status": {"name": status}},
            }
        }
        return self._request("PATCH", f"/pages/{page_id}", payload)


def extract_source_text(page: Dict[str, Any]) -> str:
    props = page.get("properties", {})

    def read_title_or_text(property_name: str) -> str:
        value = props.get(property_name)
        if not value:
            return ""
        ptype = value.get("type")
        if ptype == "title":
            items = value.get("title", [])
            return " ".join(item.get("plain_text", "") for item in items).strip()
        if ptype == "rich_text":
            items = value.get("rich_text", [])
            return " ".join(item.get("plain_text", "") for item in items).strip()
        if ptype == "multi_select":
            return " ".join(item.get("name", "") for item in value.get("multi_select", []))
        return ""

    candidates = ["Title", "Name", "Idea", "Keywords", "Keyword"]
    text_parts = [read_title_or_text(name) for name in candidates]
    merged = " ".join(part for part in text_parts if part).strip()
    return merged or "romantic dinner, warm lighting, soft jazz"
