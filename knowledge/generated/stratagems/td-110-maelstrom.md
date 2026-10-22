---
id: "td-110-maelstrom"
name: "TD-110 Maelstrom"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["broken_file_links"]
wiki_url: "https://helldivers.wiki.gg/wiki/TD-110_Maelstrom"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/td-110-maelstrom.json"
---

# TD-110 Maelstrom

**分类：** 战略配备 (`stratagems`) · **ID：** `td-110-maelstrom`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/TD-110_Maelstrom

## 简介

The TD-110 Maelstrom is a Stratagem that deploys a tracked ground vehicle armed with two triple-barrel rotary guns and two vertically mounted laser-guided missile pods.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | vehicle |
| 特性 ID (`traitIds`) | vehicle, heavy-armor-penetrating, anti-tank |
| 输入指令 (`code`) | left, down, right, down, left, down, up, left, right |
| 冷却时间（秒） (`cooldownS`) | 780 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 741 |
| 呼叫时间（秒） (`callInTimeS`) | 10.5 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time for all stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. P11（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 150 |
| `damage.durable` | 35 |
| `damage.type` | Ballistic |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 52 |
| `projectile.initialVelocityMps` | 980 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 15 |
| `forces.stagger` | 25 |
| `forces.push` | 20 |


### 2. SWP MAELSTROMIII E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 2000 |
| `damage.durable` | 2000 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 3 |
| `area.outerRadiusM` | 5 |
| `area.shockwaveRadiusM` | 10 |
| `forces.demolition` | 40 |
| `forces.stagger` | 50 |
| `forces.push` | 70 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | event |
| `label` | Armored Eagle |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| 消耗 (`cost`) | — |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/td-110-maelstrom.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/TD-110_Maelstrom
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

