# SHX_RESPONSE

> Each row on the table represents discrete response for an assessment made

**Description:** SHX_RESPONSE  
**Table type:** ACTIVITY  
**Primary key:** `SHX_RESPONSE_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `RESPONSE_MODIFIER_FLAG` | DOUBLE | NOT NULL |  | 0 - Actual Age, 1 - About Age, 2 - Before Age, 4 - After Age, 5 - Unknown |
| 5 | `RESPONSE_TYPE` | VARCHAR(12) | NOT NULL |  | Indicates the type of entry on the SHX_ RESPONSE table. It can be ALPHA, NUMERIC, DATE |
| 6 | `RESPONSE_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for responses which are numeric in nature |
| 7 | `RESPONSE_VAL` | VARCHAR(255) | NOT NULL |  | Numeric or Text Response value |
| 8 | `SHX_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME: PROBLEM_SEQ unique identifier for the SHX_ ACTIVITY table. |
| 9 | `SHX_RESPONSE_ID` | DOUBLE | NOT NULL | PK | SEQUENCE NAME: PROBLEM_SEQ This is the table's primary key. the unique identifier for a shx_act_assessment table. |
| 10 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Task Assay Code from Code set 14003. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SHX_ACTIVITY_ID` | [SHX_ACTIVITY](SHX_ACTIVITY.md) | `SHX_ACTIVITY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SHX_ALPHA_RESPONSE](SHX_ALPHA_RESPONSE.md) | `SHX_RESPONSE_ID` |

