---
id: "orbital-railcannon-strike"
name: "Orbital Railcannon Strike"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/Orbital_Railcannon_Strike"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-railcannon-strike.json"
---

# Orbital Railcannon Strike

**分类：** 战略配备 (`stratagems`) · **ID：** `orbital-railcannon-strike`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Orbital_Railcannon_Strike

## 简介

The Orbital Railcannon Strike, also known as the ORC or ORS, is an offensive stratagem that fires an auto-targeting projectile at the largest enemy nearby

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | offensive |
| `availability` | loadout |
| 类别 (`category`) | orbital_cannons |
| 类型 (`kind`) | orbital |
| 特性 ID (`traitIds`) | orbital, anti-tank |
| 输入指令 (`code`) | right, up, down, down, right |
| 冷却时间（秒） (`cooldownS`) | 180 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 171 |
| `cooldownVariants\[2\].label` | With Zero-G Breech Loading |
| `cooldownVariants\[2\].seconds` | 162 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 153.9 |
| 呼叫时间（秒） (`callInTimeS`) | 0 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 20 |
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

### 1. S P26（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 10000 |
| `damage.durable` | 10000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iii |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_iii |
| `penetration.extremeAngle` | anti_tank_iii |
| `projectile.pellets` | — |
| `projectile.massG` | 5000 |
| `projectile.initialVelocityMps` | 14000 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 0 |
| `area` | — |
| `forces.demolition` | 50 |
| `forces.stagger` | 60 |
| `forces.push` | 35 |


### 2. S P26 E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1000 |
| `damage.durable` | 1000 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 2.5 |
| `area.outerRadiusM` | 2.5 |
| `area.shockwaveRadiusM` | 10 |
| `forces.demolition` | 50 |
| `forces.stagger` | 30 |
| `forces.push` | 50 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Orbital Cannons |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 10000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-railcannon-strike.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Orbital_Railcannon_Strike
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

