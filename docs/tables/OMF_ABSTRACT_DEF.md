# OMF_ABSTRACT_DEF

> Stores abstract data element definitions. Currently supports ProFile's abstract data.

**Description:** Stores abstract data element definitions.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABSTRACT_DEF_CD` | DOUBLE | NOT NULL |  | The unique identifier for an abstract data element. |
| 2 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | The contributing source system for the abstract data element. |
| 3 | `INDICATOR_CD` | DOUBLE | NOT NULL |  | The PowerVision indicator defined for viewing of the abstract data element. |
| 4 | `OMF_FACT_IND` | DOUBLE |  |  | Defines whether the indicator is a dimension (0) or fact (1). |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

