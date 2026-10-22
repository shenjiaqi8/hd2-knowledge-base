---
id: "eat-411-leveller"
name: "EAT-411 Leveller"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated", "broken_file_links"]
wiki_url: "https://helldivers.wiki.gg/wiki/EAT-411_Leveller"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/eat-411-leveller.json"
---

# EAT-411 Leveller

**分类：** 战略配备 (`stratagems`) · **ID：** `eat-411-leveller`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/EAT-411_Leveller

## 简介

The EAT-411 Leveller is a Stratagem that calls down a single disposable large area covering anti-tank Support Weapon.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, anti-tank, expendable |
| 输入指令 (`code`) | down, down, left, up, down |
| 冷却时间（秒） (`cooldownS`) | 140 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 133 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Streamlined Request Process |
| `shipModules\[1\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Morale Augmentation |
| `shipModules\[2\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | streamlined Launch Process |
| `shipModules\[3\].effect` | All Support Weapon stratagems launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. EAT-17 BACKBLAST E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 15 |
| `damage.durable` | 15 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 6 |
| `area.shockwaveRadiusM` | 7 |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 15 |


### 2. EAT-411 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1000 |
| `damage.durable` | 1000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | anti_tank_ii |
| `projectile.pellets` | — |
| `projectile.massG` | 500 |
| `projectile.initialVelocityMps` | 50 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 40 |
| `forces.stagger` | 50 |
| `forces.push` | 20 |


### 3. EAT-411 P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 2500 |
| `damage.durable` | 2500 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 10 |
| `area.outerRadiusM` | 25 |
| `area.shockwaveRadiusM` | 35 |
| `forces.demolition` | 40 |
| `forces.stagger` | 100 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Siege Breakers P2 |
| 战争债券 ID (`warbondId`) | siege-breakers |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 85 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/eat-411-leveller.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/EAT-411_Leveller
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

