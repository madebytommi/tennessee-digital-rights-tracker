"""Minimal RSS 2.0 parser for discovery source feeds."""

from __future__ import annotations

from xml.etree import ElementTree as ET

from discovery.textutil import parse_date, strip_html

CONTENT_NS = "{http://purl.org/rss/1.0/modules/content/}"
DC_NS = "{http://purl.org/dc/elements/1.1/}"


def _child_text(item: ET.Element, names: tuple[str, ...]) -> str:
    for name in names:
        child = item.find(name)
        if child is not None:
            if child.text and child.text.strip():
                return child.text.strip()
            if list(child):
                return "".join(child.itertext()).strip()
    return ""


def parse_rss_items(xml_text: str) -> list[dict[str, str | None]]:
    root = ET.fromstring(xml_text)
    items: list[dict[str, str | None]] = []
    for item in root.findall(".//item"):
        title = strip_html(_child_text(item, ("title",)))
        link = strip_html(_child_text(item, ("link",)))
        guid = strip_html(_child_text(item, ("guid",)))
        description = _child_text(item, ("description", f"{CONTENT_NS}encoded"))
        creator = strip_html(_child_text(item, (f"{DC_NS}creator", "author")))
        pub = _child_text(item, ("pubDate", "published", "date"))
        items.append(
            {
                "title": title,
                "url": link or guid,
                "summary": strip_html(description),
                "published_at": parse_date(pub),
                "author": creator or None,
            }
        )
    return items
