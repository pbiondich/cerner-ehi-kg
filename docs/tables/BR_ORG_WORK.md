# BR_ORG_WORK

> legacy organizations

**Description:** BEDROCK ORGANIZATION WORK  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `LAB_IND` | DOUBLE | NOT NULL |  | If the indicator is a 1 then the location is a laboratory, if 0 then it is not |
| 3 | `NAME` | VARCHAR(60) |  |  | name of the organization |
| 4 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | identifies the organization |
| 5 | `ORG_DISPLAY` | VARCHAR(50) |  |  | short name of the organization |
| 6 | `PREFIX` | VARCHAR(4) |  |  | prefix name for the org |
| 7 | `START_IND` | DOUBLE | NOT NULL |  | indicates if the org should replace the START org |
| 8 | `STATUS_IND` | DOUBLE | NOT NULL |  | 1 = completed. |
| 9 | `TAX_ID_NBR` | VARCHAR(100) |  |  | tax number of the organization |
| 10 | `TIME_ZONE_ID` | DOUBLE | NOT NULL |  | time zone for the organization |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

