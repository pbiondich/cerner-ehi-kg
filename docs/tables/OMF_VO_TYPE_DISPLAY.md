# OMF_VO_TYPE_DISPLAY

> Contains the indicators and their ordering for a view option type.

**Description:** OMF View Option Type Display.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FILTER_ONLY_IND` | DOUBLE |  |  | Not currently used. |
| 3 | `REQUIRED_FILTER_IND` | DOUBLE |  |  | Not currently used. |
| 4 | `REQUIRED_IND` | DOUBLE |  |  | Not currently used. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VO_DISPLAY` | VARCHAR(100) |  |  | Text to display for this view option. |
| 11 | `VO_DISPLAY_SEQ` | DOUBLE | NOT NULL |  | Order to display this view option. |
| 12 | `VO_INDICATOR_CD` | DOUBLE | NOT NULL |  | Generic indicator code value of view option for vo_type_seq = 2. Other codesets can be used besides 14265 depending on the team defining the value. |
| 13 | `VO_TYPE_CD` | DOUBLE | NOT NULL |  | The group of view option indicators which this information applies to. Other codesets can be used besides 14210 depending on the team defining the value. |
| 14 | `VO_TYPE_SEQ` | DOUBLE | NOT NULL |  | Sequence which this information applies to. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

