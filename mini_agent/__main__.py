"""支持 python3 -m mini_agent。"""

import sys

if sys.version_info < (3, 11):
    print("需要 Python 3.11+。本项目已经提供独立环境，请改用 ./lab。", file=sys.stderr)
    raise SystemExit(2)

from .cli import main

raise SystemExit(main())
