#!/usr/bin/env python3
"""Inject data/features.json into index.template.html -> index.html (self-contained).
Edit features.json, re-run `python3 build.py`, then re-publish the artifact."""
import json, pathlib, sys

here = pathlib.Path(__file__).parent
data_path = here / "data" / "features.json"
tpl_path = here / "index.template.html"
out_path = here / "index.html"

data = json.loads(data_path.read_text(encoding="utf-8"))   # validate JSON
tpl = tpl_path.read_text(encoding="utf-8")
if "__DITTO_DATA__" not in tpl:
    sys.exit("placeholder __DITTO_DATA__ not found in template")
# compact JSON, escape any </script> defensively
payload = json.dumps(data, ensure_ascii=False).replace("</script>", "<\\/script>")
out = tpl.replace("__DITTO_DATA__", payload)
out_path.write_text(out, encoding="utf-8")
print(f"built {out_path.name}: {len(data['features'])} features, {len(out)} bytes")
