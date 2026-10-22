---
id: "exo-45-patriot-exosuit"
name: "EXO-45 Patriot Exosuit"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/EXO-45_Patriot_Exosuit"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/exo-45-patriot-exosuit.json"
---

# EXO-45 Patriot Exosuit

**分类：** 战略配备 (`stratagems`) · **ID：** `exo-45-patriot-exosuit`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/EXO-45_Patriot_Exosuit

## 简介

The EXO-45 Patriot Exosuit is an Exosuit Stratagem featuring a rocket pod on the left hand and a minigun on the right.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | robotics_workshop |
| 类型 (`kind`) | vehicle |
| 特性 ID (`traitIds`) | explosive, vehicle, anti-tank, medium-armor-penetrating |
| 输入指令 (`code`) | left, down, right, up, left, down, down |
| 冷却时间（秒） (`cooldownS`) | 600 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 399 |
| `cooldownVariants\[2\].label` | With DSS Boost |
| `cooldownVariants\[2\].seconds` | 273 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 252 |
| 呼叫时间（秒） (`callInTimeS`) | 10.5 |
| 使用次数 (`uses`) | 1 |
| `unlockLevel` | 25 |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time from all stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. MG-43 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 90 |
| `damage.durable` | 23 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | very_light |
| `projectile.pellets` | — |
| `projectile.massG` | 11 |
| `projectile.initialVelocityMps` | 820 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 12 |


### 2. P6（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1250 |
| `damage.durable` | 1250 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_i |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 2500 |
| `projectile.initialVelocityMps` | 200 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 85 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 40 |
| `forces.push` | 25 |


### 3. P6 IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 400 |
| `damage.durable` | 400 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 2 |
| `area.shockwaveRadiusM` | 4 |
| `forces.demolition` | 30 |
| `forces.stagger` | 60 |
| `forces.push` | 70 |


### 4. MLS-4X BACKBLAST E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 5 |
| `damage.durable` | 5 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 2 |
| `area.shockwaveRadiusM` | 3 |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 10 |


### 5. Exosuit Stomp（other）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 200 |
| `damage.durable` | 200 |
| `damage.type` | Damage |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | unarmored |
| `penetration.largeAngle` | unarmored |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 20 |
| `forces.push` | 20 |


### 6. Exosuit Destruction（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 200 |
| `damage.durable` | 200 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 0.6 |
| `area.outerRadiusM` | 7 |
| `area.shockwaveRadiusM` | 10 |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Robotics Workshop |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 20000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/exo-45-patriot-exosuit.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/EXO-45_Patriot_Exosuit
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

