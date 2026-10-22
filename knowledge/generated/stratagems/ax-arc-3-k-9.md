---
id: "ax-arc-3-k-9"
name: "AX/ARC-3 K-9"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated", "broken_file_links"]
wiki_url: "https://helldivers.wiki.gg/wiki/AX/ARC-3_K-9"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/ax-arc-3-k-9.json"
---

# AX/ARC-3 K-9

**分类：** 战略配备 (`stratagems`) · **ID：** `ax-arc-3-k-9`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/AX/ARC-3_K-9

## 简介

The AX/ARC-3 K-9 is a backpack Stratagem that provides support to the player by automatically targeting enemies with its mounted arc thrower.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | backpack |
| 特性 ID (`traitIds`) | hellpod, backpack, anti-tank, arc |
| 输入指令 (`code`) | down, up, left, up, right, left |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| `cooldownVariants\[2\].label` | With Hand Carts |
| `cooldownVariants\[2\].seconds` | 432 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 410.4 |
| 呼叫时间（秒） (`callInTimeS`) | 9.75 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Hand Carts |
| `shipModules\[1\].effect` | Decreases cooldown for all Backpack stratagems by 10%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Morale Augmentation |
| `shipModules\[2\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `backpack.health` | 100 |
| `backpack.armor` | very_light |
| `backpack.capacity` | — |


## 攻击模式、伤害与穿甲

### 1. AX/ARC-3 K-9 A（arc）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 250 |
| `damage.durable` | 45 |
| `damage.type` | Arc |
| `penetration.direct` | anti_tank_iii |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_iii |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 25 |


### 2. Stun Small（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | — |
| `damage.durable` | — |
| `damage.type` | — |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | — |
| `forces.stagger` | — |
| `forces.push` | — |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Force of Law P3 |
| 战争债券 ID (`warbondId`) | force-of-law |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 110 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/ax-arc-3-k-9.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/AX/ARC-3_K-9
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

