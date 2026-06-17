# SHX_ALPHA_RESPONSE

> Each row on the table represents discrete response for an assessment made

**Description:** SHX_ALPHA_RESPONSE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the nomenclature table. |
| 5 | `OTHER_TEXT` | VARCHAR(255) | NOT NULL |  | Indicates the type of entry on the SHX_ RESPONSE table. It can be ALPHA, NUMERIC, DATE |
| 6 | `SHX_ALPHA_RESPONSE_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME: PROBLEM_SEQ This is the table's primary key. the unique identifier for a shx_act_assessment table. |
| 7 | `SHX_RESPONSE_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME: PROBLEM_SEQ unique identifier for the SHX_ ACTIVITY table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `SHX_RESPONSE_ID` | [SHX_RESPONSE](SHX_RESPONSE.md) | `SHX_RESPONSE_ID` |

