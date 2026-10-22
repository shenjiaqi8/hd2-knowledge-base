---
id: "b-100-portable-hellbomb"
name: "B-100 Portable Hellbomb"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/B-100_Portable_Hellbomb"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/b-100-portable-hellbomb.json"
---

# B-100 Portable Hellbomb

**分类：** 战略配备 (`stratagems`) · **ID：** `b-100-portable-hellbomb`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/B-100_Portable_Hellbomb

## 简介

The Portable Hellbomb is a backpack Stratagem that grants the player the utility of an on-demand Hellbomb free from the restriction of only being usable near mission objectives.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | backpack |
| 特性 ID (`traitIds`) | hellpod, explosive, backpack, anti-tank |
| 输入指令 (`code`) | down, right, up, up, up |
| 冷却时间（秒） (`cooldownS`) | 300 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 285 |
| `cooldownVariants\[2\].label` | With Hand Carts |
| `cooldownVariants\[2\].seconds` | 270 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 256.5 |
| 呼叫时间（秒） (`callInTimeS`) | 9.75 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Hand Carts |
| `shipModules\[1\].effect` | Decreases cooldown for all Backpack stratagems by 10%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Morale Augmentation |
| `shipModules\[2\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `backpack.health` | — |
| `backpack.armor` | — |
| `backpack.capacity` | — |


## 攻击模式、伤害与穿甲

### 1. Hellbomb（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 10000 |
| `damage.durable` | 10000 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 17 |
| `area.outerRadiusM` | 25 |
| `area.shockwaveRadiusM` | 45 |
| `forces.demolition` | 60 |
| `forces.stagger` | 50 |
| `forces.push` | 100 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Servants of Freedom P3 |
| 战争债券 ID (`warbondId`) | servants-of-freedom |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 110 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/b-100-portable-hellbomb.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/B-100_Portable_Hellbomb
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

