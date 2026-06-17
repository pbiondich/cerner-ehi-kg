# DM_TEXT_FIND_HIGHLIGHT

> This table will store highlights found in unstructured data content which will be used for assembling ICD9 content reports.

**Description:** Data Management - Text Find Highlight  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_TEXT_FIND_CAT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key reference to the search category associated with this data |
| 2 | `DM_TEXT_FIND_DATA_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key reference to the data object associated with this data |
| 3 | `DM_TEXT_FIND_HIGHLIGHT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `HIGHLIGHT_SOURCE_NAME` | VARCHAR(50) | NOT NULL |  | The Source NAME used to find the Highlights for this row |
| 5 | `HIGHLIGHT_TEXT` | VARCHAR(250) | NOT NULL |  | The context in which this highlight was found |
| 6 | `HIGHLIGHT_WEIGHT` | DOUBLE |  |  | The weighting of this highlight. Higher numbers indicate more reliable results |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_TEXT_FIND_CAT_ID` | [DM_TEXT_FIND_CAT](DM_TEXT_FIND_CAT.md) | `DM_TEXT_FIND_CAT_ID` |
| `DM_TEXT_FIND_DATA_ID` | [DM_TEXT_FIND_DATA](DM_TEXT_FIND_DATA.md) | `DM_TEXT_FIND_DATA_ID` |

