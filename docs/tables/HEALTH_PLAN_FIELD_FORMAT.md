# HEALTH_PLAN_FIELD_FORMAT

> Contains field formatting rules for Health Plan fields.

**Description:** Health Plan Field Format  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FIELD_REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates that the Health Plan field is required. |
| 2 | `FIELD_TYPE_MEANING_TXT` | VARCHAR(12) |  |  | The meaning of the type of Health Plan field. Valid values would be "MEMBER" or "GROUP". |
| 3 | `FORMAT_MASK_TXT` | VARCHAR(100) |  |  | The format mask of the Health Plan field. |
| 4 | `HEALTH_PLAN_FIELD_FORMAT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a Health Plan field format. |
| 5 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Health Plan |
| 6 | `MIN_FORMAT_MASK_CHAR_CNT` | DOUBLE | NOT NULL |  | The minimum character count for the Health Plan field format mask. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |

