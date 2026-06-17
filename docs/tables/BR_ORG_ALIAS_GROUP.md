# BR_ORG_ALIAS_GROUP

> Grouping table for organizations for alias pool creation

**Description:** BEDROCK ORGANIZATION ALIAS GROUP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Identifies the organization |
| 3 | `PARENT_ORG_ID` | DOUBLE | NOT NULL |  | The id of the organization from which this organization was derived |
| 4 | `PATIENT_SEQ` | DOUBLE | NOT NULL |  | A number defining the grouping of the organization for patient number alias pools |
| 5 | `PHYS_SEQ` | DOUBLE | NOT NULL |  | A number defining the grouping of the organization for physician number alias pools |
| 6 | `PROCESS_FLAG` | DOUBLE |  |  | A flag indicating the processing status of the org alias group |
| 7 | `PRSNL_SEQ` | DOUBLE | NOT NULL |  | A number defining the grouping of the organization for personnel number alias pools |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VISIT_SEQ` | DOUBLE | NOT NULL |  | A number defining the grouping of the organization for visit number alias pools |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

