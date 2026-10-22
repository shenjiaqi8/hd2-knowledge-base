---
id: "ax-flam-75-hot-dog"
name: "AX/FLAM-75 Hot Dog"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/AX/FLAM-75_Hot_Dog"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/ax-flam-75-hot-dog.json"
---

# AX/FLAM-75 Hot Dog

**分类：** 战略配备 (`stratagems`) · **ID：** `ax-flam-75-hot-dog`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/AX/FLAM-75_Hot_Dog

## 简介

The AX/FLAM-75 Hot Dog is a backpack Stratagem that provides support to the player by automatically targeting enemies and setting them on fire with its mounted flamethrower.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | backpack |
| 特性 ID (`traitIds`) | hellpod, backpack, incendiary |
| 输入指令 (`code`) | down, up, left, up, left, left |
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
| `shipModules\[2\].module` | Enhanced Combustion |
| `shipModules\[2\].effect` | Fire damage from Stratagems increased by 25%. |
| `shipModules\[3\].department` | bridge |
| `shipModules\[3\].module` | Morale Augmentation |
| `shipModules\[3\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `backpack.health` | 100 |
| `backpack.armor` | very_light |
| `backpack.capacity` | — |


## 攻击模式、伤害与穿甲

### 1. AX/FLAM-75 HOT DOG S（spray）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 2 |
| `damage.durable` | 2 |
| `damage.type` | Fire |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 5 |
| `forces.push` | 5 |


### 2. Fire（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 100 |
| `damage.durable` | 100 |
| `damage.type` | Fire |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 0 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


### 3. Fire Panic（status）

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


### 4. FlamerSlowed（status）

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
| `label` | Python Commandos P1 |
| 战争债券 ID (`warbondId`) | python-commandos |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 75 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/ax-flam-75-hot-dog.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/AX/FLAM-75_Hot_Dog
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

