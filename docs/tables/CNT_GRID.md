# CNT_GRID

> INTERSECTION DATA

**Description:** CNT GRID  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_DTA_KEY_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID (Value: 0.0) |
| 2 | `CNT_GRID_ID` | DOUBLE | NOT NULL |  | Sequence generated ID - PRIMARY KEY |
| 3 | `CNT_INPUT_KEY_ID` | DOUBLE | NOT NULL | FK→ | FK FROM CNT_INPUT_KEY table |
| 4 | `COL_TASK_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Column DTA |
| 5 | `INPUT_DESCRIPTION` | VARCHAR(200) |  |  | GRID INPUT DESCRIPTION |
| 6 | `INPUT_REF_SEQ` | DOUBLE |  |  | Sequence number of input control to control order that it is placed on the section. |
| 7 | `INT_EVENT_CD` | DOUBLE | NOT NULL |  | Event code |
| 8 | `INT_EVENT_CDUID` | VARCHAR(100) | NOT NULL |  | UNIQUE VALUE FROM CNT_CODE_VALUE_KEY |
| 9 | `ROW_TASK_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for row DTA |
| 10 | `SECTION_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Section - from CNT_INPUT_KEY table |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_DTA_KEY_ID` | [CNT_DTA_KEY2](CNT_DTA_KEY2.md) | `CNT_DTA_KEY_ID` |
| `CNT_INPUT_KEY_ID` | [CNT_INPUT_KEY](CNT_INPUT_KEY.md) | `CNT_INPUT_KEY_ID` |

