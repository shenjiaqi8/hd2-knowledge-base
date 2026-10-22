---
id: "ax-tx-13-dog-breath"
name: "AX/TX-13 Dog Breath"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated", "broken_file_links"]
wiki_url: "https://helldivers.wiki.gg/wiki/AX/TX-13_Dog_Breath"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/ax-tx-13-dog-breath.json"
---

# AX/TX-13 Dog Breath

**分类：** 战略配备 (`stratagems`) · **ID：** `ax-tx-13-dog-breath`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/AX/TX-13_Dog_Breath

## 简介

The AX/TX-13 Dog Breath is a backpack Stratagem that provides defensive support to the player. It slows and blinds nearby enemies by spraying them with caustic gas, helping the owner avoid being overwhelmed by swarms.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | backpack |
| 特性 ID (`traitIds`) | hellpod, backpack, caustic |
| 输入指令 (`code`) | down, up, left, up, right, up |
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

### 1. AX/TX-13 DOG BREATH S（spray）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1 |
| `damage.durable` | 1 |
| `damage.type` | Gas |
| `penetration.direct` | anti_tank_i |
| `penetration.slightAngle` | anti_tank_i |
| `penetration.largeAngle` | anti_tank_i |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 5 |
| `forces.stagger` | 10 |
| `forces.push` | 5 |


### 2. Gas Confusion Var2（status）

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


### 3. Gas Var2（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 25 |
| `damage.durable` | 25 |
| `damage.type` | Gas |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 0 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Chemical Agents P3 |
| 战争债券 ID (`warbondId`) | chemical-agents |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 110 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/ax-tx-13-dog-breath.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/AX/TX-13_Dog_Breath
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

