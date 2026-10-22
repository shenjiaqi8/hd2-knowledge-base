---
id: "orbital-smoke-strike"
name: "Orbital Smoke Strike"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/Orbital_Smoke_Strike"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-smoke-strike.json"
---

# Orbital Smoke Strike

**分类：** 战略配备 (`stratagems`) · **ID：** `orbital-smoke-strike`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Orbital_Smoke_Strike

## 简介

The Orbital Smoke Strike is a Stratagem that creates a large smokescreen to provide cover.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | offensive |
| `availability` | loadout |
| 类别 (`category`) | bridge |
| 类型 (`kind`) | orbital |
| 特性 ID (`traitIds`) | explosive, orbital |
| 输入指令 (`code`) | right, right, down, up |
| 冷却时间（秒） (`cooldownS`) | 75 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 71.25 |
| `cooldownVariants\[2\].label` | With Zero-G Breech Loading |
| `cooldownVariants\[2\].seconds` | 67.5 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 64.125 |
| 呼叫时间（秒） (`callInTimeS`) | 4.45 |
| `callInTimeUpgradedS` | 3.45 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 8 |
| `shipModules\[1\].department` | orbital_cannons |
| `shipModules\[1\].module` | Zero-G Breech Loading |
| `shipModules\[1\].effect` | Orbital stratagem cooldown time reduced by 10%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Targeting Software Upgrade |
| `shipModules\[2\].effect` | 1-second reduction in call-in time for all Orbital Stratagems. |
| `shipModules\[3\].department` | bridge |
| `shipModules\[3\].module` | Morale Augmentation |
| `shipModules\[3\].effect` | Reduces cooldown time for all Stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. S P24（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 300 |
| `damage.durable` | 300 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iii |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | anti_tank_ii |
| `projectile.pellets` | — |
| `projectile.massG` | 5000 |
| `projectile.initialVelocityMps` | 400 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 50 |
| `forces.stagger` | 60 |
| `forces.push` | 15 |


### 2. S P5 IE（explosion）

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
| `area.innerRadiusM` | 12 |
| `area.outerRadiusM` | 12 |
| `area.shockwaveRadiusM` | 0 |
| `forces.demolition` | — |
| `forces.stagger` | — |
| `forces.push` | — |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Bridge |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 4000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-smoke-strike.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Orbital_Smoke_Strike
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

