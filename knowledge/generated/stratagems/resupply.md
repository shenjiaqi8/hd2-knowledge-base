---
id: "resupply"
name: "Resupply"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/Resupply"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/resupply.json"
---

# Resupply

**分类：** 战略配备 (`stratagems`) · **ID：** `resupply`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Resupply

## 简介

The Resupply Stratagem allows Helldivers to call down a Hellpod with 4 Supply Boxes.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | mission |
| `availability` | mission |
| 类型 (`kind`) | mission |
| 特性 ID (`traitIds`) | — |
| 输入指令 (`code`) | down, down, up, right |
| 冷却时间（秒） (`cooldownS`) | 180 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 171 |
| 呼叫时间（秒） (`callInTimeS`) | 8 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Superior Packing Methodology |
| `shipModules\[1\].effect` | Resupply stratagem boxes refill Support Weapons with the maximum number of carriable magazines. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Morale Augmentation |
| `shipModules\[2\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Synthetic Supplementation |
| `shipModules\[3\].effect` | Reduces cooldown time for Sentry, Emplacement, and Resupply stratagems by 10%. |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | other |
| `label` |  |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| 消耗 (`cost`) | — |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/resupply.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Resupply
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

