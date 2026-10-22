---
id: "orbital-gas-strike"
name: "Orbital Gas Strike"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/Orbital_Gas_Strike"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-gas-strike.json"
---

# Orbital Gas Strike

**分类：** 战略配备 (`stratagems`) · **ID：** `orbital-gas-strike`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Orbital_Gas_Strike

## 简介

The Orbital Gas Strike is an offensive orbital Stratagem that disperses lingering gas that damages enemies and applies a confusion effect over a large area.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | offensive |
| `availability` | loadout |
| 类别 (`category`) | bridge |
| 类型 (`kind`) | orbital |
| 特性 ID (`traitIds`) | explosive, orbital, caustic |
| 输入指令 (`code`) | right, right, down, right |
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
| `unlockLevel` | 1 |
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

### 1. S P14（projectile）

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


### 2. S P14 IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 0 |
| `damage.durable` | 0 |
| `damage.type` | Gas |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 15 |
| `area.shockwaveRadiusM` | 20 |
| `forces.demolition` | 50 |
| `forces.stagger` | 10 |
| `forces.push` | 40 |


### 3. Gas（status）

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


### 4. Gas Confusion（status）

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
| `type` | requisition |
| `label` | Bridge |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 4000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-gas-strike.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Orbital_Gas_Strike
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

