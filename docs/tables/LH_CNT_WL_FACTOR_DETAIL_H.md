# LH_CNT_WL_FACTOR_DETAIL_H

> This table is used to store the history of table LH_CNT_WL_FACTOR_DETAIL

**Description:** LH_CNT_WL_FACTOR_DETAIL_HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `DETAIL_TXT` | VARCHAR(255) |  |  | This column will be used to store any textual information that needs to be saved for the detail |
| 3 | `DETAIL_TYPE_CD` | DOUBLE | NOT NULL |  | CODE SET: 4003482. Identifies what kind of information this detail row stores. Examples include: Order information, Severity information, Clinical Event information, etc. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `KEY_IND` | DOUBLE | NOT NULL |  | Used to group a set of details together to form a "key" |
| 6 | `LH_CNT_WL_FACTOR_DETAIL_H_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `LH_CNT_WL_FACTOR_DETAIL_ID` | DOUBLE | NOT NULL |  | FK Value from the LH_CNT_WL_FACTOR_DETAIL table |
| 8 | `LH_CNT_WL_FACTOR_ID` | DOUBLE | NOT NULL |  | Foreign Key to LH_CNT_WL_FACTOR |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The Unique Identifier from the corresponding table referenced in PARENT_ENTITY_NAME which identifies patient attribute. |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The upper case name of the table to which this address row is related (i.e., ORDER,CLINICAL_EVENT,CATALOG_CD, etc.) |
| 11 | `PARENT_FACTOR_DETAIL_ID` | DOUBLE | NOT NULL |  | Used to define a detail hierarchy. A detail can have zero or more child details |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

