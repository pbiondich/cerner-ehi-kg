# RC_SLA_ACTIVITY

> Holds reported SLA scheduling activity.

**Description:** Revenue Cycle Service Level Agreement Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Health Plan of the SLA. |
| 3 | `RC_SLA_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_SLA_ACTIVITY table. |
| 4 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the scheudling event related to this activity. |
| 5 | `SLA_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the units for this SLA value |
| 6 | `SLA_VALUE` | DOUBLE | NOT NULL |  | Contains the value of the SLA. |
| 7 | `SUBMIT_AUTH_BY_DT_TM` | DATETIME |  |  | The date by which the SLA must be authorized. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |

