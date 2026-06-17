# RX_HEALTH_PLAN_CLAIM

> List of claim fields that can be flexed by health plan and by claim format.

**Description:** Pharmacy Health Plan Claim  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLAIM_FIELD_CD` | DOUBLE | NOT NULL | FK→ | Determines which claim field type is being flexed. |
| 2 | `CLAIM_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | Used to flex claim fields at the claim format level. The same health plan can be flexed using multiple claim formats. |
| 3 | `CODE_VALUE_CD` | DOUBLE | NOT NULL | FK→ | Determines the value that a specific claim field is flexed with. |
| 4 | `FIELD_ALIAS_CD` | DOUBLE | NOT NULL |  | Stores a code_value for a PERSON or PRSNL alias associated with the claim. |
| 5 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Determines what health plan the fields are related to. Used to flex claim fields at the health plan level. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLAIM_FIELD_CD` | [RX_CLAIM_FIELD](RX_CLAIM_FIELD.md) | `CLAIM_FIELD_CD` |
| `CLAIM_FORMAT_ID` | [RX_CLAIM_FORMAT](RX_CLAIM_FORMAT.md) | `FORMAT_ID` |
| `CODE_VALUE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `HEALTH_PLAN_ID` | [RX_HEALTH_PLAN](RX_HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |

