---
id: "exo-51-lumberer-exosuit"
name: "EXO-51 Lumberer Exosuit"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["broken_file_links"]
wiki_url: "https://helldivers.wiki.gg/wiki/EXO-51_Lumberer_Exosuit"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/exo-51-lumberer-exosuit.json"
---

# EXO-51 Lumberer Exosuit

**分类：** 战略配备 (`stratagems`) · **ID：** `exo-51-lumberer-exosuit`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/EXO-51_Lumberer_Exosuit

## 简介

The EXO-51 Lumberer Exosuit is an Exosuit Stratagem featuring an anti-tank cannon on the right arm and a flamethrower on the left.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | vehicle |
| 特性 ID (`traitIds`) | explosive, vehicle, incendiary, anti-tank |
| 输入指令 (`code`) | left, down, right, up, right, left, up |
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

### 1. P8（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1300 |
| `damage.durable` | 1300 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | medium |
| `projectile.pellets` | — |
| `projectile.massG` | 6500 |
| `projectile.initialVelocityMps` | 625 |
| `projectile.dragFactorPct` | 75 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 85 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 25 |


### 2. P8 IE（explosion）

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


### 3. LUMBERER FLAMETHROWER S（spray）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 8 |
| `damage.durable` | 8 |
| `damage.type` | Fire |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | heavy |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 5 |
| `forces.push` | 5 |


### 4. Fire（status）

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


### 5. Fire Panic（status）

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


### 6. FlamerSlowed（status）

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


### 7. Exosuit Stomp（other）

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


### 8. Exosuit Destruction（explosion）

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
| `label` | Exo Experts P2 |
| 战争债券 ID (`warbondId`) | exo-experts |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 50 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/exo-51-lumberer-exosuit.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/EXO-51_Lumberer_Exosuit
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

