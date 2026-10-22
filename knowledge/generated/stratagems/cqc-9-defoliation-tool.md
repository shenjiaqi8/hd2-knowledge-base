---
id: "cqc-9-defoliation-tool"
name: "CQC-9 Defoliation Tool"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/CQC-9_Defoliation_Tool"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/cqc-9-defoliation-tool.json"
---

# CQC-9 Defoliation Tool

**分类：** 战略配备 (`stratagems`) · **ID：** `cqc-9-defoliation-tool`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/CQC-9_Defoliation_Tool

## 简介

The CQC-9 Defoliation Tool is a Melee Support Weapon, which is capable of dealing prolonged damage on target.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, anti-tank, melee |
| 输入指令 (`code`) | down, left, right, right, down |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Streamlined Request Process |
| `shipModules\[1\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Morale Augmentation |
| `shipModules\[2\].effect` | Reduces cooldown time for all stratagems by 5%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Streamlined Launch Process |
| `shipModules\[3\].effect` | All Support Weapon stratagems launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. CQC-9 DEFOLIATION TOOL_dm（other）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 450 |
| `damage.durable` | 225 |
| `damage.type` | Melee |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 10 |
| `forces.push` | 30 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Python Commandos P2 |
| 战争债券 ID (`warbondId`) | python-commandos |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 85 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/cqc-9-defoliation-tool.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/CQC-9_Defoliation_Tool
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

