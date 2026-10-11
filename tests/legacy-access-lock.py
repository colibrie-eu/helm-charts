"""Check the narrow changed Helm blocks, without Helm or network access."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent.parent
for service in ("frontend", "onboarding"):
    path = f"charts/{service}/templates/deployment.yaml"
    current = (ROOT / path).read_text()
    original = subprocess.check_output(
        ["git", "show", "1017a2aa60e30fd5afd8f1ddf4807b1ed39aa56f:" + path],
        cwd=ROOT, text=True,
    )
    assert "value: {{ .Values.legacyAccessLock.enabled | quote }}" in current
    assert (ROOT / f"charts/{service}/values.yaml").read_text().endswith(
        "legacyAccessLock:\n  enabled: false\n"
    )
    original_probes = original[
        original.index("          {{- with .Values.livenessProbe }}"):
        original.index("          {{- with .Values.resources }}")
    ]
    if service == "frontend":
        blocks = current[
            current.index("          {{- if .Values.legacyAccessLock.enabled }}"):
            current.index("          {{- with .Values.resources }}")
        ].split("          {{- else }}\n")
        off = blocks[1].removesuffix("          {{- end }}\n")
        assert off == original_probes
        on = blocks[0].split("\n", 1)[1]
        assert on == (
            "          livenessProbe:\n"
            "            tcpSocket:\n"
            "              port: http\n"
            "          readinessProbe:\n"
            "            tcpSocket:\n"
            "              port: http\n"
        )
    else:
        probes = current[
            current.index("          {{- with .Values.livenessProbe }}"):
            current.index("          {{- with .Values.resources }}")
        ]
        assert probes == original_probes
    print(service + ": flag and probe blocks PASS (not a full Helm render)")
