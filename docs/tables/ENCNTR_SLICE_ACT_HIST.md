# ENCNTR_SLICE_ACT_HIST

> Used to store the encounter slice activity transactional history.

**Description:** Encounter Slice Activity History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COLUMN_CD` | DOUBLE | NOT NULL |  | The identifier for the column that the value_cd contains data for. |
| 4 | `COLUMN_VALUE_CD` | DOUBLE | NOT NULL |  | The value of the column on the parent_entity_name table and the parent_entity_id row. |
| 5 | `ENCNTR_SLICE_ACT_HIST_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. |
| 6 | `ENCNTR_SLICE_ACT_ID` | DOUBLE | NOT NULL | FK→ | The unique primary key of the ENCNTR_SLICE_ACT table. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID for the table row which for the table represented by the parent_entity_name. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The table which is being referenced. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_SLICE_ACT_ID` | [ENCNTR_SLICE_ACT](ENCNTR_SLICE_ACT.md) | `ENCNTR_SLICE_ACT_ID` |

