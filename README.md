# HD2 Markdown Knowledge Base

《绝地潜兵2》（Helldivers 2）非官方 Markdown 知识库，供 [AstrBot knowledge_repo_sync](https://github.com/Sakura1618/astrbot_plugin_knowledge_repo_sync) 增量拉取。

**数据来源**：[Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)，其数据取自 [The Helldivers Wiki](https://helldivers.wiki.gg/)（社区贡献）。本仓库不是 Arrowhead 或 Sony 官方数据库；数据可能滞后游戏版本。遵循上游 CC BY-NC-SA 4.0 条款，见 [LICENSE-NOTICE.md](LICENSE-NOTICE.md)。

## 更新方式

- **GitHub 自动更新**：仓库 Actions → *Update HD2 Markdown Knowledge Base* → *Run workflow* 可随时执行，另外每天 03:15 UTC 定时采集。仅数据有变化才提交 Markdown。
- **本地运行并自动推送**：Windows 双击 `run_windows.bat`；Linux/macOS 执行 `bash run_linux.sh`。需要 Python 3.9+、Git、对本仓库的推送权限；首次运行前请创建空仓库。
- **仅本地生成**：`python scripts/hd2_to_markdown.py --out knowledge --scope gameplay --aliases-csv config/aliases_zh.csv`。
- **包含所有 14 类物品**：本地执行 `run_windows.bat --scope all` 或 `bash run_linux.sh --scope all`。注意：当前 Actions 默认使用 `gameplay`；若手动采用 `all`，下一次 Actions 会重新恢复到 `gameplay`，如需长期全量请同步更改工作流参数。

## 文件结构

- `knowledge/generated/`：各装备实体 Markdown；每个实体一个文件，带来源、属性和不同攻击模式数值。
- `knowledge/_INDEX.md`：生成的索引，**不建议嵌入知识库**（内容重复）。
- `knowledge/notes/`：人工维护的补充文档，不会被采集器覆盖。
- `knowledge/manifest.json`：源数据版本与条数（非 Markdown，插件不会导入）。
- `scripts/hd2_to_markdown.py`：采集和 Markdown 转换。
- `scripts/update_repo.py`：本地采集、Git commit 和 push。
- `.github/workflows/update-knowledge.yml`：GitHub Actions 定时 / 手动更新。

## 与 AstrBot 插件对接

在 `astrbot_plugin_knowledge_repo_sync` 的配置界面填写：

| 字段 | 值 |
|---|---|
| `remote_repo_url` | `https://github.com/shenjiaqi8/hd2-knowledge-base` |
| `remote_branch` | `main` |
| `target_kb_name` | `Helldivers 2` |
| `auto_sync_enabled` | `true` |
| `auto_sync_interval_hours` | `24`（若希望更快响应，可改为 `1`） |
| `ignore_paths` | `README.md`、`LICENSE-NOTICE.md`、`knowledge/_INDEX.md`、`knowledge/notes/README.md` |

插件的命令 `/knowledge_sync` 手动拉取远端最新变更。插件只**读取 GitHub**，不会把 AstrBot 的知识库变化写回 GitHub。Github Actions 或本地采集脚本负责更新远端。

如自动创建知识库失败，请确认 AstrBot 已配置可用的嵌入模型和 `git` 命令。

## 新建仓库并首次上传（只需一次）

1. 打开 https://github.com/new ，Owner 选择 `shenjiaqi8`，Repository name 填 `hd2-knowledge-base`，建议 **Public**，不要在 GitHub 页面初始化 README、.gitignore 或许可证，以保留空仓库。
2. 将本工具包解压到一个普通文件夹（不在其他 Git 仓库里）。安装 Git for Windows 和 Python。
3. 双击 `run_windows.bat`（Linux 则 `bash run_linux.sh`）。会初始化本地 git、获取最新装备数据、生成 Markdown、提交并推送到远端；Git 可能会弹出网页登录授权。**不要将 Personal Access Token 粘贴到聊天中。**
4. 在仓库 GitHub → Actions 中启用工作流。如自动提交提示 403，请到仓库 Settings → Actions → General → Workflow permissions 设置 `Read and write permissions`。
5. 配置 AstrBot 插件并执行 `/knowledge_sync`。

若远程仓库已存在内容，建议先 `git clone` 该仓库，再将脚本和目录复制到克隆目录后运行；切勿直接覆盖不同的 Git 历史。

## 数据范围与注意事项

默认 `gameplay` 范围包含 weapons / stratagems / armors / armor-sets / boosters / passives / weapon-traits / warbonds。完整敌人弱点、任务剧情与实时战争地图不包含在这份装备 API 中，需要后续补充。

自动生成的 Markdown 中可能包含来自 Wiki 的历史或尚未实装数据。不要将所有标记为 upcoming 的数值都当成已上线数值。
