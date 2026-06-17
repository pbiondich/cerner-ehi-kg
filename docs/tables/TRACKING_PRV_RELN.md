# TRACKING_PRV_RELN

> This table is used to store the new provider role assignments to a patient.

**Description:** TRACKING PRV RELN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGN_DT_TM` | DATETIME | NOT NULL |  | Date nTime at which this provider is assigned to the patient. |
| 2 | `TRACKING_ID` | DOUBLE | NOT NULL |  | Tracking id of the patient. this is internal number used to identify tracking. |
| 3 | `TRACKING_PROVIDER_ID` | DOUBLE | NOT NULL |  | person id of the provider |
| 4 | `TRACKING_PRV_RELN_ID` | DOUBLE | NOT NULL |  | Primary key which uniquely defines the row and is a internal number |
| 5 | `UNASSIGN_DT_TM` | DATETIME | NOT NULL |  | Date n time the Provider is unassigned from the patient. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

