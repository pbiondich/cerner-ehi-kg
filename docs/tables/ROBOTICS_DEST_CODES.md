# ROBOTICS_DEST_CODES

> Destination code assignments per task assay for each service resource.

**Description:** ROBOTICS DEST CODES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AV_ERROR_CD` | DOUBLE | NOT NULL |  | Autoverify Error CodeColumn |
| 2 | `DESTINATION_CODE` | CHAR(2) |  |  | Numeric string representing a destination on the robotics line |
| 3 | `REFLEX_IND` | DOUBLE |  |  | An indicator to alert robotics that a rule exists that will cause a reflex test. |
| 4 | `ROBOTICS_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Service Resource that represents a robotics line |
| 5 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A service resource for an instrument associated with the robotics line.Column |
| 6 | `SLIDE_IND` | DOUBLE |  |  | Indicates that a slide will be made on the robotics line.Column |
| 7 | `SUBSEQ_SLIDE_IND` | DOUBLE |  |  | Indicates a slide should be made on the robotics line if this is a subsequent condition. |
| 8 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Discrete Task assay processing on robotics. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

