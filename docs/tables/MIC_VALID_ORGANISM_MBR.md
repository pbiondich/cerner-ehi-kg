# MIC_VALID_ORGANISM_MBR

> This table lists the organisms which are valid for a given valid_organism_id.

**Description:** Valid organism members  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | Code value for organism on codeset 1021. |
| 2 | `STATISTICS_IND` | DOUBLE |  |  | Determines whether or not an organism should be sent to archive for statistics. 1 - Yes 0 - No |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `VALID_ORGANISM_ID` | DOUBLE | NOT NULL |  | Id that represents the service resource, procedure, and source combination for valid organisms |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

