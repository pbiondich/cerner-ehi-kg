# WL_ACTIVITY_DETAIL

> This table will be used to store details off of the mp_worklist_act table. An example would be adding rows for clinical_events, while the parent table is the person/encounter.

**Description:** MP WORKLIST ACTIVITY DETAIL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Number is a primary key id on a different table, identified by PARENT_ENTITY_NAME. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the table being used for the parent_entity_id. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `WL_ACTIVITY_DETAIL_CD` | DOUBLE | NOT NULL |  | This code will identify the different details associated with an activity |
| 11 | `WL_ACTIVITY_DETAIL_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 12 | `WL_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the ACTIVITY for this detail record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WL_ACTIVITY_ID` | [WL_ACTIVITY](WL_ACTIVITY.md) | `WL_ACTIVITY_ID` |

