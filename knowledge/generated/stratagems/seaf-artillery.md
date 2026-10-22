---
id: "seaf-artillery"
name: "SEAF Artillery"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: []
wiki_url: "https://helldivers.wiki.gg/wiki/SEAF_Artillery"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/seaf-artillery.json"
---

# SEAF Artillery

**分类：** 战略配备 (`stratagems`) · **ID：** `seaf-artillery`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/SEAF_Artillery

## 简介

SEAF Artillery is a generic Optional Objective consisting of a large, stationary artillery platform. To complete the objective, Helldivers must activate the artillery, load five shells into it and then connect it to their Super Destroyer. Upon completion, all Helldivers in the mission gain access to five uses of the SEAF Artillery stratagem.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | mission |
| `availability` | objective |
| 类型 (`kind`) | mission |
| 特性 ID (`traitIds`) | — |
| 输入指令 (`code`) | right, up, up, down |
| 冷却时间（秒） (`cooldownS`) | 15 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 13.3 |
| 使用次数 (`uses`) | unlimited |
| `shipModules` | — |


## 攻击模式、伤害与穿甲

### 1. S P10（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 4000 |
| `damage.durable` | 4000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iv |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | anti_tank_ii |
| `projectile.pellets` | — |
| `projectile.massG` | 70000 |
| `projectile.initialVelocityMps` | 300 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 1000 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 50 |
| `forces.stagger` | 50 |
| `forces.push` | 20 |


### 2. S P10 IE（explosion）

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


### 3. S P11（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 4000 |
| `damage.durable` | 4000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iv |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | anti_tank_ii |
| `projectile.pellets` | — |
| `projectile.massG` | 70000 |
| `projectile.initialVelocityMps` | 300 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 1000 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 50 |
| `forces.stagger` | 50 |
| `forces.push` | 20 |


### 4. S P11 IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 250 |
| `damage.durable` | 250 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1.60000002 |
| `area.outerRadiusM` | 13 |
| `area.shockwaveRadiusM` | 20 |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


### 5. BurningHeavy（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 200 |
| `damage.durable` | 200 |
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


### 6. Fire（status）

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


### 7. S P12（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 4000 |
| `damage.durable` | 4000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iv |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | anti_tank_ii |
| `projectile.pellets` | — |
| `projectile.massG` | 70000 |
| `projectile.initialVelocityMps` | 300 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 1000 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 50 |
| `forces.stagger` | 50 |
| `forces.push` | 20 |


### 8. S P12 IE（explosion）

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
| `area.innerRadiusM` | 13 |
| `area.outerRadiusM` | 13 |
| `area.shockwaveRadiusM` | 0 |
| `forces.demolition` | — |
| `forces.stagger` | — |
| `forces.push` | — |


### 9. S P7（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 4000 |
| `damage.durable` | 4000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iv |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | anti_tank_ii |
| `projectile.pellets` | — |
| `projectile.massG` | 70000 |
| `projectile.initialVelocityMps` | 300 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 1000 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 50 |
| `forces.stagger` | 50 |
| `forces.push` | 20 |


### 10. S P7 IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 0 |
| `damage.durable` | 0 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 13 |
| `area.shockwaveRadiusM` | 20 |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 0 |


### 11. Stun Medium（status）

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


### 12. S P8（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 4000 |
| `damage.durable` | 4000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iv |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | anti_tank_ii |
| `projectile.pellets` | — |
| `projectile.massG` | 70000 |
| `projectile.initialVelocityMps` | 300 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 1000 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 50 |
| `forces.stagger` | 50 |
| `forces.push` | 20 |


### 13. S P8 IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1500 |
| `damage.durable` | 1500 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 4 |
| `area.outerRadiusM` | 12 |
| `area.shockwaveRadiusM` | 18 |
| `forces.demolition` | 50 |
| `forces.stagger` | 70 |
| `forces.push` | 60 |


### 14. S P9（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 4000 |
| `damage.durable` | 4000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iv |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | anti_tank_ii |
| `projectile.pellets` | — |
| `projectile.massG` | 70000 |
| `projectile.initialVelocityMps` | 300 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 1000 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 50 |
| `forces.stagger` | 50 |
| `forces.push` | 20 |


### 15. S P9 IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1500 |
| `damage.durable` | 1500 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 6.69999981 |
| `area.outerRadiusM` | 20 |
| `area.shockwaveRadiusM` | 30 |
| `forces.demolition` | 50 |
| `forces.stagger` | 100 |
| `forces.push` | 40 |


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
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/seaf-artillery.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/SEAF_Artillery
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

