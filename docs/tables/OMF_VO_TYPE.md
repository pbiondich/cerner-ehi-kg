# OMF_VO_TYPE

> Top level information about PowerVision view options to be displayed

**Description:** OMF View options types.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABSTRACT_TABLE_NAME` | VARCHAR(50) |  |  | The name of the table from which the view engine will pull abstract data demographics info. |
| 2 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | The contributing source code |
| 3 | `MIN_PARAMS` | DOUBLE |  |  | Minimum number of options which must be chosen for this view option type. Not currently used. |
| 4 | `MULTIPLE_IND` | DOUBLE |  |  | Indicates whether more than one option may be chosen. Not currently used. |
| 5 | `TITLE` | VARCHAR(100) |  |  | Title to be displayed on the view option folder in PowerVision. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VO_ABSTRACT_FLAG` | DOUBLE |  |  | Determines if this data element is an abstract dimension or abstract fact. |
| 12 | `VO_INDICATOR_CD` | DOUBLE | NOT NULL |  | Generic indicator code value which this set of view option belongs to. Other codesets can be used besides 14265 depending on the team defining the value. |
| 13 | `VO_TYPE_CD` | DOUBLE | NOT NULL |  | Set of view options which may be chosen to appear on a grid. It is possible to use one of these for multiple grids. Other codesets can be used besides 14210 depending on the team defining the value. |
| 14 | `VO_TYPE_SEQ` | DOUBLE | NOT NULL |  | Sequence. For 'non-related' facts/dimensions there will only be 1 here. For 'related' facts/dimensions such as those involving event ranges there will be 2. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

