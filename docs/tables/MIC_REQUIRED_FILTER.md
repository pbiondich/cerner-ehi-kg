# MIC_REQUIRED_FILTER

> This reference table contains the required filters for a sequence before it can be utilized to generate a report.

**Description:** Microbiology Required Filter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILTER_CD` | DOUBLE | NOT NULL |  | The field contains the internal identification code assigned to the filter stored on code_set 25212. This field identifies a required filter for the associated report type. |
| 2 | `FILTER_SEQ` | DOUBLE | NOT NULL |  | This field, in conjunction with the value included in the report_type_cd and filter_cd field, uniquely identifies a row on this table. |
| 3 | `REPORT_TYPE_CD` | DOUBLE | NOT NULL |  | The field contains the internal identification code assigned to the repot type stored on code_set 25211. This field identifies a report type that has a required filter for the associated filter. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

