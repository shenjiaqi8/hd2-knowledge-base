# HD2 每类一个 Markdown 补丁

适用于 https://github.com/shenjiaqi8/hd2-knowledge-base 当前的脚本结构。

改动：`knowledge/generated/weapons/<id>.md` 等 557 个文件合并为 `knowledge/generated/weapons.md` 等 8 个大类文件；保留实体条目的完整原文、攻击模式和原始来源。文件中有名称及别名索引，每个实体以二级标题标记。**不会凭空生成敌人信息**；当前装备数据源不包含敌人类别。

## Windows 安装

1. 下载并解压本补丁。
2. 将 `consolidate_categories.py` 复制到仓库 `scripts/` 下。
3. 将 `install_patch.py` 复制到仓库根目录，即与 `run_windows.bat` 同一层。
4. 在仓库目录运行：

```powershell
python install_patch.py
```

5. 提交并推送更新（会同时删除旧的单实体 `.md`）：

```powershell
git add -A
git commit -m "Group HD2 data by category"
git push origin main
```

6. 在 AstrBot 执行 `/knowledge_sync`，插件将删除旧路径文档并同步新的分类文件。

以后直接使用原本的 `run_windows.bat`；GitHub Actions 也会通过已修改的 `hd2_to_markdown.py` 生成分类文件，无需额外改工作流。

## 注意

- 第一次同步会删除 557 个旧知识库文档、创建 8 个新分类文档；有可能较慢。
- 8 个大文件仍会被 AstrBot 根据 `chunk_size` 再切分为知识库片段。若检索命中率不理想，建议进一步按武器子类型组织或使用关键词全文检索，而不是继续加大单文件。
- 采集器执行时会短暂生成逐实体文件，随即合并；提交到 GitHub 的最终产物始终是一类一个文件。
- 如果已有手工编辑的 `knowledge/generated/` 文件，先备份；补丁视该目录为自动生成数据，会覆盖旧文件。自定义内容放在 `knowledge/notes/`。
