---
id: "exo-55-breakthrough-exosuit"
name: "EXO-55 Breakthrough Exosuit"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/EXO-55_Breakthrough_Exosuit"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/exo-55-breakthrough-exosuit.json"
---

# EXO-55 Breakthrough Exosuit

**分类：** 战略配备 (`stratagems`) · **ID：** `exo-55-breakthrough-exosuit`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/EXO-55_Breakthrough_Exosuit

## 简介

The EXO-55 Breakthrough Exosuit is an Exosuit Stratagem featuring a heavy flak cannon on the right arm and a massive ballistic shield on the left.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | vehicle |
| 特性 ID (`traitIds`) | vehicle, heavy-armor-penetrating |
| 输入指令 (`code`) | left, down, right, left, right, down, up |
| 冷却时间（秒） (`cooldownS`) | 420 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 399 |
| `cooldownVariants\[2\].label` | With DSS Boost |
| `cooldownVariants\[2\].seconds` | 273 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 252 |
| 呼叫时间（秒） (`callInTimeS`) | 10.5 |
| 使用次数 (`uses`) | 3 |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time from all stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. P9（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 90 |
| `damage.durable` | 30 |
| `damage.type` | Ballistic |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | 40 |
| `projectile.massG` | 6 |
| `projectile.initialVelocityMps` | 385 |
| `projectile.dragFactorPct` | 120 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 20 |
| `forces.stagger` | 40 |
| `forces.push` | 30 |


### 2. Shield Bash（other）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 500 |
| `damage.durable` | 500 |
| `damage.type` | Melee |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | unarmored |
| `penetration.largeAngle` | unarmored |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 45 |
| `forces.push` | 20 |


### 3. Exosuit Stomp（other）

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


### 4. Exosuit Destruction（explosion）

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
| `type` | warbond |
| `label` | Exo Experts P3 |
| 战争债券 ID (`warbondId`) | exo-experts |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 50 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/exo-55-breakthrough-exosuit.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/EXO-55_Breakthrough_Exosuit
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

