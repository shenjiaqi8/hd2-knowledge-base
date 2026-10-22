---
id: "e-at-12-anti-tank-emplacement"
name: "E/AT-12 Anti-Tank Emplacement"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/E/AT-12_Anti-Tank_Emplacement"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/e-at-12-anti-tank-emplacement.json"
---

# E/AT-12 Anti-Tank Emplacement

**分类：** 战略配备 (`stratagems`) · **ID：** `e-at-12-anti-tank-emplacement`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/E/AT-12_Anti-Tank_Emplacement

## 简介

The Anti-Tank Emplacement, shortened to AT Emplacement or ATE, is a Stratagem that deploys a heavy anti-tank cannon.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | defensive |
| `availability` | loadout |
| 类型 (`kind`) | emplacement |
| 特性 ID (`traitIds`) | hellpod, anti-tank |
| 输入指令 (`code`) | down, up, left, right, right, right |
| 冷却时间（秒） (`cooldownS`) | 180 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 171 |
| `cooldownVariants\[2\].label` | With Synthetic Supplementation |
| `cooldownVariants\[2\].seconds` | 162 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 153.9 |
| 呼叫时间（秒） (`callInTimeS`) | 3 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time for all stratagems by 5%. |
| `shipModules\[2\].department` | engineering_bay |
| `shipModules\[2\].module` | Synthetic Supplementation |
| `shipModules\[2\].effect` | Reduces cooldown time for Sentry, Emplacement, and Resupply stratagems by 10%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Rapid Launch System |
| `shipModules\[3\].effect` | Removes deployment time for Emplacement stratagems. |


## 攻击模式、伤害与穿甲

### 1. ET Cannon 75mm APHE（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1300 |
| `damage.durable` | 1300 |
| `damage.type` | Damage |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | medium |
| `projectile.pellets` | — |
| `projectile.massG` | 6500 |
| `projectile.initialVelocityMps` | 625 |
| `projectile.dragFactorPct` | 75 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 25 |


### 2. ET APHE 75mm（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 150 |
| `damage.durable` | 150 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 3 |
| `area.outerRadiusM` | 6 |
| `area.shockwaveRadiusM` | 7 |
| `forces.demolition` | 30 |
| `forces.stagger` | 60 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Urban Legends P3 |
| 战争债券 ID (`warbondId`) | urban-legends |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 110 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/e-at-12-anti-tank-emplacement.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/E/AT-12_Anti-Tank_Emplacement
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

