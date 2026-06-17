# OMF_ABSTRACT_SOURCE

> Stores the contributor information for the abstract data.

**Description:** OMF ABSTRACT SOURCE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | The contributing source system for the abstract data element. |
| 2 | `SOURCE_BEG_EFFECTIVE_COLUMN` | VARCHAR(50) |  |  | The ccl statement that defines the beginning effective date for the where clause used in the PowerVision view. |
| 3 | `SOURCE_CD_COLUMN` | VARCHAR(50) |  |  | The ccl statement that defines the group by column used in the select stmt for the PowerVision view. |
| 4 | `SOURCE_DISPLAY_COLUMN` | VARCHAR(50) |  |  | The ccl statement that defines the display column for the select stmt used in the PowerVision view. |
| 5 | `SOURCE_END_EFFECTIVE_COLUMN` | VARCHAR(50) |  |  | The ccl statement that defines the end effective date for the where clause used in the PowerVision view. |
| 6 | `SOURCE_TABLE` | VARCHAR(50) |  |  | The ccl statement that defines the from clause for the select stmt used in the PowerVision view. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

