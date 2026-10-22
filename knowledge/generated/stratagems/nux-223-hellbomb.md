---
id: "nux-223-hellbomb"
name: "Hellbomb"
collection: "stratagems"
aliases: ["NUX-223 Hellbomb"]
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: []
wiki_url: "https://helldivers.wiki.gg/wiki/NUX-223_Hellbomb"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/nux-223-hellbomb.json"
---

# Hellbomb

**分类：** 战略配备 (`stratagems`) · **ID：** `nux-223-hellbomb`

**别名：** NUX-223 Hellbomb

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/NUX-223_Hellbomb

## 简介

Helldivers must enter the following sequence in order to call down this special Stratagem during a mission:

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | mission |
| `availability` | objective |
| 类型 (`kind`) | mission |
| 特性 ID (`traitIds`) | — |
| 输入指令 (`code`) | down, up, left, down, up, right, down, up |
| 冷却时间（秒） (`cooldownS`) | 30 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 28.5 |
| 呼叫时间（秒） (`callInTimeS`) | 5 |
| 使用次数 (`uses`) | unlimited |
| `shipModules` | — |


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
| `type` | other |
| `label` |  |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| 消耗 (`cost`) | — |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/nux-223-hellbomb.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/NUX-223_Hellbomb
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

